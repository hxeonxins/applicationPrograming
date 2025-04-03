from datetime import datetime
from typing import List

from ch05.error import Missing
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
    todo_id = todo_id+1
    _todos.append(TodoResponse(
        todo_id=todo_id,
        task=todo.task,
        completed=0,
        created_at=datetime.now()
    ))
    return _todos[todo_id]

def get_one(todo_id: int) -> TodoResponse:
    _todo = next((x for x in _todos if x.todo_id == todo_id), None)

    #exception
    if _todo is None:
        raise Missing(message=f'todo was not found')

    return _todo

def modify_completed(todo: Todo) -> TodoResponse:
    _todo = get_one(todo)
    _todo.completed = not _todo.completed
    return _todo

def delete_task(todo_id: int) -> bool:
    #해당하는 task get_one으로 찾기
    _todo = get_one(todo_id)
    if _todo is None:
        return False
    _todos.remove(_todo)
    return True