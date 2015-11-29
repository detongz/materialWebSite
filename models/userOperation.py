# coding: utf-8
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.Material


def stuLogin(uid, pwd):
    return db.Student.find_one({}, {'user': uid, 'password': pwd})


def teaLogin(uid, pwd):
    return db.Teacher.find_one({}, {'user': uid, 'password': pwd})


if __name__ == "__main__":
    print(stuLogin('zdt', '11'))
