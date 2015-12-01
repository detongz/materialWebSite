# coding: utf-8

from models import db
from security import clean


def get_teacher_course(uid):
    return db.Course.find({'tid': clean(uid)})


if __name__ == "__main__":
    for i in get_teacher_course('zmy**'):
        print i
