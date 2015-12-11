# coding: utf-8

from models import db
from security import clean, text2Html
from userOperation import getTeacher

"""对学生操作"""


def get_teacher_notif(uid):
    """获取教师发布的所有信息"""

    sql = 'select * from Info where tid = "%s";' % (clean(uid))
    return db.query(sql)


def get_all_notif():
    """获取所有老师发布的所有消息"""

    sql = '''
            select I.idInfo,I.t‎itle,I.date,I.type,T.name,I.tid
            from Teacher as T,Info as I
            where T.idTeacher=I.tid
            '''
    return db.query(sql)


def get_all_comments(stu):
    """获取教师的所有评语"""

    sql = "select comment,date,tag,type,idHomework " \
          "from Homework " \
          "where comment!='' and sid='%s' " \
          "order by date desc;" \
          % (clean(stu))

    return db.query(sql)


def get_info_by_infoid(Iid):
    """使用信息id号查找消息"""

    sql = "select * from Info where idInfo='%s';" % (clean(Iid))
    return db.get(sql)


def publish_notif(tid, idInfo, detail, title):
    """教师发布课程 通知 """

    if not getTeacher(tid):
        return 't nt exist'

    # 需要加入判断内容长度的部分，防止内容转换后过长
    detail = text2Html(detail)
    title = clean(title)

    sql = "insert into Info (tid,idInfo,detail,title) values ('%s','%s','%s','%s');" \
          % (clean(tid), clean(idInfo), detail, title);


def publish_res(tid, idInfo, detail, title):
    """教师发布课程 资源"""

    if not getTeacher(tid):
        return 't nt exist'

    # 需要加入判断内容长度的部分，防止内容转换后过长
    detail = text2Html(detail)
    title = clean(title)

    sql = "insert into Info (type,tid,idInfo,detail,title) values ('res','%s','%s','%s','%s');" \
          % (clean(tid), clean(idInfo), detail, title);
