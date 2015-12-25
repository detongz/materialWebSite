# coding: utf-8
from base.base import BaseHandler
from models.course import get_teacher_course, get_teacher_course_delete, new_course, get_course
from models.student import get_my_student
from models.homework import get_teacher_homework, get_homework, update_comment
from models.notification import get_teacher_notif
from models.security import html2Text
from dash import is_loged
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class CourseEditHandler(BaseHandler):
    """教师编辑课程首页"""

    def get(self):
        gp, uid = is_loged(self)

        if gp == 't':
            self.render('teacher_edit_course.html', id=uid, active='dsh', active_slide='mycourse',
                        course=get_teacher_course(uid), delete=get_teacher_course_delete(uid))
        else:
            self.redirect('/404')

    def post(self, *args, **kwargs):
        """教师新增课程"""

        gp, uid = is_loged(self)

        if gp == 't':
            cid = self.get_argument('cid')
            year = self.get_argument('year')
            start_week = int(self.get_argument('sw'))
            end_week = int(self.get_argument('ew'))

            if end_week > 20 or end_week < start_week or not (0 < start_week < 18):
                self.render('error.html', title='输入错误', content='周数输入有误<br><br>请重新输入', icon='ion-alert-circled',
                            active='dsh', id=uid)
            elif get_course(cid) is not None:
                self.render('error.html', title='输入错误', content='课序号已经存在<br><br>请删除相应课程后在进行创建新课程的操作',
                            icon='ion-alert-circled', active='dsh', id=uid)
            else:
                try:
                    new_course(uid, cid, year, str(start_week), str(end_week))
                    self.render('error.html', title='操作成功', content='课程创建成功', icon='ion-checkmark-circled',
                                active='dsh', id=uid)
                except Exception as e:
                    print e
                    self.render('error.html', title=None, content=None, icon='ion-bug', active='dsh', id=uid)


class EditingCertainCourseHandler(BaseHandler):
    """教师编辑特定课程页面"""

    def get(self, cid):
        gp, uid = is_loged(self)
        if gp == 't':
            self.write('haha')  # 测试消息
        else:
            self.redirect('/404')


class DeleteCourseHandler(BaseHandler):
    """教师编辑特定课程页面"""

    def get(self, cid):
        gp, uid = is_loged(self)
        if gp == 't':
            self.write('haha')  # 测试消息
        else:
            self.redirect('/404')


class MyStudentsHandler(BaseHandler):
    """获取教师所有学生"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.render('teacher_my_students.html', id=uid, active='dsh', active_slide='allstu',
                        stu=get_my_student(uid))
        else:
            self.redirect('/404')


class MyNotifHandler(BaseHandler):
    """获取教师发布的消息"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.render('teacher_my_notifications.html', id=uid, active='dsh', active_slide='ntfc',
                        info=get_teacher_notif(uid))
        else:
            self.redirect('/404')


class CommentingIndexHandler(BaseHandler):
    """教师评价作业首页"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.render('teacher_commenting.html', id=uid, active='dsh', active_slide='cmt',
                        homework=get_teacher_homework(uid))
        else:
            self.redirect('/404')


class CommentingHandler(BaseHandler):
    """教师评价某位同学某的次作业"""

    def get(self, hid):
        gp, uid = is_loged(self)

        if gp == 't':

            self.clear_cookie('Iid')
            self.set_secure_cookie('Iid',hid)

            h = get_homework(hid)
            comment = h['comment']
            self.render('teacher_cmt_homework.html', id=uid, active='dsh', active_slide='cmt', hid=hid, comment=comment)

        else:
            self.redirect('/404')

    def post(self, hid):
        gp, uid = is_loged(self)
        if gp == 't':
            comment = self.get_argument('comment')

            try:
                update_comment(hid, comment)
                self.render('error.html', title='评价成功', content='您对这次作业已经评价过了！', icon='ion-checkmark-circled',
                            active='dsh', id=uid)

            except Exception as e:
                print(e)

            finally:
                self.clear_cookie('Iid')


class PublishEntrenceHandler(BaseHandler):
    """教师选择发布新消息的类型"""

    def get(self, *args, **kwargs):
        gp, uid = is_loged(self)
        if gp == 't':
            self.render('teacher_publish_entrence.html', id=uid, active='dsh', active_slide='ntfc')
        else:
            self.redirect('/404')
