from datetime import datetime

from pydantic import BaseModel


class Todo(BaseModel):
    task: str

#Request 는 생략
class TodoResponse(Todo): #Todo 상속 받아서 사용
    task_id: int
    completed: int
    created_at: str#datetime