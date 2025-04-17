from typing import List

from ch06_school.data import cur
from ch06_school.model.department import DepartmentResponse, DepartmentOptionalResponse
from ch06_school.model.student import StudentResponse

cur.executescript(
    '''
    create table if not EXISTS student(
        id int primary key auto_increment,
        name text not null,
        score real not null default 0,,
        department_id integer,
        foreign key (department_id) references department(id)
    );

    insert or ignore into student (id, name, score, department_id) values (2000, 'shj', 98.7);
    insert or ignore into student (id, name, score) values (2001, 'sim', 99.8);
    '''
)

# 객체 만들어서 리컨
def row_to_model(entity: tuple) -> StudentResponse:
    id, name, score, dept_id, dept_name, dept_quota, dept_description = entity

    return StudentResponse(
        id = id,
        name = name,
        score = score,
        department = DepartmentOptionalResponse(
            id = dept_id,
            name = dept_name,
            quota = dept_quota,
            description = dept_description
        )
    )

def find_all() -> List[StudentResponse]:
    query = ("select s.id, s.name, s.score, d.id, d.name, d.quota, d.description "
            "from student s left join department d on s.department_id = d.id")
    cur.execute(query)
    return [row_to_model(row) for row in cur.fetchall()]

def find_by_id(id: int) -> StudentResponse:
    query = ("select s.id, s.name, s.score, d.id, d.name, d.quota "
             "from student s left join department d on s.department_id = d.id"
             f"where s.id={id}")
    cur.execute(query)
    row = cur.fetchone()
    if row is None:
        return None
    return row_to_model(row)