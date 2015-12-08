# coding: utf-8
from base.base import BaseHandler
from dash import is_loged
from models.notification import get_all_notif, get_all_comments
from models.homework import get_my_homework


class MyHomeworkHandler(BaseHandler):
    """我的所有作业"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            self.render('stu_homework.html', homework=get_my_homework(uid), id=uid, active='dsh', active_slide='hmwk')
        else:
            self.redirect('/404')


class MyMessagesHandler(BaseHandler):
    """所有消息提示"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            self.render('stu_message.html', id=uid, message=get_all_notif(), comments=get_all_comments(uid),
                        active='dsh', active_slide='msg')
        else:
            self.redirect('/404')


class MyCourseHandler(BaseHandler):
    """我的课程界面"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            pass
        else:
            self.redirect('/404')


class submitAssgnmentHandler(BaseHandler):
    """ 学生提交作业 """
    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            self.render('stu_submitassignment.html',id=uid, active='dsh', active_slide='mcs')
        else:
            self.render('error.html', title=None, content='提交作业要先登陆哦', icon='ion-happy', active='', id=uid)
