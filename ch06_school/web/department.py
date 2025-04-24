from typing import List

from fastapi import APIRouter, HTTPException, Body

from ch06_school.data import department as data
from ch06_school.error import Missing, Duplicate
from ch06_school.model.department import DepartmentResponse
from ch06_school.model.department import Department
router = APIRouter(prefix="/departments")

@router.get("/")
def get_all() -> List[DepartmentResponse]:
    return data.find_all()

@router.get("/{id}")
def get_by_id(id: int) -> DepartmentResponse:
    try:
        return data.find_by_id(id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.message)

@router.post("/")
def create_department(department: Department = Body()) -> DepartmentResponse:
    try:
        data.save(department)
    except Duplicate as e:
        raise HTTPException(status_code=409, detail=e.message)

@router.delete("/{id}")
def delete_department(id: int) -> bool:
    try:
        return data.delete(id)
    except Missing as e:
        raise HTTPException(status_code=404, detail=e.message)