# coding: utf-8
import tornado.web
from tornado.escape import json_encode
from models.getCourse import getCourseByCourseId, getAllCoursesId
from models.query import addUser, getUserInfo


class signUpHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(signUpHandler, self).__init__(application, request, **kwargs)
        self.user = self.get_secure_cookie('id')

    def get(self):
        if not self.user:
            self.render('signup.html', group=0, autumn=getAllCoursesId(1), spring=getAllCoursesId(2),
                        summer=getAllCoursesId(3))
        else:
            self.redirect('/')

    def post(self):
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

        if not getUserInfo(user_id, '0'):
            flag = addUser(user_id, name, pwd, email, user_class, course)
            if flag == "id":
                result['result'] = "学号格式错误"
            elif flag == "email":
                result['result'] = "邮箱格式错误"
            else:
                result['result'] = "success"
        else:
            result['result'] = "用户已存在"
        self.write(json_encode(result))


class signUpHandlerTeacher(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(signUpHandlerTeacher, self).__init__(application, request, **kwargs)
        self.user = self.get_secure_cookie('id')

    def get(self):
        if not self.user:
            self.render('signup.html', group=1, autumn=None, spring=None, summer=None)
        else:
            self.redirect('/')
