#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@time: 2016/10/13 15:37
@author: Silence
'''
import urllib

def face(url):
    return urllib.urlopen('http://apicn.faceplusplus.com/v2/detection/detect?api_key=ef93c355170b75a4b101d0189ef1a9c9&api_secret=auL84a5x4raou8TP6mJOOKzWhivVyPYP&url=%s&attribute=glass,pose,gender,age,race,smiling' %url).read()

if __name__ == '__main__':
    print face('http://www.litianqiang.com/static/images/qz.jpg')