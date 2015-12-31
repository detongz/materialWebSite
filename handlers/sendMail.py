# -*- coding: utf-8 -*-
"""
发送html文本邮件
"""
import smtplib
from email.mime.text import MIMEText

mail_host = 'smtp.dlut.edu.cn'  # 转发邮箱服务器地址
mail_user = "holdyourgun@mail.dlut.edu.cn"  # 用户名
mail_pass = "zxcuahsid"  # 口令
mail_postfix = "dlut.edu.cn"  # 发件箱的后缀


def send_mail(to_list, sub, content):  # to_list：收件人；sub：主题；content：邮件内容
    me = "化学的某一个网站" + "<" + mail_user + "@" + mail_postfix + ">"  # 这里的hello可以任意设置，收到信后，将按照设置显示
    msg = MIMEText(content, _subtype='html', _charset='utf-8 ')  # 创建一个实例，这里设置为html格式邮件
    msg['Subject'] = sub  # 设置主题
    msg['From'] = me
    msg['To'] = ";".join(to_list)
    try:
        s = smtplib.SMTP()
        s.connect(mail_host)  # 连接smtp服务器
        s.starttls()
        s.login(mail_user, mail_pass)  # 登陆服务器
        s.sendmail(me, to_list, msg.as_string())  # 发送邮件
        s.close()
        return True
    except Exception, e:
        print str(e)
        return False


def send_forget_mail(toAddress, User):
    mailto_list = [toAddress]
    send_mail(mailto_list, "化学那啥网的忘记密码邮件主题", "<h3>账号:%s</h3><h4>密码:%s</h4>" % (User['name'], User['pwd']))
