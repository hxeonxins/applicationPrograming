# 쿼리
from ch06_school.data import cur

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