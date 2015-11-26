# coding:utf-8

import tornado.web
from models.query import *
from models.getCourse import getAcademicYear, createCourse, getCourse
from tornado.escape import json_encode


class courseInfoHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(courseInfoHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('name')

    def get(self, *args, **kwargs):
        self.render('courseInfoIndex.html', id=self.id)


class teacherIntorduction(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(teacherIntorduction, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('name')

    def get(self, idteacher):
        result = getTeacherInfo(idteacher)
        self.render('teacherInfo.html', info=result, id=self.id)


class courseinfoTeachersHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        teacher = getTeachers()
        self.id = self.get_secure_cookie('name')
        self.render('courseInfoTeacher.html', id=self.id, teachers=teacher)


class createCourseHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(createCourseHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie("id")
        self.group = self.get_secure_cookie('group')

    def get(self):
        if not self.id:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            self.render('createCourse.html', year=getAcademicYear())

    def post(self):
        result = {}
        academicYear = self.get_argument('year')
        term = self.get_argument('term')
        course_num = self.get_argument('course_num')
        start_week = self.get_argument('start_week')
        max = self.get_argument('max')

        start_week = '0' + str(int(start_week))
        if int(course_num < 10):
            course_num = '0' + str(int(course_num))

        if academicYear >= getAcademicYear():
            # try:
            if 20 > int(start_week) > 0:
                if getCourse(term, course_num) is not None:
                    result['result'] = '课程号已存在'
                else:
                    print term
                    createCourse(academicYear, term, start_week, course_num, self.id, max)
                    result['result'] = 'success'
            else:
                result['result'] = '请重新输入周数'
            # except ValueError:
            #     print
            #     result['result'] = "请输入数字"
        else:
            result['result'] = "年份错误"
        self.write(json_encode(result))
