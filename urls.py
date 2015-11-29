# coding: utf-8
from handlers.index import IndexHandler
from handlers.login import LoginHandler, LogoutHandler
from handlers.error import ErrorHandler

urls = [
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),

    (r'/.*', ErrorHandler)
]
