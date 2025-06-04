from pydantic import BaseModel


class LoginUser(BaseModel):
    username: str
    password: str
    admin: bool = False

fake_users = list()
fake_users.append(LoginUser(username="user", password="user"))
fake_users.append(LoginUser(username="admin", password="admin", admin=True))