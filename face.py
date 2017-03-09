#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@time: 2016/9/26 17:56
@author: Silence
'''
import web
import getinfo

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
        open('static/images/1.jpg', 'wb').write(info.get('file'))
        return render.face('../static/images/1.jpg')
        # if info.get('file'):
        #     open('static/images/1.jpg', 'wb').write(info.get('file'))
        #     return render.face1('static/images/1.jpg')
        # else:
        #     return getinfo.face1('http://www.litianqiang.com/static/images/qz.jpg')

if __name__ == '__main__':
    web.application(urls,globals()).run()