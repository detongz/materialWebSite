# coding: utf-8
from base.base import BaseHandler
from dash import is_loged


class SignUpHandler(BaseHandler):
    """新用户注册"""
    def prepare(self):
        self.id=self.get_secure_cookie('id')]
        
    def get(self):
        if not self.id:
            self.render('login.html', id=None, active='lgin')
        else:
            self.redirect('/')
    def post(self):
        pass
