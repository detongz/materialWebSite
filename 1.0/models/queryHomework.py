# coding:utf-8
from query import db


def getrandom():
    import random
    return random.randint(0, 1e4)


def getHomeworkOfPeriod(idstu, period):
    sql = "select * " \
          "from homework " \
          "where idcourse=(select course from student where id = '" + idstu + "') and courseP = '" + period + \
          "' and idstu = '" + idstu + "'"
    try:
        return db.query(sql)[0]
    except:
        return None


def commentingHomework(period, stuId, comment):
    sql = "update homework " \
          "set isCommented=0, comment='" + comment + "' " \
                                                     "where idstu = '" + stuId + "' and courseP='" + period + "'"
    return db.execute(sql)


def homeworkUpload(idstu, period, idcourse):
    rand = getrandom()
    sql = "select homeworkid from homework where idstu = '" + idstu + "' and courseP='" + period + "'"
    homeworkid = db.query(sql)
    if not homeworkid:
        sql = "insert into homework " \
              "values ('%s','%s','%s',null,'%s',1,null);" \
              % (rand, idstu, idcourse, period)
        db.execute(sql)


def vedioUpload(idstu, period, idcourse, link):
    rand = getrandom()
    sql = "select homeworkid from homework where idstu = '" + idstu + "' and courseP='" + period + "'"
    homeworkid = db.query(sql)
    if homeworkid is not None:
        sql = "delete from homework where idstu = '" + idstu + "' and courseP='" + period + "'"
        db.execute(sql)

    sql = "insert into homework " \
          "values ('%s','%s','%s',null,'%s',1,'%s');" \
          % (rand, idstu, idcourse, period, link)
    db.execute(sql)


def getMyHomework(stuNum):
    sql = "select courseP,homeworkid,comment,homeworkid,isCommented,link " \
          "from homework " \
          "where idcourse=(select course from student where id = '" + stuNum + "') and idstu='" + stuNum + "'" \
                                                                                                           "order by courseP"
    try:
        return db.query(sql)
    except IndexError:
        return None


def finalCommenting(stuNum, comment):
    sql = "insert into score (id_stu,finalComment) values ('" + stuNum + "','" + comment + "')"
    db.query(sql)


def finalScoreing(stuNum, comment, score):
    sql = "replace into score values ('" + stuNum + "','" + score + "','" + comment + "')"
    db.query(sql)


def getMyCourseHomeworkState(idteacher):
    sql = '''
            select * from (select * from course where idteacher="%s") as a
            left join
            (select sum(homework.isCommented) as state, homework.idcourse as cid from homework
            where
                homework.idcourse in (select idcourse from course where idteacher="%s")
            group by homework.idcourse) as summing on summing.cid=a.idcourse;''' % (idteacher, idteacher)
    return db.query(sql)


def getAllPeriods(idcourse):
    sql = 'select * from periods where idcourse="' + idcourse + '" order by period;'
    return db.query(sql)


def getMyCourse(idstu):
    sql = "select course from student where id='" + idstu + "'"
    return db.get(sql)['course']


def getAssgnmentType(idcourse, period):
    sql = 'select type from periods where idcourse="' + idcourse + '" and period="' + period + '"'
    print sql
    return db.get(sql)['type']


def getHomeworkVideoLink(stuid, period):
    sql = "select link from homework where idstu='%s' and courseP='%s';" % (stuid, period)
    try:
        return db.get(sql)['link']
    except TypeError:
        return None


if __name__ == "__main__":
    stu = raw_input()
    period = raw_input()
    print getAssgnmentType(stu, period)
