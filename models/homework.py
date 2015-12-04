# coding: utf-8

from models import db
from security import clean

"""作业操作"""


def get_teacher_homeworks(uid):
    """获取教师所有作业"""
    # return db.Course.find({'tid': 'uid'})
    sql = "select * from Homework where cid in (select idCourse from Course where tid='%s')" % (clean(uid))
    return db.query(sql)
