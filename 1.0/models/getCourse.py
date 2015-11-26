# coding:utf-8

import time
from query import db

terms = {'autumn': '1', 'spring': '2', 'summer': '3'}
forms = {'1': 'pic', '2': 'video'}


def getAcademicYear():
    tm = time.localtime()
    year, month = tm[0], tm[1]
    if int(month) < 8:
        year = int(year) - 1
    return year


def getCoursesTeacher(id):
    sql = "SELECT * FROM course where idteacher='" + id + "';"
    return db.query(sql)


def getCourseById(courseid):
    sql = "select * from course where idcourse ='" + courseid + "';"
    return db.query(sql)[0]


def getCourse(term, courseNum):
    year = getAcademicYear()
    if 0 < int(courseNum) < 99:
        if int(courseNum) < 10:
            sql = "SELECT count(*) as count FROM course where idcourse regexp '" + str(year) + "-" \
                  + terms[term] + "-\\\d{2}-" + courseNum + "';"
            print sql
            return db.query(sql)[0]


def getCourseByCourseId(term, courseNum, year=getAcademicYear()):
    term = str(int(term))
    if 0 < int(courseNum) < 99:
        if int(courseNum) < 10:
            courseNum = str('0') + str(int(courseNum))
        sql = 'select idcourse from course where idcourse like "' + str(year) + '-' + term + '-%%-' + courseNum + '";'
        return db.query(sql)[0]


def getCourseHistory():
    year = getAcademicYear()
    sql = "select * from course where idcourse not regexp('" + str(year) + "');"
    return db.query(sql)


def getCoursesToBeStated():
    sql = "select * from course where applyState != 2 and period=-1;"
    return db.query(sql)


def createCourse(year, term, start_week, course_num, id, max):
    sql = "insert into course values ('" + year + "-" \
          + terms[term] + "-" + start_week + "-" + course_num + "','" + id + "',-1,-1," + max + ");"
    return db.execute(sql)


def updateApplyState(idcourse):
    sql = "update course" \
          " set applyState=applyState+1 " \
          "where idcourse='" + idcourse + "';"
    return db.execute(sql)


def updatePeriod(idcourse,stopCreateing):
    sql = "update course " \
          "set period=period+1 " \
          "where idcourse='" + idcourse + "';"
    db.execute(sql)
    sql = "select * from periods where idcourse='" + idcourse + "' and period=1+(select period from course where idcourse='" + idcourse + "')"
    if not db.query(sql) and stopCreateing==0:
        sql = "insert into periods (idcourse,period,type) values ('" + idcourse + "',(select period from course where idcourse='" + idcourse + "')+1,'pic');"
        db.execute(sql)
    return 0


def startCourse(idcourse):
    sql = "update course " \
          "set applyState=1,period=0 " \
          "where idcourse='" + idcourse + "';"
    db.execute(sql)
    sql = "select * from periods where idcourse='" + idcourse + "' and period='1'"
    if not db.query(sql):
        sql = "insert into periods (idcourse,period,type) values ('" + idcourse + "',(select period from course where idcourse='" + idcourse + "')+1,'pic');"
        db.execute(sql)
    return 0


def endCourse(idcourse):
    sql = "update course " \
          "set applyState=2,period=max " \
          "where idcourse='" + idcourse + "';"
    return db.execute(sql)


def endCourseForce(idcourse):
    sql = "update course " \
          "set applyState=2,period=-1 " \
          "where idcourse='" + idcourse + "';"
    return db.execute(sql)


def myCourse(stuNum):
    sql = '''select * from course where idcourse = (select course from student where id = "''' + stuNum + '''");'''
    return db.query(sql)[0]


def getCourseState(stuNum):
    sql = "select applyState,period,max,idcourse " \
          "from course " \
          "where idcourse=(select course from student where id = '" + stuNum + "')"
    return db.query(sql)[0]


def setPeriodForm(idcourse, period, form):
    sql = '''update periods set type="%s" where idcourse='%s' and period="%s";''' % (forms[form], idcourse, period)
    print sql
    return db.execute(sql)


def getPeriodsOfForm(idcourse, period):
    sql = "select type from periods where period='%s' and idcourse='%s';" % (period, idcourse)
    return db.query()[0]


def getAllCoursesId(term):
    sql = "select idcourse from course where idcourse like '" + str(getAcademicYear()) + "-" + str(term) + "-%%';"
    return db.query(sql)




if __name__ == "__main__":
    stuid=raw_input()
    period=raw_input()
    print getCourse(stuid,period)
