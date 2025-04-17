# 연결 -> singleton
from sqlite3 import Connection, Cursor, connect
from typing import Optional
from .department import find_all, find_by_id, save

con: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_db():
    global con, cur
    if con is None:
        # 연결 시키기
        con = connect('./my_db', check_same_thread=False)
        cur = con.cursor()

get_db()