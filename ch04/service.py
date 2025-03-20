#main
from ch04.data.todo import find_all, insert_one
from ch04.models import Todo


if __name__ == '__main__':
    print(find_all())
    insert_one(Todo("study fastapi"))
    print(find_all())