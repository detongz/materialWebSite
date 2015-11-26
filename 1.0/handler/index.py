# coding:utf-8

import tornado.web
from models.queryResourse import getnotification, getresources


class indexHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(indexHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('name')

    def get(self):
        self.render("index.html", id=self.id, res=getresources(), note=getnotification())
