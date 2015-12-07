# coding: utf-8
from base.base import BaseHandler
from dash import is_loged
from models.userOperation import getTempUser


class SignUpHandler(BaseHandler):
    """新用户注册"""

    def prepare(self):
        self.id = self.get_secure_cookie('id')

    def get(self):
        if not self.id:
            self.render('login.html', id=None, active='lgin')
        else:
            self.redirect('/')

    def post(self):
        pass


class AdminHandler(BaseHandler):
    """管理员用户界面，认证教师用户"""

    def get(self):
        gp, uid = is_loged(self)
        if uid == str(int(1e6)):
            self.render('admin.html', temp=getTempUser())
        else:
            self.redirect('/404')
