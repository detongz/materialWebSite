# coding: utf-8

from models import db
from security import clean

"""对学生操作"""


def get_my_student(uid):
    """获取老师的所有学生"""
    sql = 'select * from Student where cid in (select idCourse from Course where tid="%s");' % (clean(uid))
    return db.query(sql)
