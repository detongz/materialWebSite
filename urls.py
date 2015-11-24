# coding:utf-8
import tornado.web
from handler.index import indexHandler
from handler.loginOut import loginHandler, logoutHandler
from handler.courseInfo import courseInfoHandler, courseinfoTeachersHandler, teacherIntorduction, createCourseHandler
from handler.user import userInfoHandler, updateCourseStateHandler, CourseHistoryHandler, allStudentsHandler, \
    courseToBeStarted, viewStudentDetails, changeProfileHandler, teacherSetting, teacherSetPic, teacherSetIntorduction
from handler.signUp import signUpHandler, signUpHandlerTeacher
from handler.homeworks import myHomework, uploadHomework, getHomework, stuHomeworkDetail, stuHomeworkPicPreview, \
    commentingHandler, markingHandler, setFormHandler, chooseSubmitHandler, assignedTypeHandler, uploadVideo, \
    stuHomeworkVideoPreview, homeworkTypeHandler, homeworkTypeHandlerTeacher
from handler.resourse import resourseHandler, notificationIndexHandler, chooseInfoToPostHandler, publishResources, \
    publishNotification, resourseDetailHandler, notificationDetailHandler

urls = [
    (r'/', indexHandler),
    (r'/index', indexHandler),
    (r'/login', loginHandler),
    (r'/logout', logoutHandler),
    (r'/courseInfo', courseInfoHandler),
    (r'/courseInfo-teachers', courseinfoTeachersHandler),
    (r'/courseInfo/teacher/(.*)', teacherIntorduction),
    (r'/user', userInfoHandler),
    (r'/user/updateCourse/(.*)', updateCourseStateHandler),
    (r'/user/CourseHistory', CourseHistoryHandler),
    (r'/user/AllStudents', allStudentsHandler),
    (r'/user/courseToStart', courseToBeStarted),
    (r'/user/myHomework', myHomework),
    (r'/user/upload/(.*)', uploadHomework),
    (r'/user/uploadvideo/(.*)', uploadVideo),
    (r'/user/chooseSubmit', chooseSubmitHandler),
    (r'/user/homeworktype/(.*)_(.*)', assignedTypeHandler),
    (r'/user/viewhomeworktype/(.*)_(.*)', homeworkTypeHandler),
    (r'/user/viewhomeworktypeTeacher/(.*)_(.*)_(.*)', homeworkTypeHandlerTeacher),
    (r'/signUp', signUpHandler),
    (r'/signUp/teacher', signUpHandlerTeacher),
    (r'/createCourse', createCourseHandler),
    (r'/assignment/(.*)', getHomework),
    (r'/viewAssignment/(.*)_(.*)', stuHomeworkDetail),
    (r'/previewImages/(.*)_(.*)', stuHomeworkPicPreview),
    (r'/previewVideo/(.*)_(.*)', stuHomeworkVideoPreview),
    (r'/student/(.*)', viewStudentDetails),
    (r'/commenting/(.*)_(.*)', commentingHandler),
    (r'/mark/(.*)', markingHandler),
    (r'/setForm/(.*)', setFormHandler),
    (r'/changeProfile', changeProfileHandler),
    (r'/user/publish', chooseInfoToPostHandler),
    (r'/user/publish/notifications', publishNotification),
    (r'/user/publish/resources', publishResources),
    (r'/notifications', notificationIndexHandler),
    (r'/notifications/detail/(.*)', notificationDetailHandler),
    (r'/resource', resourseHandler),
    (r'/resource/detail/(.*)', resourseDetailHandler),
    (r'/Material/user/teacher/setting/info', teacherSetting),
    (r'/Material/user/teacher/setting/picture/(.*)', teacherSetPic),
    (r'/Material/user/teacher/setting/introduction/(.*)', teacherSetIntorduction),
]
