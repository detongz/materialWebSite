# coding: utf-8

from models import db
from security import clean

"""对学生操作"""


def get_teacher_notif(uid):
    """获取教师发布的所有信息"""
    sql = 'select * from Info where tid = "%s";' % (clean(uid))
    return db.query(sql)
