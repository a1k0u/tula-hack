import sqlite3
from typing import Dict


def create_db(connect_db, app):
    db = connect_db()
    with app.open_resource('sq_db.sql', 'r') as f:
        db.cursor().executescript(f.read())
    db.commit()
    db.close()


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def make_request_to_sql(self, sql: str) -> list:
        result = []
        try:
            self.__cur.execute(sql)
            result = self.__cur.fetchall()
        except sqlite3.Error:
            assert sqlite3.Error
        return result

    def get_user(self, username: str) -> Dict[str, str]:
        sql = f"SELECT * FROM users WHERE username={username}"
        return self.make_request_to_sql(sql)

    def get_all_users(self) -> list:
        sql = "SELECT * FROM users"
        return self.make_request_to_sql(sql)

    def create_user(self, username: str, password: str) -> None:
        sql = f"INSERT INTO users(username, password) VALUES({username}, {password})"
        try:
            self.__cur.execute(sql)
        except sqlite3.Error:
            assert sqlite3.Error

