from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class User(BaseModel):
    id: int
    name: str
    age: int
    email: str

class Product(BaseModel):
    name: str = Field(..., min_length=4, max_length=10)
    price: float = Field(..., gt = 10.0, le=100)
    stock: Optional[int] = 10


class Event(BaseModel):
    name: str
    start_type: datetime

class Admin(User):
    role: str="admin"

if __name__ == "__main__":
    user = User(id=1, name="choi", age=25, email="teacher009@bssm.hs.kr")
    user2 = User(id="2", name="jung", age=43, email="teacher099@bssm.hs.kr")
    print(user)
    print(user2)

    p1 = Product(name = "맥북프로", price = 99.9)
    print(p1)

    e1 = Event(name="Algorithm", start_type="2025-06-25")
    print(e1)

    admin = Admin(id=3, name="teachmon", age=123, email="teacher999@bssm.hs.kr")
    print(admin)