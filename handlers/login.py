# coding: utf-8
from base.base import BaseHandler


class LoginHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(LoginHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')

    def get(self, *args, **kwargs):
        if not self.id:
            self.render('login.html', id=None)
        else:
            self.write('成功登陆')

    def post(self, *args, **kwargs):
        id = self.get_argument('id')
        pwd = self.get_argument('pwd')
