from typing import List

from fastapi import APIRouter

from ch05.model.todo import TodoResponse, Todo
from ch05.service import todo as service

router = APIRouter(prefix="/todo") #todo로 들어오는 엔드 포인트 관리

#top-down 방식으로 구현
#@app.get -> router.get
@router.get('')
def get_all() -> List[TodoResponse]:
    return service.get_all()

router.post('')
def insert_one(task: Todo) -> TodoResponse:
    return service.insert_one(task)
#단건 조회, 수정, 삭제 일 때는 str 쓰자~