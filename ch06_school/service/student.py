from typing import List

from joblib.testing import raises

from ch06_school import service
from ch06_school.error import StudentNotFoundException
from ch06_school.model.student import StudentResponse, RequestDeptId, AssignDepartment
from ch06_school.data import student as data

def find_all() -> List[StudentResponse]:
    return data.find_all()

def find_by_id(id: int) -> StudentResponse:
    _student = data.find_by_id(id)
    if _student is None:
        raise StudentNotFoundException(id)
    return _student

def assign_student(assign_dto:AssignDepartment) -> StudentResponse:
     # 성적 기준 학과 배정 로직
     assigned = data.assign_student(assign_dto.student_id, assign_dto.dept_id)
     if not assigned:
         raise StudentNotFoundException(assign_dto.student_id)
     return data.find_by_id(assign_dto.student_id)