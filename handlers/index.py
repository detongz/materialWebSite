# coding: utf-8
from base.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        self.render('index.html',id=id)
