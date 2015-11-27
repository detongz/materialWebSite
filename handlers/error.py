# coding: utf-8
from base.base import BaseHandler

class ErrorHandler(BaseHandler):
    def get(self, *args, **kwargs):
        self.write('404')