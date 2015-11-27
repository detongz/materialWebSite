# coding:utf-8
import os
import tornado.web
from urls import urls

TEMPLATE_PATH = os.path.join(os.path.dirname(__file__), "templates")
STATIC_PATH = os.path.join(os.path.dirname(__file__), "static")

settings = dict(
    template_path=TEMPLATE_PATH,
    static_path=STATIC_PATH,
    debug="True",
    cookie_secret="asdfasdfasdfasdf",
    login_url="/login",
)


class application(tornado.web.Application):
    def __init__(self):
        setting = settings
        handlers = urls
        tornado.web.Application.__init__(self, handlers, **setting)
