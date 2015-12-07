# coding: utf-8

from models import db
from security import clean


"""课程操作"""


def get_teacher_course(uid):
    """获取该教师所有的课程"""
    # return db.Course.find({'tid': clean(uid)})
    sql = 'select * from Course where tid= "%s";' % (clean(uid))
    return db.query(sql)


def get_teacher_course_delete(uid):
    """获取教师可以删除的(不在开课状态的)课程"""
    # return db.Course.find({'tid': clean(uid), 'period': 0})
    sql = 'select * from Course where tid="%s" and state=0 ' % (clean(uid))
    return db.query(sql)


def get_student_course(uid):
    """获取学生所有的课程"""
    sql='select * from Course where idCourse in (select cid from Student where idStudent="%s");' % (clean(uid))
    return db.query(sql)


def get_student_homework(uid):
    """获取该学生所有的作业"""
    sql="select * from Homework where sid='%s';" % (clean(uid))
    return db.query(sql)

if __name__ == "__main__":
    for i in get_teacher_course('zmy**'):
        print i
