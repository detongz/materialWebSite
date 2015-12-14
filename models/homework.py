# coding: utf-8

from models import db
from security import clean, cleanLink, text2Html

import sys

reload(sys)
sys.setdefaultencoding('utf-8')

"""作业操作"""


def get_teacher_homework(uid):
    """获取教师所有作业"""

    # return db.Course.find({'tid': 'uid'})
    sql = """
            select Homework.cid,name,type,date,comment,idHomework,tag from Homework,Student
            where Homework.cid in (select idCourse from Course where tid='%s') and Student.idStudent = Homework.sid
            order by date desc;
            """ \
          % (clean(uid))
    return db.query(sql)


def get_my_homework(uid):
    """获取学生提交的所有作业"""

    sql = 'select * from Homework where sid="%s";' % (clean(uid))
    return db.query(sql)


def submit_homework(idHomework, sid, content, tag):
    """学生提交作业 三视图"""

    sql = "insert into Homework " \
          "(idHomework,cid,sid,content,tag) " \
          "values " \
          "('%s'," \
          "(select cid from Student where idStudent='%s')," \
          "'%s'," \
          "'%s'," \
          "'%s')" % (clean(idHomework), clean(sid), clean(sid), cleanLink(content), clean(tag))
    return db.execute(sql)


def submit_homework_vedio(idHomework, sid, content, tag):
    """学生提交作业 视频"""

    sql = "insert into Homework (idHomework,cid,sid,content,tag,type) values " \
          "('%s',(select cid from Student where idStudent='%s'),'%s','%s','%s','video')" \
          % (clean(idHomework), clean(sid), clean(sid), cleanLink(content), clean(tag))
    return db.execute(sql)


def get_homework(hid):
    """根据作业id，获取某次作业"""

    sql = "select * from Homework where idHomework='%s';" % (clean(hid))
    return db.get(sql)


def update_comment(hid, comment):
    """添加/修改作业的评语"""

    sql = 'update Homework set comment="%s" where idHomework="%s";' % (text2Html(comment), clean(hid))
    return db.execute(sql)
