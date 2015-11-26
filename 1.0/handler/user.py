# coding:utf-8
"""
与用户相关的操作
"""

import tornado.web
from models.query import getUserInfo, getStudents, getTeachers, allMyStudents, viewStudentInfo, getTeacherInfo, \
    getStudentInfor, changeProfile, teacherSigningUp, updateIntorduction,updateTeacherImage
from models.getCourse import getCoursesTeacher, getCourseByCourseId, getCourseHistory, getCoursesToBeStated, \
    getCourseById, updateApplyState, updatePeriod, endCourse, startCourse, endCourseForce, myCourse, getAllCoursesId
from models.queryHomework import getMyHomework, getMyCourseHomeworkState
from tornado.escape import json_encode
from handler.resourse import text2Html
import os


class userInfoHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(userInfoHandler, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self):
        if not self.group:
            self.redirect('/login')
        elif self.group == '1':
            course = getMyCourseHomeworkState(self.id)
            self.render('userInfoIndexTeacher.html', user=getTeacherInfo(self.id), id=self.name, course=course)
        else:
            try:
                course = myCourse(self.id)
            except IndexError:
                course = None
            self.render("userInfoIndex.html", user=getStudentInfor(self.id), id=self.name, course=course)


class updateCourseStateHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(updateCourseStateHandler, self).__init__(application, request, **kwargs)
        self.course = {}
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self, courseid):
        if not self.group:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            self.course = getCourseById(courseid)
            self.render('updateCourseState.html', id=self.name, course=self.course)

    def post(self, courseid):
        result = {'setform': '0'}
        signal = self.get_argument('signal')
        self.course = getCourseById(self.get_argument('idcourse'))
        if signal == '1':
            if int(self.course['applyState']) == 1:
                if int(self.course['period']) < int(self.course['max'] - 1):
                    updatePeriod(self.course['idcourse'], 0)
                    result['result'] = 'success'
                    result['setform'] = '1'
                elif int(self.course['period']) == int(self.course['max']) - 1:
                    updatePeriod(self.course['idcourse'], 1)
                    result['result'] = 'success'
                elif int(self.course['period']) == int(self.course['max']):
                    endCourse(self.course['idcourse'])
                    result['result'] = 'success'
                else:
                    result['result'] = 'error'
            else:
                result['result'] = 'error'
        elif signal == '0':
            if int(self.course['applyState']) == 2 and int(self.course['period']) > int(self.course['max']):
                result['result'] = '课程结束，不可更改课程状态'
            elif int(self.course['applyState']) == 0:
                startCourse(self.course['idcourse'])
                result['result'] = 'success'
                result['setform'] = '1'
            elif int(self.course['applyState']) == 1:
                endCourseForce(self.course['idcourse'])
                result['result'] = 'success'
            else:
                updateApplyState(self.course['idcourse'])
                result['result'] = 'success'
        self.write(json_encode(result))


class CourseHistoryHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(CourseHistoryHandler, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            history = getCourseHistory()
            teachers = getTeachers()
            self.render('CourseHistory.html', id=self.name, courses=history, teachers=teachers,
                        user=getTeacherInfo(self.id))


class allStudentsHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(allStudentsHandler, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            students = allMyStudents(self.id)
            self.render('allStudents.html', id=self.name, students=students, user=getTeacherInfo(self.id))


class courseToBeStarted(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(courseToBeStarted, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.group = self.get_secure_cookie('group')
        self.name = self.get_secure_cookie('name')

    def get(self, *args, **kwargs):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            courses = getCoursesToBeStated()
            teachers = getTeachers()
            self.render('courseToBegin.html', id=self.name, course=courses, teachers=teachers,
                        user=getTeacherInfo(self.id))


class viewStudentDetails(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(viewStudentDetails, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self, stuid):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            student = viewStudentInfo(stuid)
            thisUser = getTeacherInfo(self.id)
            homework = getMyHomework(stuid)
            course = myCourse(stuid)
            self.render('viewStudentDetail.html', id=self.name, user=thisUser, stu=student, course=course,
                        homework=homework)


class changeProfileHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(changeProfileHandler, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self, *args, **kwargs):
        if not self.id:
            self.redirect('/login')
        elif self.group != '0':
            self.redirect('/')
        else:
            self.render('changeprofile.html', idstu=self.id, autumn=getAllCoursesId(1), spring=getAllCoursesId(2),
                        summer=getAllCoursesId(3))

    def post(self, *args, **kwargs):
        result = {}
        user_id = self.get_argument('id')
        name = self.get_argument('name')
        pwd = self.get_argument('pwd')
        email = self.get_argument('email')
        user_class = self.get_argument('class')
        course = self.get_argument('course')
        time = self.get_argument('time')

        if course == "":
            course = "null"
        else:
            course = getCourseByCourseId(time, course)['idcourse']
        if email == "":
            email = 'null'
        if user_class == "":
            user_class = "null"

        if getUserInfo(user_id, '0'):
            flag = changeProfile(user_id, name, pwd, email, user_class, course)
            if flag == "id":
                result['result'] = "学号格式错误"
            elif flag == "email":
                result['result'] = "邮箱格式错误"
            else:
                result['result'] = "success"
        else:
            result['result'] = "用户不存在！"
        self.write(json_encode(result))


class teacherSetting(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        if self.get_secure_cookie('id') is not None:
            self.redirect('/')
        else:
            self.render('teachersetting.html')

    def post(self, *args, **kwargs):
        import re

        result = {}

        id = self.get_argument('id')
        name = self.get_argument('name')
        email = self.get_argument('email')
        pwd = self.get_argument('pwd')

        pattern_email = re.compile(r'\b.+@.+\..+$')
        pattern_id = re.compile(r'\b\d{9}')
        if not pattern_id.match(id):
            print id
            result['result'] = '教职工号输入错误'
        else:
            if pattern_email.match(email) is not None:
                try:
                    teacherSigningUp(id, name, pwd, email)
                    result['result'] = 'success'
                except:
                    result['result'] = '该教职工号已经被注册过'
            else:
                result['result'] = '用户邮箱填写错误！'
        self.write(json_encode(result))


class teacherSetPic(tornado.web.RequestHandler):
    def get(self, idteacher, *args, **kwargs):
        self.id = self.get_secure_cookie('id')
        group = self.get_secure_cookie('group')
        if group == '0':
            self.redirect('/')
        self.render('teacherSetPicture.html', id=self.id, idteacher=idteacher)

    def post(self, idteacher, *args, **kwargs):
        path = os.path.dirname(__file__)[:-8] + '/static/images/teacher/'
        extention = self.request.files['file'][0].filename.split('.')[-1]
        filename = idteacher + '.' + extention
        try:
            f = open(os.path.join(path, filename), "w")
            f.write(self.request.files['file'][0].body)
            f.close()
            updateTeacherImage(idteacher,filename)
        except:
            pass

        self.redirect('/courseInfo/teacher/' + idteacher)


class teacherSetIntorduction(tornado.web.RequestHandler):
    def get(self, idteacher, *args, **kwargs):
        self.id = self.get_secure_cookie('id')
        group = self.get_secure_cookie('group')
        if group == '0':
            self.redirect('/')
        self.render('teacherSetIntorduction.html', id=self.id, idteacher=idteacher)

    def post(self, idteacher):
        content = self.get_argument('contents')
        content = text2Html(content)
        updateIntorduction(idteacher, content)
        self.redirect('/courseInfo/teacher/' + idteacher)
