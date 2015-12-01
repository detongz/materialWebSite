# coding: utf-8

from .userOperation import db


def getmycourse():
    return db.Course.find({}, {'tid': 'zmy'})


if __name__ == "__main__":
    print(getmycourse())
