#예외 처리
#None 이라고 알려주기
#단건 조회 시 예외 발생
from fastapi import HTTPException
from fastapi.openapi.utils import status_code_ranges


#exception 상속 받아서 직접 만들수도 있음
class Missing(Exception):
    def __init__(self, message):
        super.__init__(self, message)
        self.message = message
#
# def get_one(task: str):
#     if task != 'task1':
#         #exception!!
#         raise Missing(message = f'task {task} is not exist')
#
# def web():
#     #try-catch
#     try:
#         result = get_one("todo")
#     except Missing as e:
#         raise HTTPException(status_code=404, detail=e.message)
#
# if __name__ == '__main__':
#     web()