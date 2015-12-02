# coding: utf-8
from base.base import BaseHandler


class IndexHandler(BaseHandler):
    """首页"""

    def get(self, *args, **kwargs):
        id = self.get_secure_cookie('id')
        self.render('index.html', id=id, active='ind')
