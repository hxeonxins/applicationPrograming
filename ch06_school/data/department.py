# 쿼리
from typing import List

from ch06_school.data import cur
from ch06_school.model.department import DepartmentResponse

cur.executescript(
    '''
    create table if not EXISTS department (
        id int primary key auto_increment,
        name text not null unique ,
        quota int not null default 0,
        description text
    );
    
    insert or ignore into department (name, quota) values ('sw', 32);
    insert or ignore into department (name, quota) values ('embedded', 32);
    '''
)


# 객체를 만듩어 주는 공간. 함수 ㅏ그래도 객체 만들어서 리턴
def row_to_model(entity: tuple) -> List[DepartmentResponse]:
    id, name, quota, descripstion = entity
    return DepartmentResponse(
        id = id,
        name = name,
        quota = quota,
        description = descripstion,
    )

def find_all() -> List[DepartmentResponse]:
    query = "select * from department"
    cur.execute(query)
    return {row_to_model((row)) for row in cur.fetchall()}