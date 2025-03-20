import sqlite3
from http.client import HTTPException

from fastapi import FastAPI, Depends, Query

app = FastAPI()

def user_get(name: str = Query(...), gender:str = Query(...)):
    return {"name": name, "gender": gender}

@app.get("/user")
def get_user(user: dict = Depends(user_get)): #method no ()
    return user

#2. 토큰 확인 후 권한 부여
def check_admin(token: str = Query(...)):
    if token == "secure_token_2_1":
        return {"role":"admin"}
    raise HTTPException(status_code=401, detail="Invalid token")

#3. db connection
class Databas():

    def __init__(self):
        self.connection = sqlite3.connect("ch03.db")
    def get_connect(self):
       return self.connection #no 근본;;

def get_db():
    db = Databas()
    return db
@app.get("/db")
def get_db(connection: str = Depends(get_db)): #connection에 접근. 원래는 connection타입이 있음..
    return {"db_connection": connection}


@app.get("/check_admin")
def check_ad(user: dict = Depends(check_admin)):
    return {"message": "welcome", "user": user}

# if __name__ == '__main__':
#     import uvicorn
#     uvicorn.run("depends:app", reload=True, port=8082)

#4. 전체 라우터 수준에서 의존성 주입
def verify_token(token: str = Query(...)):
    if token != "secure_token_2_1":
        raise HTTPException(status_code=401, detail="Invalid token")
app_dep = FastAPI()
@app_dep.get("/public")
def public_endpoint():
    return {"message": "public endpoint"}

@app_dep.get("/private", dependencies=[Depends(verify_token)])
def public_endpoint():
    return {"message": "private endpoint"}

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("depends:app_dep", reload=True, port=8082)