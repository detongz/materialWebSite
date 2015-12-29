# coding: utf-8
from base.base import BaseHandler


class CourseDetailHandler(BaseHandler):
    """课程详情"""

    def get(self):
        id = self.get_secure_cookie('id')
        self.render('courseInfo.html', id=id, active='det')
