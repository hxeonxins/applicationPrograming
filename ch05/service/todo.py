from typing import List

from ch05.model.todo import TodoResponse, Todo
from ch05.fake import todo as data
# from ch05.data import todo as data

def get_all() -> List[TodoResponse]:
    return data.get_all()

def insert_one(todo: Todo) -> TodoResponse:
    return data.insert_one(todo)