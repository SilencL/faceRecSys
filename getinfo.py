#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
@time: 2016/10/13 15:37
@author: Silence
'''
import urllib2
import json

url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'

def face(imageUrl):
    data = 'api_key=S2WvfVml4punPdrxuFk0fNI7TgFMEAF3&api_secret=iWliw8kmUDpX7_p1wkLTDj2XG0ueTPhw&image_url=%s&return_attributes=gender,age,smiling,headpose,facequality,blur,eyestatus' %imageUrl
    html = urllib2.urlopen(url,data=data).read()
    html = json.loads(html)
    gender = html['faces'][0]['attributes']['gender']['value']
    age = html['faces'][0]['attributes']['age']['value']
    smile = html['faces'][0]['attributes']['smile']['value']
    # print smile
    return gender,age,smile

if __name__ == '__main__':
    print face('https://imgsa.baidu.com/baike/c0%3Dbaike150%2C5%2C5%2C150%2C50/sign=eff8a637dd3f8794c7f2407cb3726591/faedab64034f78f08a8bdf7c70310a55b2191cb8.jpg')