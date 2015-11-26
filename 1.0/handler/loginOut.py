# coding:utf-8

import tornado.web
from models.query import *
from tornado.escape import json_encode


class loginHandler(tornado.web.RequestHandler):
    def get(self):
        if self.get_secure_cookie('id'):
            self.redirect('/')
            return
        self.render("login.html")

    def post(self):
        # 获取ajax post
        id = self.get_argument('id')
        pwd = self.get_argument('pwd')
        group = 0
        if (self.get_argument('group')).encode("utf-8") == "教师":
            group = 1
        # 设置cookie
        name = getUserName(id, group)
        self.set_secure_cookie('name', name)
        self.set_secure_cookie('id', id)
        self.set_secure_cookie('group', str(group))
        # 响应ajax
        result = {}
        if authenticate(id, pwd, group) == 1:
            result['result'] = "success"
        else:
            result['result'] = '用户不存在,请注意用户类型'
        self.write(json_encode(result))


class logoutHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.clear_cookie('name')
        self.clear_cookie('id')
        self.clear_cookie('group')
        self.redirect("/")
