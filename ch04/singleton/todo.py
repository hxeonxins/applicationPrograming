#create table
from typing import List, Tuple

from ch03.sqlite import query
from ch04.data import cur, con
from ch04.models import TodoResponse, Todo

cur.execute('''
create table if not exists todo(
    task_id integer primary key autoincrement,
    task text not null unique,
    completed integer not null default 0,
    created_at text not null default(datetime('now', 'localtime'))
) 
''')

def row_to_model(entity: Tuple) -> TodoResponse:
    task_id, task, completed, created_at = entity
    return TodoResponse(
        task_id=task_id,
        task=task,
        completed=completed,
        created_at=created_at
    )

def find_all() -> List[TodoResponse]:#model에서 정의 필요
    cur.execute("select * from todo")
    return [row_to_model(row) for row in cur.fetchall()] #list type return (no 근본 but 간편)

def insert_one(task: Todo):
    query="insert into todo(task) values(:task)"
    cur.execute(query, task.model_dump())
    con.commit()