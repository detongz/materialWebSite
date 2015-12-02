# coding: utf-8
from base.base import BaseHandler
from models.course import get_teacher_course


class DashBoardHandler(BaseHandler):
    def get(self, *args, **kwargs):
        uid = self.get_secure_cookie('id')
        gp = self.get_secure_cookie('gp')

        if not uid:
            self.redirect('/login')
        elif gp == 's':
            self.render('stu_dash.html', id=uid, active='dsh', active_slide='mycourse')
        elif gp == 't':
            self.render('teacher_index.html', id=uid, active='dsh', active_slide='mycourse',
                        course=get_teacher_course('zmy'))
        else:
            self.redirect('/404')
