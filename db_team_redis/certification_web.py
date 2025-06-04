from random import random

import pymysql
import redis
import uvicorn
from fastapi import FastAPI, Body, HTTPException
from random import randint
from pydantic import BaseModel

class VerifyRequest(BaseModel):
    number: str
    code: str

app = FastAPI()

#create redis client
redis_client = redis.Redis(host='localhost', port=6379, db=0)

#db connection
def get_connect():
    return pymysql.connect(
        host="localhost",
        port=3307,
        user="root",
        passwd="1234",
        db="test",
        charset="utf8",
    )

#인증 코드 발송
@app.post("/verified")
def create_verified(number: str = Body(...)):
    code = str(randint(100000, 999999))
    redis_client.setex(f"verified:{number}", 180, code)
    print(f"[web 발신]"
          f"인증 코드는 {code}입니다."
          f"절대 타인에게 노출시키지 마세요.")
    return {"message": "인증 코드가 발송 되었습니다. 기기에서 확인해 주세요."}

#인증 코드 확인
@app.post("/verify/check")
def verify_check(payload: VerifyRequest):
    number = payload.number
    code = payload.code
    save_code = redis_client.get(f"verified:{number}")
    if not save_code:
        raise HTTPException(status_code=400, detail="인증 코드가 만료되었거나 존재하지 않습니다.")
    if code != save_code.decode():
        raise HTTPException(status_code=400, detail="인증 코드가 일치하지 않습니다.")

    #인증 성공 시 디비 업데이트
    conn = get_connect()
    cur = conn.cursor()
    cur.execute("UPDATE user SET isVerified = 1 WHERE number = %s", (number,))
    conn.commit()
    cur.close()
    conn.close()

    # 인증 성공 후 Redis에서 제거해도 됨
    redis_client.delete(f"verified:{number}")

    return {"message": "인증이 완료되었습니다."}

if __name__ == "__main__":
    uvicorn.run("certification_web:app", host="0.0.0.0", port=8000)