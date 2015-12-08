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


def getTeacher(uid):
    """获取某位教师信息"""
    sql = "select * from Teacher where idTeacher='%s'" % (clean(uid))
    return db.get(sql)


def getStudent(uid):
    """获取某位学生信息"""
    sql = 'select * from Student where idStudent = "%s"' % (clean(uid))
    return db.get(sql)


def getTempUser():
    """获取所有申请教师用户的账号"""
    sql = 'select * from tempuser;'
    return db.query(sql)


def getATempUser(uid):
    """获取某一位临时用户"""
    sql = 'select * from tempuser where id="%s"' % (clean(uid))
    return db.get(sql)


def insertIntoTempUser(id, type, name, pwd):
    """将新申请的用户加入数据库"""
    sql = "insert into tempuser (id,type,name,pwd) values ('%s','%s','%s','%s');" % (
        clean(id), clean(type), clean(name), clean(pwd))
    db.execute(sql)


def authNewUser(id):
    """管理员通过信用户申请"""

    sql = "select * from tempuser where id='%s';" % (clean(id))

    user = db.get(sql)

    name = user['name']
    pwd = user['pwd']
    type = user['type']

    if type == 't':
        sql = "insert into Teacher (idTeacher,name,pwd) values ('%s','%s','%s');" % (clean(id), name, pwd)
        db.execute(sql)
        sql = "delete from tempuser where id='%s';" % (clean(id))
        db.execute(sql)
        return 'success'
    elif type == 's':
        sql = "insert into Student (idStudent,name,pwd) values ('%s','%s','%s');" % (clean(id), name, pwd)
        db.execute(sql)
        sql = "delete from tempuser where id='%s';" % (clean(id))
        db.execute(sql)
        return 'success'
    else:
        return 'fail'


if __name__ == "__main__":
    print(stuLogin('zdt', '11'))
