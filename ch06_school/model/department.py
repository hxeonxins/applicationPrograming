from typing import Optional

from pydantic import BaseModel

class Department(BaseModel):
    name: str
    quota: int = 0
    description: Optional[str] = None


class DepartmentResponse(Department):
    id: int


class DepartmentOptionalResponse(Department):
    id: Optional[int]
    name: Optional[str]
    quota: Optional[int] = 0
    description: Optional[str] = None
