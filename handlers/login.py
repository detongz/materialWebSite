# coding: utf-8
from base.base import BaseHandler
from models.userOperation import stuLogin, teaLogin


class LoginHandler(BaseHandler):
    """ 用户登陆"""

    def __init__(self, application, request, **kwargs):
        super(LoginHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')

    def get(self, *args, **kwargs):
        if not self.id:
            self.render('login.html', id=None, active='lgin')
        else:
            self.redirect('/')

    def post(self, *args, **kwargs):
        id = self.get_argument('id')
        pwd = self.get_argument('password')
        ugroup = self.get_argument('ug')

        if ugroup == 'student':
            stu = stuLogin(id, pwd)
            if not stu:
                self.render('error.html', content='用户不存在', active='lgin', title=None, id=None, icon='ion-ios-close')
            else:
                self.set_secure_cookie('id', id)
                self.set_secure_cookie('gp', 's')
                self.redirect('/login')
        elif ugroup == 'teacher' or ugroup == 't':
            tea = teaLogin(id, pwd)
            if not tea:
                self.render('error.html', content='用户不存在', active='lgin', title=None, id=None, icon='ion-ios-close')
            else:
                self.set_secure_cookie('id', id)
                self.set_secure_cookie('gp', 't')
                self.redirect('/login')


class LogoutHandler(BaseHandler):
    """登陆用户注销"""

    def get(self, *args, **kwargs):
        self.clear_cookie('id')
        self.clear_cookie('gp')
        self.redirect('/')

    def post(self, *args, **kwargs):
        self.clear_cookie('id')
        self.clear_cookie('gp')
        self.redirect('/')
