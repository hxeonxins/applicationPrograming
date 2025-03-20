#SQlite 연동
#서버 필요 없음, 로컬 데이터 저장에 많이 사용

import sqlite3

from fastapi import params

#데이터 베이스 연결
con = sqlite3.connect("study.db") #study.db 에 연결
cur = con.cursor()

#테이블 생성 - cur
cur.execute('''
create table if not exists person(
    id integer primary key autoincrement,
    name text not null,
    age integer)
''')

#insert into
cur.execute('insert into person(name, age) values(?,?)', ('ch01', 25))
name = "sim"
age = 18
cur.execute(f"insert into person(name, age) values('{name}', {age})") #자주 하는 실수 -> '{name}'를 해줘야 문자열 인식
con.commit()

cur.execute("select * from person")
rows = cur.fetchall()
for row in rows:
    print(row)

#업데이트 - 가장 많이 쓰임
query = "update person set age = :age where name = :name"
params = {"name": "ch01", "age":28}
cur.execute(query, params)
con.commit()

cur.execute("select * from person")
rows = cur.fetchall()
for row in rows:
    print(row)

#delete
cur.execute("delete from person where name = :name", {"name": "sim"})
con.commit()
cur.execute("select * from person")
rows = cur.fetchall()

#연결 끊기
cur.close()
con.close()