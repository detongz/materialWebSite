# coding: utf-8
from models import db
from security import clean

"""用户操作"""


def stuLogin(uid, pwd):
    """学生登陆"""
    # return db.Student.find_one({}, {'user': clean(uid), 'password': clean(pwd)})
    sql = 'select * from Student where idStudent="%s" and pwd="%s"' % (clean(uid), clean(pwd))
    return db.get(sql)


def teaLogin(uid, pwd):
    """教师登陆"""
    # return db.Teacher.find_one({}, {'user': clean(uid), 'password': clean(pwd)})
    sql = 'select * from Teacher where idTeacher="%s" and pwd="%s"' % (clean(uid), clean(pwd))
    return db.get(sql)


def getTempUser():
    '''获取所有申请教师用户的老师账号'''
    sql = 'select * from tempuser;'
    return db.query(sql)


if __name__ == "__main__":
    print(stuLogin('zdt', '11'))
