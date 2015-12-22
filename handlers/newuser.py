# coding: utf-8
from base.base import BaseHandler
from dash import is_loged
from models.userOperation import getTempUser, insertIntoTempUser, getStudent, getTeacher, getATempUser, authNewUser


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
        pwdC = self.get_argument('pwdConfirm')
        id = self.get_argument('id')
        ugroup = self.get_argument('ug')
        email = self.get_argument('email')

        if pwd!=pwdC:
            # 判断两次输入的密码不相同时候
            self.render('error.html', title=None, content='两次输入的密码不同<br>请重新注册', icon='ion-alert-circled',
                        active='none', id=None)
        else:
            if ugroup == 'teacher':
                ugroup = 't'
            elif ugroup == 'student':
                ugroup = 's'
            try:
                if getStudent(id) is None and getTeacher(id) is None:
                    # 账户不存在'
                    if not getATempUser(id):
                        # 在临时表中没有记录
                        insertIntoTempUser(id, ugroup, name, pwd, email)
                        self.render('error.html', title='申请成功', content='请等待管理员通过你的申请吧', icon='ion-checkmark-circled',
                                    active='none', id=None)
                    else:
                        # 这个账户已经申请过，在临时表里有记录
                        self.render('error.html', title=None, content='请等待管理员通过你的申请吧', icon='ion-alert-circled',
                                    active='none', id=None)
                else:
                    # 账户已经存在， 一个账户只能存在于一个用户组里
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
        print uid
        if uid == str(int(1e6)):
            self.render('admin.html', temp=getTempUser(), active='none')
        else:
            self.redirect('/404')


class AuthUserHandler(BaseHandler):
    """管理员通过新用户申请"""

    def get(self, tp_id):
        gp, uid = is_loged(self)
        try:
            if uid == str(int(1e6)):
                returned = authNewUser(tp_id)
                if returned == "success":
                    self.render('error.html', title='认证成功', content='新用户授权成功', icon='ion-checkmark-circled', active='',
                                id=uid)
                elif returned == 'fail':
                    self.render('error.html', title='认证失败', content='新用户授权失败', icon='ion-close-circled', active='',
                                id=uid)
            else:
                print uid
                self.redirect('/404')
        except:
            self.render('error.html', title=None, content='出错啦', icon='ion-alert-circled', active='none', id=uid)
            # 页面渲染有问题！！
