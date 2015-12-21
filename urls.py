# coding: utf-8
from handlers.index import IndexHandler
from handlers.login import LoginHandler, LogoutHandler
from handlers.error import ErrorHandler
from handlers.dash import DashBoardHandler
from handlers.teaDashboard import CourseEditHandler, EditingCertainCourseHandler, DeleteCourseHandler, \
    CommentingHandler, CommentingIndexHandler, MyStudentsHandler, MyNotifHandler, PublishEntrenceHandler
from handlers.information import PublishNotificationHandler, PublishResourceHandler, EditNotificationHandler, \
    EditResourceHandler,NotificationIndexHandler
from handlers.stuDashboard import MyHomeworkHandler, MyMessagesHandler, ViewHomeworkHandler, RemoveHomeworkHandler, \
    SetCourseHandler, SetCourseListHandler
from handlers.submitAssignment import submitAssgnmentHandler, submitStep2, submitStep3, submitStep4, submitVedio
from handlers.newuser import SignUpHandler, AdminHandler, AuthUserHandler

urls = [
    (r'/', IndexHandler),
    (r'/login', LoginHandler),
    (r'/logout', LogoutHandler),
    (r'/signup', SignUpHandler),

    (r'/notification',NotificationIndexHandler),


    # 教师接口
    (r'/dash/commenting/viewHomework/(.*)', ViewHomeworkHandler),
    (r'/dash/commenting/(.*)', CommentingHandler),
    (r'/dash/commenting', CommentingIndexHandler),
    (r'/dash/editCourse/delete/(.*)', DeleteCourseHandler),
    (r'/dash/editCourse/(.*)', EditingCertainCourseHandler),
    (r'/dash/editCourse', CourseEditHandler),
    (r'/dash/publishing/notification', PublishNotificationHandler),
    (r'/dash/publishing/resource', PublishResourceHandler),
    (r'/dash/editing/notification/(.*)', EditNotificationHandler),
    (r'/dash/editing/resource/(.*)', EditResourceHandler),
    (r'/dash/publishing', PublishEntrenceHandler),
    (r'/dash/allStudents', MyStudentsHandler),
    (r'/dash/notifications', MyNotifHandler),

    # 学生接口
    (r'/dash/setCourse/(.*)', SetCourseHandler),
    (r'/dash/setCourse', SetCourseListHandler),
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
    (r'/Material/Admin/TWF5IEplZmYgRGVhbiBCbGVzcyBNeSBXaWVyZCBXZWIgQXBwbGljYXRpb24=/(.*)', AuthUserHandler),
    (r'/Material/Admin/TWF5IEplZmYgRGVhbiBCbGVzcyBNeSBXaWVyZCBXZWIgQXBwbGljYXRpb24=', AdminHandler),

    # error
    (r'/.*', ErrorHandler),
]
