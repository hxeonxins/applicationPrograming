from typing import List

from fastapi import APIRouter, HTTPException, Body

from ch06_school import data
from ch06_school.error import Missing, Duplicate, StudentNotFoundException
from ch06_school.model.student import StudentResponse
from ch06_school import service

router = APIRouter(prefix="/students")

router.get("/")
def get_all() -> List[StudentResponse]:
    return service.find_all()

router.get("/{id}")
def find_by_id(id: int) -> StudentResponse:
    return service.find_by_id()
    raise StudentNotFoundException(id)