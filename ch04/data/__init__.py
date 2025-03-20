from sqlite3 import Connection, Cursor, connect
from typing import Optional

con: Optional[Connection] = None
cur: Optional[Cursor] = None

def get_db():
    global con, cur
    if con is None:
        print("Connection")
        con = connect('mydb.db')
        cur = con.cursor()
get_db()