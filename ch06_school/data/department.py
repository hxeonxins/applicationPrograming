# 쿼리
import sqlite3
from typing import List

from fastapi import HTTPException

from ch06_school.data import cur, con
from ch06_school.error import Missing, Duplicate
from ch06_school.model.department import DepartmentResponse, Department

cur.executescript(
    '''
    create table if not EXISTS department (
        id integer primary key autoincrement,
        name text not null unique,
        quota int not null default 0,
        description text
    );
    
    insert or ignore into department (name, quota) values ('sw', 32);
    insert or ignore into department (name, quota) values ('embedded', 32);
    '''
)


# 객체를 만들어 주는 공간. 객체 만들어서 리턴
def row_to_model(entity: tuple) -> List[DepartmentResponse]:
    id, name, quota, description = entity
    return DepartmentResponse(
        id = id,
        name = name,
        quota = quota,
        description = description,
    )

def find_all() -> List[DepartmentResponse]:
    query = "select * from department"
    cur.execute(query)
    return [row_to_model((row)) for row in cur.fetchall()]

def find_by_id(id: int) -> DepartmentResponse:
    query = f"select * from department where id = {id}"
    cur.execute(query)
    row = cur.fetchone()
    if row is None:
        raise Missing(message = f"department with id {id} not found")
    return row_to_model(row)

def save(department: Department) -> DepartmentResponse:
    query = ("insert into department(name, quota, description) "
             "values (:name, :quota, :description)")
    try:
        cur.execute(query, department.model_dump())
        con.commit()
        new_department_id = cur.lastrowid
        find_by_id(new_department_id)
        return find_by_id(new_department_id)
    except sqlite3.IntegrityError as e: # 무결성 에러
        raise Duplicate(message = f"department with name {department.name} already exists")


def delete(id: int) -> bool:
    query = f"delete from department where id = {id}"
    cur.execute(query)
    con.commit()
    if cur.rowcount:
        return True
    raise Missing(message = f"department with id {id} not found")

