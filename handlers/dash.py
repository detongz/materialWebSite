# coding: utf-8
from base.base import BaseHandler


class DashBoardHandler(BaseHandler):
    def get(self, *args, **kwargs):
        uid = self.get_secure_cookie('id')
        gp = self.get_secure_cookie('gp')

        if not uid:
            self.redirect('/login')
        elif gp == 's':
            self.render('stu_dash.html', id=uid, active='dsh')
        elif gp == 't':
            self.render('teacher_dash.html', id=uid, active='dsh')
        else:
            self.redirect('/404')
