# coding: utf-8
from base.base import BaseHandler
from dash import is_loged


class StudentIndex(BaseHandler):
    """学生 dashboard 首页"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            self.render('dashboardIndex.html', id=uid)
        else:
            self.redirect('/404')


class MyHomeworkHandler(BaseHandler):
    """我的所有作业"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            # self.render('')
            pass
        else:
            self.redirect('/404')

class MyMessagesHandler(BaseHandler):
    """所有消息提示"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            pass
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
