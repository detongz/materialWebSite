# coding:utf-8

from tornado.web import RequestHandler
from models import db


class BaseHandler(RequestHandler):
    def initialize(self):
        self.access = db
