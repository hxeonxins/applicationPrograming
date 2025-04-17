#예외 처리
#None 이라고 알려주기
#단건 조회 시 예외 발생
from fastapi import HTTPException
from fastapi.openapi.utils import status_code_ranges
from starlette import status


#exception 상속 받아서 직접 만들수도 있음
class Missing(Exception):
    def __init__(self, message):
        super.__init__(self, message)
        self.message = message

#중복 에러 처리
class Duplicate(Exception):
    def __init__(self, message):
        super.__init__(self, message)
        self.message = message

# 에외 처리 루트 익셉션
class SchoolException(Exception):
    def __init__(self, message:str, status_code:int = status.HTTP_400_BAD_REQUEST):
        self.message = message
        self.status_code = status_code

# not found exception
class StudentNotFoundException(SchoolException):
    def __init__(self, student_id:int):
        super.__init__(
            message = f'학생 {student_id}을 찾을 수 없습니다.',
            status_code = status.HTTP_404_NOT_FOUND
        )