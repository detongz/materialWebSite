# coding: utf-8
from base.base import BaseHandler


class ErrorHandler(BaseHandler):
    """处理未接收到的url地址"""
    def get(self, *args, **kwargs):
        self.write('404')
