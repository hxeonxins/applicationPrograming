from datetime import datetime
from typing import List

from ch05.model.todo import TodoResponse, Todo

_todos = [
    TodoResponse(
        todo_id=0,
        task="Study fastapi 1",
        completed=0,
        created_at=datetime.now()
    ),
    TodoResponse(
        todo_id=1,
        task="Study fastapi 2",
        completed=1,
        created_at=datetime.now()
    )
]

#insert 시 todo_id 공통 관리
todo_id=1


def get_all() -> List[TodoResponse]:
    return _todos

def insert_one(todo: Todo) -> TodoResponse:
    global todo_id
    # if next((x for x in _todos if x.task == todo.task), None):
    #     print("중복됨")
    #     return None
    todo_id = todo_id+1
    _todos.append(TodoResponse(
        todo_id=todo_id,
        task=todo.task,
        completed=0,
        created_at=datetime.now()
    ))
    return _todos[todo_id]