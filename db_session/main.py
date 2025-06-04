import json
import uuid
import redis
import uvicorn
from fastapi import FastAPI, Body, HTTPException
from starlette.requests import Request
from starlette.responses import Response, RedirectResponse

from db_session.login import fake_users, LoginUser

app = FastAPI()
redis_client = redis.Redis(host="localhost", port=6379, db=0)

SESSION_COOKIE_NAME = "session_id"
SESSION_TTL_SECONDS = 3600  # 60*60 -> 최초 로그인부터 1시간 동안 살아있음

@app.post("/session/login")
def login(response: Response, login_user: LoginUser = Body()):
    find_user = next((user for user in fake_users
                     if user.username == login_user.username), None)
    if not find_user or find_user.password != login_user.password:
        raise HTTPException(status_code=404, detail="Invalid username or password")

    session_id = str(uuid.uuid4())
    redis_client.setex(session_id, SESSION_TTL_SECONDS, json.dumps(find_user.dict()))

    response.set_cookie(
        key = SESSION_COOKIE_NAME,
        value = session_id,
        max_age = SESSION_TTL_SECONDS,
        httponly = True, # false면 HTTPS에서만 동작
    )

    response.body = b"session login success"
    response.status_code = 200
    return response

# 권한별 페이지 리턴
@app.get("/session/page")
def page(request: Request):
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    if not session_id:
        raise HTTPException(status_code=404, detail="Invalid session id")
    get_user = redis_client.get(session_id)
    get_user = json.loads(get_user)

    if get_user is None:
        raise HTTPException(status_code=404, detail="Invalid session id")

    # 권한 별 리턴
    if str(get_user['admin']) == "True":
        return Response(content="admin page", status_code=200)
    return Response(content="user page", status_code=200)

# 쿠키 없애기
@app.post("/session/logout")
def logout(request: Request, response: Response):
    session_id = request.cookies.get(SESSION_COOKIE_NAME)
    if session_id:
        redis_client.delete(session_id)
        response.delete_cookie(SESSION_COOKIE_NAME)
        response.body = b"session logout success"
        response.status_code = 200
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0")