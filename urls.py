# coding: utf-8
from handlers.index import IndexHandler
from handlers.login import LoginHandler, LogoutHandler
from handlers.error import ErrorHandler
from handlers.dash import DashBoardHandler
from handlers.teaDashboard import CourseEditHandler, EditingCertainCourseHandler, DeleteCourseHandler, \
    CommentingHandler, MyStudentsHandler, MyNotifHandler
from handlers.stuDashboard import MyHomeworkHandler, MyMessagesHandler, ViewHomeworkHandler, RemoveHomeworkHandler
from handlers.submitAssignment import submitAssgnmentHandler, submitStep2, submitStep3, submitStep4, submitVedio
from handlers.newuser import SignUpHandler, AdminHandler, AuthUserHandler

urls = [
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/signup', SignUpHandler),

    # 教师接口
    # (r'/dash/commenting/(.*)', ),
    (r'/dash/commenting', CommentingHandler),

    (r'/dash/editCourse/delete/(.*)', DeleteCourseHandler),
    (r'/dash/editCourse/(.*)', EditingCertainCourseHandler),
    (r'/dash/editCourse', CourseEditHandler),
    (r'/dash/allStudents', MyStudentsHandler),
    (r'/dash/notifications', MyNotifHandler),

    # 学生接口
    (r'/dash/messages', MyMessagesHandler),
    (r'/dash/myHomework', MyHomeworkHandler),
    (r'/dash/myHomework/view/(.*)', ViewHomeworkHandler),
    (r'/dash/myHomework/delete/(.*)', RemoveHomeworkHandler),
    (r'/submitAssgnment-Vedio', submitVedio),  # 交视频作业
    (r'/submitAssgnment-1', submitStep2),  # 交作业
    (r'/submitAssgnment-2', submitStep3),  # 交作业
    (r'/submitAssgnment-3', submitStep4),  # 交作业
    (r'/submitAssgnment', submitAssgnmentHandler),  # 交作业

    (r'/dash', DashBoardHandler),

    # 管理员新用户认证
    (r'/TWF5IEplZmYgRGVhbiBCbGVzcyBNeSBXaWVyZCBXZWIgQXBwbGljYXRpb24=/(.*)', AuthUserHandler),
    (r'/TWF5IEplZmYgRGVhbiBCbGVzcyBNeSBXaWVyZCBXZWIgQXBwbGljYXRpb24=', AdminHandler),

    # error
    (r'/.*', ErrorHandler),
]
