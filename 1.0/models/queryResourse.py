# coding:utf-8
from query import db
from queryHomework import getrandom


def publishingInformation(idteacher, title, infotype):
    import datetime
    t = datetime.datetime.now()
    random = getrandom()
    while True:
        sql = '''select * from resource where idartical='%s';''' % (random)
        if not db.query(sql):
            break
        random = getrandom()

    sql = '''insert into resource values ('%s','%s','%s','%s','%s');''' % (
    random, idteacher, t.strftime('%Y-%m-%d %H:%M:%S'), infotype, title)
    db.execute(sql)
    return random


def getresources():
    sql = 'select * from resource where infoType="resource";'
    return db.query(sql)


def getnotification():
    sql = 'select * from resource where infoType="notification";'
    return db.query(sql)

def getInfoDetail(id):
    sql='select * from resource where idartical="'+id+'";'
    try:
        return db.query(sql)[0]
    except IndexError:
        return None


if __name__=="__main__":
    id=raw_input()
    print getInfoDetail(id)
