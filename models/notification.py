# coding: utf-8

from models import db
from security import clean

"""对学生操作"""


def get_teacher_notif(uid):
    """获取教师发布的所有信息"""
    sql = 'select * from Info where tid = "%s";' % (clean(uid))
    return db.query(sql)


def get_all_notif():
    """获取所有老师发布的所有消息"""
    sql='''select I.idInfo,I.t‎itle,I.date,I.type,T.name,I.tid from Teacher as T,Info as I where T.idTeacher=I.tid'''
    return db.query(sql)


def get_all_comments(stu):
    """获取教师的所有评语"""
    sql="select comment,date,tag,type,idHomework from Homework where comment!='' and sid='%s' order by date desc;" % (clean(stu))
    return db.query(sql)
