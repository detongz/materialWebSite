# coding:utf-8
import os

import tornado.web
from tornado.escape import json_encode
from models.query import getUserInfo, viewStudentInfo, getStudentInfor
from models.getCourse import getCourseState, myCourse, getCourseById, setPeriodForm
from models.queryHomework import homeworkUpload, getMyHomework, commentingHomework, finalScoreing, finalCommenting, \
    getMyCourse, getAllPeriods, getAssgnmentType, vedioUpload, getHomeworkVideoLink


class myHomework(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(myHomework, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.group = self.get_secure_cookie('group')
        self.name = self.get_secure_cookie('name')

    def get(self):
        if self.group != '0':
            self.redirect('/')
        else:
            try:
                homework = getMyHomework(self.id)
                courseState = getCourseState(self.id)
            except IndexError:
                homework = courseState = None
            self.render('studentHomework.html', user=getStudentInfor(self.id), id=self.name, homework=homework,
                        course=courseState)


class uploadHomework(tornado.web.RequestHandler):
    # 渲染学生上传文件页面
    def __init__(self, application, request, **kwargs):
        super(uploadHomework, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.group = self.get_secure_cookie('group')
        self.name = self.get_secure_cookie('name')

    def get(self, period):
        course = myCourse(self.id)
        if self.group != '0':
            self.redirect('/')
        else:
            self.render("homeworkUpdate.html", user=getStudentInfor(self.id), id=self.name,
                        period=period, max=course['max'])

    def post(self, request, **kwargs):
        path = os.path.dirname(__file__)[:-8] + '/static/assignments'
        course = myCourse(self.id)
        result = {}
        period = self.get_argument('period')
        extention = self.request.files['file'][0].filename.split('.')[-1]
        filename = self.id + '-' + period + '.' + extention
        try:
            cmd = 'find ./ -regex ".*/' + self.id + '-' + period + '\.\(jpg\|gif\|png\|jpeg\)" | xargs rm'
            os.system(cmd)
            f = open(os.path.join(path, filename), "w")
            f.write(self.request.files['file'][0].body)
            f.close()
            result['result'] = "作业上传成功"
        except:
            pass

        homeworkUpload(self.id, period, str(course['idcourse']))
        self.redirect('/user/myHomework')


class uploadVideo(tornado.web.RequestHandler):
    # 上传视频作业
    def __init__(self, application, request, **kwargs):
        super(uploadVideo, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')

    def get(self, period):
        if not self.name:
            self.redirect('/login')
        elif self.group != '0':
            self.redirect('/')
        else:
            self.render('homeworkVideoUpdate.html', period=period)

    def post(self, period):
        fulllink = self.get_argument('link')
        result = {}
        try:
            link = fulllink.split()[0].split('/')[2]
            if link != 'pan.baidu.com':
                raise IndexError
            else:
                vedioUpload(self.id, period, myCourse(self.id)['idcourse'], fulllink)
                result['result'] = 'success'
        except IndexError:
            result['result'] = "请输入使用百度云创建的创建公开链接"
        finally:
            self.redirect('/user/myHomework')


class getHomework(tornado.web.RequestHandler):
    def get(self, period):
        pwd = os.path.dirname(__file__)[:-8] + '/static/assignments'
        path = os.popen("find  " + pwd + " -name '" + self.get_secure_cookie('id') + "-" + period + ".*'").read().strip(
            '\n')
        filename = path.split('/')[-1]
        x = open(path)
        self.set_header('Content-Type', 'text/csv')
        self.set_header('Content-Disposition', 'attachment; filename=' + filename)
        self.finish(x.read())


class stuHomeworkDetail(tornado.web.RequestHandler):
    # 学生作业文件下载
    def get(self, period, stuId):
        pwd = os.path.dirname(__file__)[:-8] + '/static/assignments'
        path = os.popen("find " + pwd + " -name '" + str(stuId) + "-" + period + ".*'").read().strip(
            '\n')
        filename = path.split('/')[-1]
        x = open(path)
        self.set_header('Content-Type', 'text/csv')
        self.set_header('Content-Disposition', 'attachment; filename=' + filename)
        self.finish(x.read())


class stuHomeworkPicPreview(tornado.web.RequestHandler):
    # 学生作业图片格式预览，图片限制为jpg格式
    def __init__(self, application, request, **kwargs):
        super(stuHomeworkPicPreview, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self, period, stuId):
        if not self.name:
            self.redirect('/login')
        else:
            pwd = os.path.dirname(__file__)[:-8] + '/static/assignments'
            comm = 'find ' + pwd + ' -regex ".*/' + str(stuId) + '-' + period + '\.\(jpg\|gif\|png\|jpeg\|JPG\)"'
            path = os.popen(comm).read().strip('\n')
            filename = '/static/assignments/' + path.split('/')[-1]
            print filename
            student = viewStudentInfo(stuId)
            self.render('viewHomework.html', stu=student, id=self.id, period=period, filepath=filename,
                        group=self.group)


class stuHomeworkVideoPreview(tornado.web.RequestHandler):
    # 学生作业图片格式预览，图片限制为jpg格式
    def __init__(self, application, request, **kwargs):
        super(stuHomeworkVideoPreview, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self, period, stuId):
        if not self.name:
            self.redirect('/login')
        else:
            link = getHomeworkVideoLink(stuId, period)
            if link is not None:
                self.redirect(link)
            else:
                self.render('error.html', id=self.name, info='作业不存在')


class commentingHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(commentingHandler, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self, stuId, period):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            student = viewStudentInfo(stuId)
            self.render('commenting.html', stu=student, id=self.id, period=period)

    def post(self, *args, **kwargs):
        result = {}
        content = self.get_argument('content')
        stuId = self.get_argument('stuid')
        period = self.get_argument('period')
        try:
            commentingHomework(period, stuId, content)
            result['result'] = 'success'
        except:
            result['result'] = "信息错误"
        self.write(json_encode(result))


class markingHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(markingHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.group = self.get_secure_cookie('group')
        self.name = self.get_secure_cookie('name')

    def get(self, stuId):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            student = viewStudentInfo(stuId)
            self.render('finalComment.html', stu=student, id=self.id)

    def post(self, *args, **kwargs):
        result = {}
        content = self.get_argument('comment')
        score = self.get_argument('socre')
        stuId = self.get_argument('sduId')
        try:
            if score == '':
                finalCommenting(stuId, content)
            else:
                finalScoreing(stuId, content, score)
            result['result'] = 'success'
        except:
            result['result'] = '写入失败'
        self.write(json_encode(result))


class setFormHandler(tornado.web.RequestHandler):
    # 老师设置本次需要上交的作业类型（若不设置则默认为上交图片）
    def __init__(self, application, request, **kwargs):
        super(setFormHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')

    def get(self, courseid):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            self.render('setHomeworkForm.html', id=self.name, course=courseid, courseInfo=getCourseById(courseid))

    def post(self, course):
        form = self.get_argument('checker')
        period = self.get_argument('period')
        setPeriodForm(course, period, form)
        result = {'result': "success"}
        self.write(json_encode(result))


class chooseSubmitHandler(tornado.web.RequestHandler):
    # 学生选择要上传哪一次作业
    def __init__(self, application, request, **kwargs):
        super(chooseSubmitHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')

    def get(self):
        if not self.name:
            self.redirect('/login')
        elif self.group != '0':
            self.redirect('/')
        else:
            self.render('chooseWhich.html', periods=getAllPeriods(getMyCourse(self.id)))


class assignedTypeHandler(tornado.web.RequestHandler):
    # 判断要提交的作业类型
    def __init__(self, application, request, **kwargs):
        super(assignedTypeHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')

    def get(self, period, idcourse, *args, **kwargs):
        if not self.name:
            self.redirect('/login')
        elif self.group != '0':
            self.redirect('/')
        else:
            type = getAssgnmentType(idcourse, period)
            if type == "pic":
                self.redirect('/user/upload/' + period)
            elif type == "video":
                self.redirect('/user/uploadvideo/' + period)


class homeworkTypeHandler(tornado.web.RequestHandler):
    # 判断要查看的作业类型
    def __init__(self, application, request, **kwargs):
        super(homeworkTypeHandler, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')

    def get(self, period, idcourse):
        if not self.name:
            self.redirect('/login')
        elif self.group != '0':
            self.redirect('/')
        else:
            type = getAssgnmentType(idcourse, period)
            if type == "pic":
                self.redirect('/previewImages/' + period + '_' + self.id)
            elif type == "video":
                self.redirect('/previewVideo/' + period + '_' + self.id)
            elif type is None:
                self.write('本次作业不存在')


class homeworkTypeHandlerTeacher(tornado.web.RequestHandler):
    # 判断要查看的作业类型
    def __init__(self, application, request, **kwargs):
        super(homeworkTypeHandlerTeacher, self).__init__(application, request, **kwargs)
        self.id = self.get_secure_cookie('id')
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')

    def get(self, period, idcourse, idstu):
        if not self.name:
            self.redirect('/login')
        else:
            type = getAssgnmentType(idcourse, period)
            if type == "pic":
                self.redirect('/previewImages/' + period + '_' + idstu)
            elif type == "video":
                self.redirect('/previewVideo/' + period + '_' + idstu)
            elif type is None:
                self.render('error.html', id=self.name, info='本次作业不存在')
