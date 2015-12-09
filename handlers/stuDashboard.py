# coding: utf-8
from base.base import BaseHandler
from dash import is_loged
from models.notification import get_all_notif, get_all_comments
from models.homework import get_my_homework
import os

class MyHomeworkHandler(BaseHandler):
    """我的所有作业"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            self.render('stu_homework.html', homework=get_my_homework(uid), id=uid, active='dsh', active_slide='hmwk')
        else:
            self.redirect('/404')


class MyMessagesHandler(BaseHandler):
    """所有消息提示"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            self.render('stu_message.html', id=uid, message=get_all_notif(), comments=get_all_comments(uid),
                        active='dsh', active_slide='msg')
        else:
            self.redirect('/404')


class MyCourseHandler(BaseHandler):
    """我的课程界面"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            pass
        else:
            self.redirect('/404')


class submitAssgnmentHandler(BaseHandler):
    """ 学生提交作业 """

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            self.render('stu_submitassignment.html', id=uid, active='dsh', active_slide='mcs')
        else:
            self.render('error.html', title=None, content='提交作业要先登陆哦', icon='ion-happy', active='', id=uid)

    def post(self):
        gp, uid = is_loged(self)
        if gp == 's':
            print self.get_argument('content')
            print self.get_argument('submitName')
            self.render('stu_step2.html', id=uid, active='dsh', active_slide='mcs')


class submitStep2(BaseHandler):
    """提交正视图"""

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            fname = self.request.files['frontal'][0].filename
            if not extensionJudge(fname, uid, self):
                f = self.request.files['frontal'][0].body
                self.render('stu_step3.html', id=uid, active='dsh', active_slide='mcs')


class submitStep3(BaseHandler):
    """提交俯视图"""

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            fname = self.request.files['top'][0].filename
            if not extensionJudge(fname, uid, self):
                f = self.request.files['top'][0].body
                self.render('stu_step4.html', id=uid, active='dsh', active_slide='mcs')


class submitStep4(BaseHandler):
    """提交侧视图"""

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':
            fname = self.request.files['profile'][0].filename
            if not extensionJudge(fname, uid, self):
                f = self.request.files['profile'][0].body
                self.render('error.html', title="提交成功", content='作业提交成功', icon='ion-checkmark-circled', id=uid, active='dsh')


def extensionJudge(fname, uid, request):
    """判断提交文件是否是图片格式"""

    ext = fname.split('.')[-1]
    if ext not in ['jpg', 'jpeg', 'png', 'gif', 'JPEG', 'tiff', 'tif', 'raw']:
        request.render('error.html', title="提交失败", content='请提交图片格式的作业哦', icon='ion-happy', id=uid, active='dsh')
        return 'error'
    return None


def saveFile(fname,uid,f):
    """保存上传的文件"""