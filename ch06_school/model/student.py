from typing import Optional

from pydantic import BaseModel

from ch06_school.model.department import DepartmentResponse, DepartmentOptionalResponse


# 생성 시 활용되는 DTO
class Student(BaseModel):
    name: str
    score: float


# 응답 시 활용되는 DTO
class StudentResponse(Student):
    id: int
    department: DepartmentOptionalResponse # 객체지향 스러운 코드!
    # dept_id: int # 객체 지향 스럽지 않음

# 학과 배정을 위한 DTO
class AssignDepartment(BaseModel):
    student_id: int
    dept_id: int

class RequestDeptId(BaseModel):
    dept_id: int