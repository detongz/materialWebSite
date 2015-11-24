# coding: utf-8
"""
课程动态课程资源相关操作
"""

import tornado.web
from tornado.escape import json_encode
from models.queryResourse import publishingInformation, getnotification, getresources, getInfoDetail
from models.query import getTeacherInfo
import os


class resourseHandler(tornado.web.RequestHandler):
    def get(self, *args, **kwargs):
        self.name = self.get_secure_cookie('name')
        resource = getresources()
        self.render('notificationsIndex.html', id=self.name, pageType='resource', info=resource)


class notificationIndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.name = self.get_secure_cookie('name')
        notification = getnotification()
        self.render('notificationsIndex.html', id=self.name, pageType='notification', info=notification)


class notificationDetailHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.name = self.get_secure_cookie('name')
        info = getInfoDetail(id)
        teacher=getTeacherInfo(info['idteacher'])
        self.render('infoDetail.html', id=self.name, pageType="notification", info=info,teacher=teacher)


class resourseDetailHandler(tornado.web.RequestHandler):
    def get(self, id):
        self.name = self.get_secure_cookie('name')
        info = getInfoDetail(id)
        teacher=getTeacherInfo(info['idteacher'])
        self.render('infoDetail.html', id=self.name, pageType="resource", info=info,teacher=teacher)


class chooseInfoToPostHandler(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(chooseInfoToPostHandler, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            self.render('chooseInfoToPost.html')


class publishNotification(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(publishNotification, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            self.render('publishNotification.html')

    def post(self, *args, **kwargs):
        title = self.get_argument('title')
        content = self.get_argument('content')
        idtemplate = publishingInformation(self.id, title, 'notification')
        saveTemplate(text2Html(content), idtemplate)
        result = {'result': 'success','url':'/notifications'}
        self.write(json_encode(result))


class publishResources(tornado.web.RequestHandler):
    def __init__(self, application, request, **kwargs):
        super(publishResources, self).__init__(application, request, **kwargs)
        self.name = self.get_secure_cookie('name')
        self.group = self.get_secure_cookie('group')
        self.id = self.get_secure_cookie('id')

    def get(self):
        if not self.name:
            self.redirect('/login')
        elif self.group != '1':
            self.redirect('/')
        else:
            self.render('publishResources.html')

    def post(self, *args, **kwargs):
        title = self.get_argument('title')
        content = self.get_argument('content')
        idtemplate = publishingInformation(self.id, title, 'resource')
        saveTemplate(text2Html(content), idtemplate)
        result = {'result': 'success', 'url': '/resource'}
        self.write(json_encode(result))


def text2Html(content):
    def escape(txt):
        """将txt文本中的空格、&、<、>、（"）、（'）转化成对应的的字符实体，以方便在html上显示"""
        txt = txt.replace('&', '&#38;')
        txt = txt.replace(' ', '&#160;')
        txt = txt.replace('<', '&#60;')
        txt = txt.replace('>', '&#62;')
        txt = txt.replace('"', '&#34;')
        txt = txt.replace('\'', '&#39;')
        return txt

    content = escape(content)
    lines = content.split('\n')
    for i, line in enumerate(lines):
        lines[i] = '<p>' + line + '</p><br>'
    content = ''.join(lines)
    return content


def saveTemplate(content, idtemplate):
    # 将转换好的html存为文件
    pwd = os.path.dirname(__file__)[:-8] + '/templates/resource/'
    with open(pwd + str(idtemplate) + '.html', 'w') as f:
        f.write(content.encode('utf-8'))
