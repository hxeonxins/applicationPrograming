import json
import uuid
import redis
import uvicorn
from fastapi import FastAPI, Body, HTTPException
from jose import jwt
from starlette import status
from starlette.requests import Request
from starlette.responses import Response, RedirectResponse

from db_session.jwt_util import create_access_token
from db_session.login import fake_users, LoginUser

app = FastAPI()
redis_client = redis.Redis(host="localhost", port=6379, db=0)

SESSION_COOKIE_NAME = "session_id"
SESSION_TTL_SECONDS = 3600  # 60*60 -> 최초 로그인부터 1시간 동안 살아있음

# jwt로 로그인 구현
@app.post("/jwt/login")
def login_jwt(response: Response, login_user: LoginUser = Body()):
    find_user = next((user for user in fake_users
                     if user.username == login_user.username), None)
    if not find_user or find_user.password != login_user.password:
        raise HTTPException(status_code=404, detail="Invalid username or password")

    # 토큰에 포함시킬 데이터 선정
    token_data = {"username": find_user.username,
                  "admin": find_user.admin}

    # jwt 토큰 생성
    access_token = create_access_token(data=token_data)

    response.set_cookie(
        key="access_token",
        value=access_token,
        httponly=True,
        samesite="strict",
        secure=False,
        path="/"
    )
    response.status_code = status.HTTP_200_OK
    response.body = b"jwt login ok"
    return response

    # return {"access_token": access_token}

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
@app.post("/jwt/logout")
def logout_jwt(response: Response):
    response.delete_cookie("access_token")
    response.status_code = status.HTTP_200_OK
    response.body = b"jwt logout ok"
    return response

if __name__ == "__main__":
    uvicorn.run("main:app", port=8000, host="0.0.0.0", reload=True)