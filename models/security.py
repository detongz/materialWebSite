# coding: utf-8
import sys

reload(sys)
sys.setdefaultencoding('utf-8')


def clean(s):
    """防止sql注入，去除关键字"""
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%"]
    for stuff in dirty_stuff:
        if s.find(stuff) >= 0:
            s = s.replace(stuff, "")
    return s.decode('utf-8')


def cleanLink(s):
    """清洗文件分享链接"""
    dirty_stuff = ["\"", "\\", "*", "'", "-", "#", ";", "<", ">", "+", "%"]
    for suff in dirty_stuff:
        if s.find(suff) >= 0:
            s = s.replace(suff, "")
    return s.decode('utf-8')


def text2Html(content):
    def escape(txt):
        """将txt文本中的空格、&、<、>、（"）、（'）转化成对应的的字符实体，以方便在html上显示"""
        txt = txt.replace('&', '&#38;')
        txt = txt.replace(' ', '&#160;')
        txt = txt.replace('<', '&#60;')
        txt = txt.replace('>', '&#62;')
        txt = txt.replace('"', '&#34;')
        txt = txt.replace('\'', '&#39;')
        return txt

    content = escape(content)
    lines = content.split('\n')
    for i, line in enumerate(lines):
        lines[i] = '<p>' + line + '</p>'
    content = ''.join(lines)
    return content


def html2Text(content):
    def escape(txt):
        """将数据库中的html标签去掉，仅仅留下txt文档"""
        txt = txt.replace('&#38;', '&')
        txt = txt.replace('&#160;', ' ')
        txt = txt.replace('&#60;', '<')
        txt = txt.replace('&#62;', '>')
        txt = txt.replace('&#34;', '"')
        txt = txt.replace('&#39;', '\'')
        return txt

    content = escape(content)
    lines = content.split('</p>')
    for i, line in enumerate(lines):
        lines[i] = line.strip('<p>').strip('<br>').strip('<\p>') + '\n'
    content = ''.join(lines)
    return content
