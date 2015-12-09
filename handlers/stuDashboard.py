# coding: utf-8
import os
import commands

from base.base import BaseHandler
from dash import is_loged
from models.notification import get_all_notif, get_all_comments
from models.homework import get_my_homework, get_homework
from models.security import clean


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


class ViewHomeworkHandler(BaseHandler):
    """查看某次作业"""

    def get(self, hid, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':

            homework = get_homework(hid)

            if not homework:
                self.render('error.html', title=None, content="作业不存在", icon='ion-sad', active='dsh', id=uid)

            else:
                if homework['type'] == 'pic':
                    # 作业是图片类型

                    path = get_file_path(hid)

                    if len(path) != 3:
                        # 没有获得三个文件
                        self.render('error.html', title=None, content=None, icon='ion-sad', active='dsh', id=uid)
                    else:

                        fname = []
                        for p in path:
                            f = p.split('/')[-1]
                            if f.split('.')[-1] in {'jpg', 'jpeg', 'png', 'gif', 'JPEG', 'JPG', 'tiff', 'tif', 'raw'}:
                                fname.append(f)

                        if len(fname) != 3:
                            # 没有获得三个图片文件
                            self.render('error.html', title=None, content=None, icon='ion-sad', active='dsh', id=uid)

                        else:
                            self.render('stu_homework_once.html', homework=homework, id=uid, active='dsh',
                                        active_slide='hmwk', front=fname[0], portrait=fname[1], top=fname[2])
                else:
                    # video类型作业
                    self.render('stu_homework_once.html', homework=homework, id=uid, active='dsh', active_slide='hmwk')
        else:
            self.redirect('/404')


class RemoveHomeworkHandler(BaseHandler):
    """删去某次作业"""
    """未实现！"""

    def get(self, hid, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 's':

            homework = get_homework(hid)

            if not homework:
                self.render('error.html', title=None, content="作业不存在", icon='ion-sad', active='dsh', id=uid)

            else:
                if homework['type'] == 'pic':
                    # 作业是图片类型
                    pass
                else:
                    pass

        else:
            self.redirect('/404')


def get_file_path(hid):
    """获取提交的三视图文件路径"""

    dirpath = os.path.dirname(__file__)[:-8] + 'static/homework/'
    comm = "find %s -name '%s*'" % (dirpath, clean(hid))
    return commands.getstatusoutput(comm)[1].split('\n')