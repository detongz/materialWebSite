# coding:utf-8

from urls import urls
import tornado.web
import os

setting = dict(
    template_path=os.path.join(os.path.dirname(__file__), "templates"),
    static_path=os.path.join(os.path.dirname(__file__), "static"),
    debug="True",
    cookie_secret="bZJc2sWbQLKos6GkHn/VB9oXwQt8S0R0kRvJ5/xJ89E=",
    login_url="/login",
)

application = tornado.web.Application(
    handlers=urls,
    **setting
)
