from typing import List

from fastapi import APIRouter

from ch06_school import data
from ch06_school.model.department import DepartmentResponse
from ch06_school.model.department import Department
router = APIRouter(prefix="/departments")

router.get("/")
def get_all() -> List[DepartmentResponse]:
    return data.find_all()