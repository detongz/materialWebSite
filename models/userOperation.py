# coding: utf-8
from models import db
from security import clean


def stuLogin(uid, pwd):
    return db.Student.find_one({}, {'user': clean(uid), 'password': clean(pwd)})


def teaLogin(uid, pwd):
    return db.Teacher.find_one({}, {'user': clean(uid), 'password': clean(pwd)})


if __name__ == "__main__":
    print(stuLogin('zdt', '11'))
