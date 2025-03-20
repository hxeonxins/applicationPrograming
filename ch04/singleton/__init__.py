#연결 방법 바꾸기
import sqlite3


class DBConnect:
    _instance = None #static으로 관리
    def __new__(cls):
        if cls._instance is None:
            print("produce instance")
            cls._instance = super().__new__(cls)
            cls._instance.con = sqlite3.connect("mydb.db")

        return cls._instance
    def get_connection(self):
        return self.con

# db1 = DBConnect()
# db2 = DBConnect()
# db3 = DBConnect() ->클래스에서 객체 생성을 하나만 함. 4개 만들어도 한개만 넘어감
db = DBConnect()
db.get_connection()