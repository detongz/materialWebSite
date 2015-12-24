# coding: utf-8
from base.base import BaseHandler
from myCaptcha import Captcha
import random
from sendMail import send_forget_mail

#TODO:这里用了模拟数据{‘name’:'zhj','pwd':'123','email':'928835127@qq.com','id':'201492470'}
#TODO:正式使用时请解除下行注释
#from models.userOperation import getTeacher, getStudent

class ForgetPassHandler(BaseHandler):
    #忘记密码首页
    def get(self, *args, **kwargs):
        ug = self.get_argument('ug') or ''
        if ug != u's' and ug != u't':
            self.redirect('./login')
        self.render('forget_pass.html',group = ug,msg='')

    def post(self, *args, **kwargs):
        id = self.get_argument('id') or ''
        ug = self.get_argument('group') or ''
        email = self.get_argument('email') or ''
        _code = self.get_argument('code') or ''
        if not id or not ug or not email:
            return self.render('forget_pass.html',msg = '请完整填写信息',group=ug)
        if not _code:
            return self.render('forget_pass.html',msg = '请输入验证码',group=ug)
        ca = Captcha(self)
        if ca.check(_code):
            if ug == 't':
                u = {'name' : 'zhj','pwd' : '123','email' : '928835127@qq.com','id' : '201492470'}
                #TODO:正式使用时注释上一行，解除注释下一行
                #u = getTeacher(id)
            elif ug == 's':
                u = {'name' : 'zhj','pwd' : '123','email' : '928835127@qq.com','id' : '201492470'}
                #TODO:正式使用时注释上一行，解除注释下一行
                #u = getStudent(id)
            else:
                self.redirect('./login')
            if u['email'] == email:
                send_forget_mail(email,User  = u)
                return self.render('forget_pass.html',msg = '已将密码发往您的邮箱',group=ug)
            else:
                return self.render('forget_pass.html',msg = '邮箱地址错误',group=ug)
        else:
            return self.render('forget_pass.html',msg = '验证码错误',group=ug)

class VarifyCodeHandler(BaseHandler):
    def get(self, *args, **kwargs):
        figures = [2,3,4,5,6,7,8,9]
        ca =  Captcha(self)
        ca.worlds = [''.join([str(random.sample(figures,1)[0]) for i in range(0,4)])]
        ca.type = 'number'
        return ca.display()
