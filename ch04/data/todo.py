#create table
from ch04.data import cur

cur.execute('''
create table if not exists todo(
    task_id integer primary key autoincrement,
    task text not null unique,
    completed integer not null defult 0,
    created_at text not null defult(datetime('now', 'localtime'))
) 
''')