# coding: utf-8
from base.base import BaseHandler
from models.course import get_teacher_course, get_teacher_course_delete
from dash import is_loged


class CourseEditHandler(BaseHandler):
    """教师编辑课程首页"""

    def get(self):
        gp, uid = is_loged(self)

        if gp == 't':
            self.render('teacher_edit_course.html', id=uid, active='dsh', active_slide='mycourse',
                        course=get_teacher_course(uid), delete=get_teacher_course_delete(uid))
        else:
            self.redirect('/404')


class EditingCertainCourseHandler(BaseHandler):
    """教师编辑特定课程页面"""

    def get(self, cid):
        gp, uid = is_loged(self)
        if gp == 't':
            self.write('haha')  # 测试消息
        else:
            self.redirect('/404')


class DeleteCourseHandler(BaseHandler):
    """教师编辑特定课程页面"""

    def get(self, cid):
        gp, uid = is_loged(self)
        if gp == 't':
            self.write('haha')  # 测试消息
        else:
            self.redirect('/404')


class CommentingHandler(BaseHandler):
    """教师评价作业首页"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.render('teacher_commenting.html', id=uid, active='dsh', active_slide='cmt',
                        course=get_teacher_course(uid))
        else:
            self.redirect('/404')
