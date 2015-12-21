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
    """获取学生参加的课程"""
    sql = 'select * from Course where idCourse in (select cid from Student where idStudent="%s");' % (clean(uid))
    return db.get(sql)


def get_student_homework(uid):
    """获取该学生所有的作业"""

    sql = "select * from Homework where sid='%s';" % (clean(uid))
    return db.query(sql)


def get_all_course():
    """获取全部课程"""

    sql = 'select idCourse,name,state from Course as c,Teacher as t where c.tid=t.idTeacher;'
    return db.query(sql)


def get_course(cid):
    """获取某个课序号的所有信息"""

    sql = "select * from Course where idCourse='%s';" % (clean(cid))
    return db.get(sql)


def set_course(uid, cid):
    """学生录入课序号"""

    sql = "update Student set cid='%s' where idStudent='%s';" % (clean(cid), clean(uid))
    db.execute(sql)


def new_course(tid, idc, year, st, en):
    """教师新增加课程"""

    sql = "insert into Course (idCourse,tid,year,start_week,end_week) " \
          "values ('%s','%s','%s','%s','%s');" \
          % (clean(idc), clean(tid), year, st, en)
    db.execute(sql)


if __name__ == "__main__":
    for i in get_teacher_course('zmy**'):
        print i
