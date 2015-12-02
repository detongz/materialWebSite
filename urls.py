# coding: utf-8
from handlers.index import IndexHandler
from handlers.login import LoginHandler, LogoutHandler
from handlers.error import ErrorHandler
from handlers.dash import DashBoardHandler
from handlers.teaDashboard import CourseEditHandler, EditingCertainCourseHandler

urls = [
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/dash', DashBoardHandler),
    (r'/dash/editCourse/(.*)', EditingCertainCourseHandler),
    (r'/dash/editCourse', CourseEditHandler),

    (r'/.*', ErrorHandler)
]
