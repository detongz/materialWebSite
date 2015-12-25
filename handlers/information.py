# coding: utf-8
from base.base import BaseHandler
from dash import is_loged
from models.notification import get_info_by_infoid, publish_notif, publish_res, get_info, update_notif, get_all_notif,\
            get_info_by_infoid_all, delete_notif
from models.security import html2Text

import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class PublishResourceHandler(BaseHandler):
    """教师发布课程资源"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.clear_cookie('Iid')
            self.render('teacher_publish_resource.html', id=uid, active='dsh', active_slide='ntfc', r_content=None,
                        r_title=None, act='pub')
        else:
            self.redirect('/404')

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            content = self.get_argument('content')
            title = self.get_argument('title')

            if len(title) > 50:
                self.render('error.html', title=None, content='标题过长<br>请重新输入', icon='ion-alert-circled', active='ntfc',
                            id=uid)
            else:
                from postingInfo import infoIdState
                idInfo = infoIdState(self)

                try:
                    publish_res(uid, idInfo, content, title)
                    self.render('error.html', title='资源发布成功', content='成功发布了一条课程资源', icon='ion-checkmark-circled',
                                active='ntfc', id=uid)
                    self.clear_cookie('Iid')
                except Exception as e:
                    self.clear_cookie('Iid')
                    print e


class PublishNotificationHandler(BaseHandler):
    """教师发布课程通知"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.clear_cookie('Iid')
            self.render('teacher_publish_notif.html', id=uid, active='dsh', active_slide='ntfc', n_title=None,
                        content=None, act='pub')
        else:
            self.redirect('/404')

    def post(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            content = self.get_argument('content')
            title = self.get_argument('title')

            if len(title) > 50:
                self.render('error.html', title=None, content='标题过长<br>请重新输入', icon='ion-alert-circled', active='ntfc',
                            id=uid)
            else:

                from postingInfo import infoIdState
                idInfo = infoIdState(self)

                try:
                    if not publish_notif(uid, idInfo, content, title):
                        self.render('error.html', title='通知发布成功', content='成功发布了一条课程通知', icon='ion-checkmark-circled',
                                    active='dsh', id=uid)
                        self.clear_cookie('Iid')
                    else:
                        print 'teacher not exist'
                        self.clear_cookie('Iid')
                except Exception as e:
                    self.clear_cookie('Iid')
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

            self.clear_cookie('Iid')
            self.set_secure_cookie('Iid',infoId)

            info = get_info(infoId)
            content = info['detail']
            title = info['t‎itle']

            self.render('teacher_publish_notif.html', id=uid, active='dsh', active_slide='ntfc', n_title=title,
                        content=content, act='edit')

        else:
            self.redirect('/404')

    def post(self, infoId, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            content = self.get_argument('content')
            title = self.get_argument('title')

            if len(title) > 50:
                self.render('error.html', title=None, content='标题过长<br>请重新输入', icon='ion-alert-circled', active='ntfc',
                            id=uid)
            else:
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

            self.clear_cookie('Iid')


class EditResourceHandler(BaseHandler):
    """编辑课程资源"""

    def get(self, infoId, *args, **kwargs):
        gp, uid = is_loged(self)

        if gp == 't':

            self.clear_cookie('Iid')
            self.set_secure_cookie('Iid',infoId)

            info = get_info(infoId)
            content = info['detail']
            title = info['t‎itle']

            self.render('teacher_publish_resource.html', id=uid, active='dsh', active_slide='ntfc', r_title=title,
                        r_content=content, act='edit')

        else:
            self.redirect('/404')

    def post(self, infoId, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            content = self.get_argument('content')
            title = self.get_argument('title')

            if len(title) > 50:
                self.render('error.html', title=None, content='标题过长<br>请重新输入', icon='ion-alert-circled', active='ntfc',
                            id=uid)
            else:
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
            self.clear_cookie('Iid')


class NotificationIndexHandler(BaseHandler):
    """课程资源里列表"""

    def get(self):
        uid = self.get_secure_cookie('id')
        info = get_all_notif()

        self.render('notification.html',id=uid,active='notification', info = info)


class ResourseDetailHandler(BaseHandler):
    """课程通知详情"""

    def get(self, Iid):
        uid = self.get_secure_cookie('id')
        info = get_info_by_infoid_all(Iid)

        self.render('infoDetail.html',id=uid,info=info,active='notification')


class InfoDetailHandler(BaseHandler):
    """课程资源详情"""

    def get(self, Iid):
        uid = self.get_secure_cookie('id')
        info = get_info_by_infoid_all(Iid)

        self.render('infoDetail.html',id=uid,info=info,active='notification')


class RemoveNotifHandler(BaseHandler):
    """删除已经发布的信息"""

    def get(self,iid):
        gp, uid = is_loged(self)

        if gp == 't':
            try:
                delete_notif(iid,uid) # 删除记录
                from submitAssignment import delete_updated
                delete_updated(iid) # 删除文件

                self.redirect('/dash/notifications')

            except Exception as e:
                print e
        else:
            self.redirect('/')
