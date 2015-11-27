# coding: utf-8
from base.base import BaseHandler


class IndexHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.render('index.html')
