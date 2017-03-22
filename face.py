#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@time: 2016/9/26 17:56
@author: Silence
'''
import web
import getinfo
import time

urls = (
    '/','Index'

)

render = web.template.render('templates')#参数是模板文件存放路径

class Index(object):
    def GET(self):
        return render.face()
    def POST(self):
        info = web.input()
        print info
        path = info.get('path', None)
        if path != None:
            path = 'http://img15.3lian.com/2015/f2/94/d/44.jpg'
            faceInfo = getinfo.face(path)
            text = u'年龄：%s<br>性别：%s<br>微笑指数：%s<br>患病指数：20%%' %(faceInfo[1],faceInfo[0],faceInfo[2])

            return text
        else:
            imgfile = web.input().get('file')
            imgpath = 'static/images/%s.jpg' %time.time()
            open(imgpath,'wb').write(imgfile)

            return render.face(imgpath)


if __name__ == '__main__':
    app = web.application(urls,globals())
    application = app.wsgifunc()