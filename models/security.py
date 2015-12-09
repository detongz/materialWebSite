# coding: utf-8


def clean(s):
    """防止sql注入，去除关键字"""
    dirty_stuff = ["\"", "\\", "/", "*", "'", "=", "-", "#", ";", "<", ">", "+", "%"]
    for stuff in dirty_stuff:
        if s.find(stuff) >= 0:
            s = s.replace(stuff, "")
    return s


def cleanLink(s):
    """清洗文件分享链接"""
    dirty_stuff = ["\"", "\\", "*", "'", "-", "#", ";", "<", ">", "+", "%"]
    for suff in dirty_stuff:
        if s.find(suff) >=0:
            s=s.replace(suff,"")
    return s