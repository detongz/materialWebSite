# coding: utf-8

from base.base import BaseHandler
from dash import is_loged
from models.notification import get_info_by_infoid, publish_notif, publish_res, get_info, update_notif, get_all_notif,\
            get_info_by_infoid_all, delete_notif
from models.security import html2Text,clean
from information import generateInfoid

import commands
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


class UploadImageForInfoHandler(BaseHandler):
    """消息通知上传图片文件"""

    def post(self):
        gp, uid = is_loged(self)
        if gp == 't':
            Iid = infoIdState(self)
            fname = self.request.files['upload'][0].filename

            import os
            dirpath = os.path.dirname(__file__)[:-8] + 'static/notif/'

            # 生成pic文件名
            import random
            filename = Iid + str(random.randint(99, 1000)) +'.'+ fname.split('.')[-1]
            while True:
                cmd = 'find %s -name "%s"' % (dirpath,clean(filename))
                if not commands.getstatusoutput(cmd)[1]:
                    break
                filename = Iid + str(random.randint(99, 1000)) + fname.split('.')[-1]

            f = self.request.files['upload'][0].body

            savefile = open(dirpath+filename,'w')
            savefile.write(f)
            savefile.close()

            callback = self.get_argument('CKEditorFuncNum')

            self.write('''
                <script type="text/javascript">
                    window.parent.CKEDITOR.tools.callFunction("%s","%s",'');
                </script>
            '''% (callback,'/static/notif/'+filename))


def infoIdState(request):
    """获取cookie中的iid值"""

    iid = request.get_secure_cookie('Iid')
    if not iid:
        iid = generateInfoid()
        request.set_secure_cookie('Iid',iid)
    return iid
