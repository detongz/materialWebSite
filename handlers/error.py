# coding: utf-8
from base.base import BaseHandler


class ErrorHandler(BaseHandler):
    """处理未接收到的url地址"""

    def get(self, *args, **kwargs):
        uid = self.get_secure_cookie('id')
        self.render('error.html', title=None, content='<br>404<br><br><br>页面没有找到', icon='ion-sad', active='', id=uid)