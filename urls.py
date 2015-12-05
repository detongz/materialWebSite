# coding: utf-8
from handlers.index import IndexHandler
from handlers.login import LoginHandler, LogoutHandler
from handlers.error import ErrorHandler
from handlers.dash import DashBoardHandler
from handlers.teaDashboard import CourseEditHandler, EditingCertainCourseHandler, DeleteCourseHandler, \
    CommentingHandler, MyStudentsHandler, MyNotifHandler
from handlers.stuDashboard import MyHomeworkHandler, MyMessagesHandler,MyCourseHandler

urls = [
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),

    #教师接口
    # (r'/dash/commenting/(.*)', ),
    (r'/dash/commenting', CommentingHandler),

    (r'/dash/editCourse/delete/(.*)', DeleteCourseHandler),
    (r'/dash/editCourse/(.*)', EditingCertainCourseHandler),
    (r'/dash/editCourse', CourseEditHandler),
    (r'/dash/allStudents', MyStudentsHandler),
    (r'/dash/notifications', MyNotifHandler),

    #学生接口
    (r'/dash/messages',MyMessagesHandler),
    (r'/dash/myHomework',MyHomeworkHandler),

    (r'/dash', DashBoardHandler),
    (r'/.*', ErrorHandler)
]
