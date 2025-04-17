from typing import List

from joblib.testing import raises

from ch06_school import service
from ch06_school.error import StudentNotFoundException
from ch06_school.model.student import StudentResponse
from ch06_school.data import student as data

def find_all() -> List[StudentResponse]:
    return data.find_all()

def find_by_id(id: int) -> StudentResponse:
    _student = find_by_id(id)
    if _student is None:
        raise StudentNotFoundException(id)
    return _student