from typing import List, Tuple, Dict, Optional, Union


#타입 힌트 사용
def add(a: int, b: int) -> int:
    return a + b

#list 타입 힌트
#1,2,3, 리스트 받아서 2 곱해서 리턴
def process_numbers(numbers: List[int]) -> List[int]:
    return [n*2 for n in numbers]

#Tuple 타입 힌트
#이름, 나이 리턴
def get_person_info() -> Tuple[str, int]:
    return ("NAME", 25)

#딕셔너리 타입 힌트
#이름, 점수 리턴
def get_student_scores() -> Dict[str, float]:
    return {"tlagiswls", 100}

#Optional
def find_user(user_id: int) -> Optional[str]:
    users = {1: "tla", 2: "wjd"}
    return users.get(user_id)

#Union
def whatType(value: Union[str, int]) -> int:
    if isinstance(value, int):
        return value ** 2
    else:
        return len(value)


if __name__ == "__main__":
    print(add(1, 2))
    print(add("1", "2")) #타입 힌트는 강제성이 없는 선택 사항이다
    print(process_numbers([1, 2, 3]))
    print(get_person_info())
    print(get_student_scores())
    print(find_user(1))
    print(find_user(3)) #None
    print(whatType(10))
    print(whatType("10"))