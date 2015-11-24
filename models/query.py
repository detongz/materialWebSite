# coding:utf-8

import torndb
import re

db = torndb.Connection('localhost', 'courseDesign', 'root')
GROUP = {'0': 'student', '1': 'teacher'}


def authenticate(id, pwd, group):
    sql = ''
    if group == 0:
        sql = "SELECT * FROM student where id='" + id + "' and password='" + pwd + "';"
    elif group == 1:
        sql = "SELECT * FROM teacher where id='" + id + "' and password='" + pwd + "';"
    count = db.query(sql)
    if count:
        return 1
    else:
        return 0


def viewStudentInfo(stuid):
    sql = "select * from student where id='" + stuid + "'"
    try:
        return db.query(sql)[0]
    except:
        return None


def getUserName(id, group):
    sql = "SELECT NAME FROM " + GROUP[str(group)] + " WHERE ID = '" + id + "';"
    name = db.query(sql)
    if not name:
        return id
    else:
        return name[0]['NAME']


def getTeachersName():
    sql = "select name from teacher"
    return db.query(sql)


def getStudents():
    sql = "select * from student"
    return db.query(sql)


def getTeachers():
    sql = "select * from teacher"
    return db.query(sql)


def getUserInfo(id, group):
    sql = "select * from " + GROUP[group] + " where id = '" + id + "';"
    return db.query(sql)


def getTeacherInfo(id):
    sql = "select * from teacher where id='" + id + "';"
    return db.query(sql)[0]


def getStudentInfor(id):
    sql = "select * from student where id='" + id + "';"
    return db.query(sql)[0]


def allMyStudents(teacherid):
    sql = '''
        select s.id,s.name,s.email,s.password,s.class,s.course,ifnull(sum(h.isCommented),0) as state
        from homework as h,student as s
        where course in (select idcourse from course where idteacher = "''' + teacherid + '''" and applyState = 1) and h.idstu=s.id
        group by h.idstu,h.idcourse
        union
        select s.id,s.name,s.email,s.password,s.class,s.course,0 as state from student as s;'''
    return db.query(sql)


def addUser(id, name, pwd, email, usr_class, courseId):
    pattern_id = re.compile(r'\b201\d{6}')
    if email != 'null':
        pattern_email = re.compile(r'\b.+@.+\..+$')
    else:
        pattern_email = re.compile(r'null')
    if pattern_id.match(id) is not None:
        if pattern_email.match(email) is not None:
            sql = "insert into student value ('" + id + "','" + name + "','" + email + "','" + pwd + "','" + usr_class + "','" + courseId + "');"
            return db.execute(sql)
        else:
            return "email"
    else:
        return "id"


def changeProfile(id, name, pwd, email, usr_class, courseid):
    # Student!
    pattern_id = re.compile(r'\b201\d{6}')
    if email != 'null':
        pattern_email = re.compile(r'\b.+@.+\..+$')
    else:
        pattern_email = re.compile(r'null')
    if pattern_id.match(id) is not None:
        if pattern_email.match(email) is not None:
            sql = "update student set name='%s',password='%s',email='%s',class='%s',course='%s' where id='%s'" % (
            name, pwd, email, usr_class, courseid, id)
            return db.execute(sql)
        else:
            return "email"
    else:
        return "id"


def teacherSigningUp(id, name, pwd, email):
    sql = "insert into teacher (id,name,email,password) values ('%s','%s','%s','%s');" % (id, name, email, pwd)
    db.execute(sql)

def updateIntorduction(id,content):
    sql='''update teacher set introduction="%s" where id="%s";''' % (content,id)
    db.execute(sql)

def updateTeacherImage(id,filepath):
    sql="update teacher set photo='/static/images/teacher/%s' where id='%s';" %(filepath,id)
    db.execute(sql)

if __name__ == "__main__":
    id = raw_input()
    name=raw_input()
    pwd=raw_input()
    email=raw_input()
    teacherSigningUp(id,name,pwd,email)
