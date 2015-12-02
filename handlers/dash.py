# coding: utf-8
from base.base import BaseHandler
from models.course import get_teacher_course

'''个人管理(dashboard)界面老师/学生通用函数和方法'''


class DashBoardHandler(BaseHandler):
    """个人管理首页"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            self.render('stu_dash.html', id=uid, active='dsh', active_slide='mycourse')
        elif gp == 't':
            self.render('teacher_index.html', id=uid, active='dsh', active_slide='mycourse',
                        course=get_teacher_course(uid))
        else:
            self.redirect('/404')


def is_loged(request):
    """判断用户是否已经登陆后返回用户名密码"""

    uid = request.get_secure_cookie('id')
    gp = request.get_secure_cookie('gp')

    if not uid:
        request.redirect('/login')
    return gp, uid
