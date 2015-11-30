# coding: utf-8
from base.base import BaseHandler


class StudentIndex(BaseHandler):
    def get(self, *args, **kwargs):
        uid = self.get_secure_cookie('id')
        if not uid:
            self.redirect('/login')
        else:
            self.render('dashboardIndex.html', id=uid)
