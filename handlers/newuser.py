# coding: utf-8
from base.base import BaseHandler
from dash import is_loged
from models.userOperation import getTempUser, insertIntoTempUser, getStudent, getTeacher, getATempUser


class SignUpHandler(BaseHandler):
    """新用户注册"""

    def prepare(self):
        self.id = self.get_secure_cookie('id')

    def get(self):
        if not self.id:
            self.render('signup.html', id=None, active='lgin')
        else:
            self.redirect('/')

    def post(self):
        name = self.get_argument('signupName')
        pwd = self.get_argument('password')
        id = self.get_argument('id')
        ugroup = self.get_argument('ug')

        if ugroup == 'teacher':
            ugroup = 't'
        elif ugroup == 'student':
            ugroup = 's'
        try:
            if getStudent(id) is None and getTeacher(id) is None:
                if getATempUser(id) is None:
                    insertIntoTempUser(id, ugroup, name, pwd)
                    self.render('error.html', title='申请成功', content='请等待管理员通过你的申请吧', icon='ion-checkmark-circled',
                                active='none', id=None)
                else:
                    self.render('error.html', title=None, content='请等待管理员通过你的申请吧', icon='ion-alert-circled',
                                active='none', id=None)
            else:
                self.render('error.html', title=None, content='这个号码已经被注册过了', icon='ion-alert-circled', active='none',
                            id=None)
        except Exception as e:
            print("Error!", e)
            self.render('error.html', title='申请失败', content='出错啦，请重新申请新用户', icon='ion-alert-circled', active='none',
                        id=None)


class AdminHandler(BaseHandler):
    """管理员用户界面，认证教师用户"""

    def get(self):
        gp, uid = is_loged(self)
        if uid == str(int(1e6)):
            self.render('admin.html', temp=getTempUser(), active='none')
        else:
            self.redirect('/404')


class AuthUserHandler(BaseHandler):
    """管理员通过新用户申请"""

    def get(self, tp_id):
        gp, uid = is_loged(self)
        if uid == str(int(1e6)):
            pass
        else:
            self.redirect('/404')
