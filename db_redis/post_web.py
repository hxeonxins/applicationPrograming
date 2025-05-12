# 게시판 post 페이징으로 전체 조회
from fastapi import Query

import pymysql
import uvicorn
from fastapi import FastAPI

app = FastAPI()

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

    return {
        "page": page,
        "size": size,
        "total": total,
        "posts": posts
    }


if __name__ == "__main__":
    uvicorn.run("post_web:app", port=8000, host="0.0.0.0")