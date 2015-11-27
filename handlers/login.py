# coding: utf-8
from base.base import BaseHandler


class LoginHandler(BaseHandler):
    def __init__(self, application, request, **kwargs):
        super(LoginHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')

    def get(self, *args, **kwargs):
        if not self.id:
            self.write(
                '<form><input name="id" type="text" placeholder="用户名"><br><input placeholder="密码" name="pwd" type="password"><br><input type="submit"></form>')
        else:
            self.write('成功登陆')

    def post(self, *args, **kwargs):
        id = self.get_argument('id')
        pwd = self.get_argument('pwd')
