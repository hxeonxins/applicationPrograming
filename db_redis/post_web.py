# 게시판 post 페이징으로 전체 조회
import json

import redis
from fastapi import Query

import pymysql
import uvicorn
from fastapi import FastAPI

app = FastAPI()

#redis로 게시글 조회하기
redis_client = redis.Redis(host="localhost", port=6379, db=0)

#디비 접속
def get_connect():
    return pymysql.connect(
        host="localhost",
        port=3307,
        user="root",
        passwd="1234",
        db="test",
        charset="utf8",
    )

@app.get("/post")
def get_post(page: int = Query(default=1, ge=1), size: int = Query(default=10, le=100)):
    #키 값 정의
    cache_key = f"post:{page}:size:{size}"

    #redis에 있으면 디비 접속할 필요 없음
    cached = redis_client.get(cache_key, page)
    if cached:
        print("redis cached")
        return {
            "page": page,
            "size": size,
            "total": int(redis_client.get('post:total')),
            "posts": json.loads(cached)
        }

    #db 접속
    conn = get_connect()
    cur = conn.cursor()

    offset = (page - 1) * size

    #쿼리 날리기 - 전체 게시글 조회(총 페이지 수 계산용)
    cur.execute("select count(*) as total from posts")
    total = cur.fetchone()[0]

    #페이징 된 게시글 가져오기
    cur.execute(f"select id, title, created_at "
                f"from posts order by created_at desc limit {size} offset {offset}")
    posts = cur.fetchall()

    cur.close()
    conn.close()

    redis_client.setex('posts:total', 60, total)
    redis_client.setex(cache_key, 60, json.dumps(posts))

    return {
        "page": page,
        "size": size,
        "total": total,
        "posts": posts
    }


if __name__ == "__main__":
    uvicorn.run("post_web:app", port=8000, host="0.0.0.0")