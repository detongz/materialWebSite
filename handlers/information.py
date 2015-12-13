# coding: utf-8
from base.base import BaseHandler
from dash import is_loged
from models.notification import get_info_by_infoid, publish_notif, publish_res, get_info, update_notif
from models.security import html2Text
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class PublishResourceHandler(BaseHandler):
    """教师发布课程资源"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.render('teacher_publish_resource.html', id=uid, active='dsh', active_slide='ntfc', r_content=None,
                        r_title=None)
        else:
            self.redirect('/404')

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            content = self.get_argument('content')
            title = self.get_argument('title')

            idInfo = generateInfoid()

            try:
                publish_res(uid, idInfo, content, title)
                self.render('error.html', title='资源发布成功', content='成功发布了一条课程资源', icon='ion-checkmark-circled',
                            active='ntfc', id=uid)
            except Exception as e:
                print e


class PublishNotificationHandler(BaseHandler):
    """教师发布课程通知"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.render('teacher_publish_notif.html', id=uid, active='dsh', active_slide='ntfc', r_title=None,
                        content=None)
        else:
            self.redirect('/404')

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            content = self.get_argument('content')
            title = self.get_argument('title')

            idInfo = generateInfoid()

            try:
                if not publish_notif(uid, idInfo, content, title):
                    self.render('error.html', title='通知发布成功', content='成功发布了一条课程通知', icon='ion-checkmark-circled',
                                active='dsh', id=uid)
                else:
                    print 'teacher not exist'
            except Exception as e:
                print e


def generateInfoid():
    """使用时间信息生成消息id号"""

    import datetime as dt
    import random as rd

    idInfo = dt.datetime.now().strftime('%Y%m%d')
    rd = rd.randint(99, 1000)
    idInfo += str(rd)

    while True:
        result = get_info_by_infoid(idInfo)
        if not result:
            break
        rd = rd.randint(99, 1000)
        idInfo = idInfo[0:8] + str(rd)

    return idInfo


class EditNotificationHandler(BaseHandler):
    """编辑课程通知"""

    def get(self, infoId, *args, **kwargs):
        gp, uid = is_loged(self)

        if gp == 't':
            info = get_info(infoId)
            content = html2Text(info['detail'])
            title = info(['title'])

            self.render('teacher_publish_notif.html', id=uid, active='dsh', active_slide='ntfc', r_title=title,
                        content=content)
        else:
            self.redirect('/404')

    def post(self, infoId, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            content = self.get_argument('content')
            title = self.get_argument('title')

            if not get_info(infoId):
                self.render('error.html', title=None, content='通知不存在', icon='ion-sad', active='dsh', id=uid)
            else:
                try:
                    if not update_notif(infoId, content, title):
                        self.render('error.html', title='通知更新成功', content='成功更新了一条课程通知', icon='ion-checkmark-circled',
                                    active='dsh', id=uid)
                    else:
                        print 'teacher not exist'
                except Exception as e:
                    print e


class EditResourceHandler(BaseHandler):
    """编辑课程资源"""

    def get(self, infoId, *args, **kwargs):
        gp, uid = is_loged(self)

        if gp == 't':
            info = get_info(infoId)
            content = html2Text(info['detail'])
            title = info(['title'])

            self.render('teacher_publish_resource.html', id=uid, active='dsh', active_slide='ntfc', r_title=title,
                        content=content)
        else:
            self.redirect('/404')

    def post(self, infoId, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            content = self.get_argument('content')
            title = self.get_argument('title')

            if not get_info(infoId):
                self.render('error.html', title=None, content='通知不存在', icon='ion-sad', active='dsh', id=uid)
            else:
                try:
                    if not update_notif(infoId, content, title):
                        self.render('error.html', title='通知更新成功', content='成功更新了一条课程通知', icon='ion-checkmark-circled',
                                    active='dsh', id=uid)
                    else:
                        print 'teacher not exist'
                except Exception as e:
                    print e
