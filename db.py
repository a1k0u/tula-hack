import sqlite3
import time
import math


class DataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def add_user(self, name, hash_password):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE username LIKE '{name}'")
            res = self.__cur.fetchone()
            if res['count']:
                print("Пользователь с таким username уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, NULL, ?)", (name, hash_password, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Error server :( " + str(e))
            return False
        return True

    def get_user(self, user_id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {user_id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))
        return False

    def get_user_by_name(self, name):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE username = '{name}' LIMIT 1")
            res = self.__cur.fetchone()
            print(res)
            if not res:
                print("Пользователь не найден")
                return False
            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД " + str(e))

        return False
