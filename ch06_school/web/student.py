from typing import List

from fastapi import APIRouter, HTTPException, Body

from ch06_school import data
from ch06_school.error import Missing, Duplicate, StudentNotFoundException
from ch06_school.model.student import StudentResponse, RequestDeptId, AssignDepartment
from ch06_school.service import student as service

router = APIRouter(prefix="/students")

@router.get("/")
def get_all() -> List[StudentResponse]:
    return service.find_all()

@router.get("/{id}")
def find_by_id(id: int) -> StudentResponse:
    return service.find_by_id(id)
    raise StudentNotFoundException(id)

@router.patch("/{student_id}")
def assign_student(student_id: int, request_dto: RequestDeptId=Body()) -> StudentResponse:
    assign_dto = AssignDepartment(student_id=student_id, dept_id=request_dto.dept_id)
    return service.assign_student(assign_dto)