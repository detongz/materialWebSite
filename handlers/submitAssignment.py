# coding: utf-8

import os
import base64
from base.base import BaseHandler
from dash import is_loged
from models.course import get_student_course
from models.homework import get_homework, submit_homework, submit_homework_vedio

"""学生交作业"""


class submitAssgnmentHandler(BaseHandler):
    """ 学生提交作业 """

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            # 判断是否登陆
            cid = get_student_course(uid)
            if cid == '':
                # 数据库中没有课程号记录
                self.render('error.html', title=None, content='提交作业要先录入课程号哦', icon='ion-happy', active='', id=uid)
            else:
                self.render('stu_submitassignment.html', id=uid, active='dsh', active_slide='mcs')
        else:
            self.render('error.html', title=None, content='提交作业要先登陆哦', icon='ion-happy', active='', id=uid)

    def post(self):
        gp, uid = is_loged(self)
        if gp == 's':
            content = self.get_argument('content')
            submitName = self.get_argument('submitName')

            # 生成idhomework
            import random

            idHomework = uid + str(random.randint(99, 1000))
            while True:
                # 获取idhomework的值直到获取到数据库中与其他记录不冲突为止
                if not get_homework(idHomework):
                    break
                idHomework = uid + str(random.randint(99, 1000))

            # 删除文件夹下所有相同id的文件
            # 未实现！！！！
            self.clear_cookie('content')
            self.clear_cookie('submitName')
            self.clear_cookie('hid')
            self.clear_cookie('frontal')
            self.clear_cookie('top')

            self.set_secure_cookie('content', base64.encodestring(content.encode('utf8')))  # 命名简单加密后加载到cookie中保存
            self.set_secure_cookie('submitName', base64.encodestring(submitName.encode('utf8')))
            self.set_secure_cookie('hid', idHomework)
            self.render('stu_step2.html', id=uid, active='dsh', active_slide='mcs')


class submitStep2(BaseHandler):
    """提交正视图"""

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            fname = self.request.files['frontal'][0].filename
            if not extensionJudge(fname, uid, self):

                hid = self.get_secure_cookie('hid')

                if self.get_secure_cookie('submitName') != '' and hid != '':
                    # 判断是否已经完成了之前的提交步骤
                    f = self.request.files['frontal'][0].body

                    saveFile(fname, hid, f, 'frontal')

                    self.set_secure_cookie('frontal', '1')
                    self.render('stu_step3.html', id=uid, active='dsh', active_slide='mcs')

                else:
                    self.render('error.html', title=None, content='请按顺序交作业哦', icon='ion-happy', active='dsh', id=uid)


class submitStep3(BaseHandler):
    """提交俯视图"""

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            fname = self.request.files['top'][0].filename
            if not extensionJudge(fname, uid, self):

                hid = self.get_secure_cookie('hid')

                if self.get_secure_cookie('frontal') == '1' and self.get_secure_cookie(
                        'submitName') is not None and hid != '':
                    # 判断是否已经完成了之前的提交步骤

                    f = self.request.files['top'][0].body
                    saveFile(fname, hid, f, 'top')

                    self.set_secure_cookie('top', '1')
                    self.render('stu_step4.html', id=uid, active='dsh', active_slide='mcs')

                else:
                    self.render('error.html', title=None, content='请按顺序交作业哦', icon='ion-happy', active='dsh', id=uid)


class submitStep4(BaseHandler):
    """提交侧视图"""

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            fname = self.request.files['profile'][0].filename
            if not extensionJudge(fname, uid, self):

                hid = self.get_secure_cookie('hid')

                if self.get_secure_cookie('frontal') == '1' and self.get_secure_cookie('submitName') is not None \
                        and self.get_secure_cookie('top') == '1' and hid is not None:
                    # 判断是否已经完成了之前的提交步骤

                    f = self.request.files['profile'][0].body
                    saveFile(fname, hid, f, 'profile')

                    try:
                        content = base64.decodestring(self.get_secure_cookie('content'))
                        submitName = base64.decodestring(self.get_secure_cookie('submitName'))
                        print content, submitName
                        submit_homework(hid, uid, content, submitName)

                        self.clear_cookie('content')
                        self.clear_cookie('submitName')
                        self.clear_cookie('hid')
                        self.clear_cookie('frontal')
                        self.clear_cookie('top')

                        self.render('error.html', title="提交成功", content='作业提交成功', icon='ion-checkmark-circled', id=uid,
                                    active='dsh')
                    except Exception as e:
                        print e
                else:
                    self.render('error.html', title=None, content='请按顺序交作业哦', icon='ion-happy', active='dsh', id=uid)


def saveFile(fname, hid, f, type):
    """保存上传的文件"""
    for i in range(4):
        try:
            dirpath = os.path.dirname(__file__)[:-8] + 'static/homework/'
            num = {'top': '2', 'profile': '3', 'frontal': '1'}
            fpath = dirpath + hid + '-' + num[type] + '.' + fname.split('.')[-1]
            sf = open(fpath, 'w')
            sf.write(f)
            sf.close()
            return None

        except Exception as e:
            print e
    return 'error'


def extensionJudge(fname, uid, request):
    """判断提交文件是否是图片格式"""

    ext = fname.split('.')[-1]
    if ext not in {'jpg', 'jpeg', 'png', 'gif', 'JPEG', 'JPG', 'tiff', 'tif', 'raw'}:
        request.render('error.html', title="提交失败", content='请提交图片格式的作业哦', icon='ion-happy', id=uid, active='dsh')
        return 'error'
    return None


class submitVedio(BaseHandler):
    """提交视频作业"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            # 判断是否登陆
            cid = get_student_course(uid)
            if not cid:
                # 数据库中没有课程号记录
                self.render('error.html', title=None, content='提交作业要先录入课程号哦', icon='ion-happy', active='', id=uid)
            else:
                self.render('stu_submit_vedio.html', id=uid, active='dsh', active_slide='mcs')
        else:
            self.render('error.html', title=None, content='提交作业要先登陆哦', icon='ion-happy', active='', id=uid)

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':

            # 生成idhomework
            import random

            idHomework = uid + str(random.randint(99, 1000))
            while True:
                # 获取idhomework的值直到获取到数据库中与其他记录不冲突为止
                if not get_homework(idHomework):
                    break
                idHomework = uid + str(random.randint(99, 1000))

            name = self.get_argument('submitName').encode('utf-8')
            content = self.get_argument('content').encode('utf-8')

            try:
                submit_homework_vedio(idHomework, uid, content, name)
                self.render('error.html', title="提交成功", content='作业提交成功', icon='ion-checkmark-circled', id=uid,
                            active='dsh')
            except Exception as e:
                print e
