# -*- coding: UTF-8 -*-
'''
Created on 2014年7月8日

@author: luorc
'''

import pymongo, time
from bson.objectid import ObjectId

mongo = pymongo.Connection('121.37.30.15', 27017)
db = mongo.mianshi
message = db.message

def createMsg(userId, nickname):
    dbObj = {}
    dbObj['_id'] = ObjectId()
    dbObj['userId'] = userId
    dbObj['nickname'] = nickname
    dbObj['flag'] = 3
    dbObj['visible'] = 3
    dbObj['body'] = createBody(userId)
    dbObj['count'] = createCount()
    dbObj['time'] = int(time.time())
    dbObj['model'] = 'CentOS 6.5'
    dbObj['latitude'] = 111111
    dbObj['longitude'] = 222222
    dbObj['location'] = '测试地址'

    return dbObj
def createImageList():
    image1 = {}
    image1['oUrl'] = 'http://192.168.1.240/image/t/201407/fe917e8b-ce01-4d59-be1b-28979e2cf1ac.jpg'
    image1['tUrl'] = 'http://192.168.1.240/image/t/201407/fe917e8b-ce01-4d59-be1b-28979e2cf1ac.jpg'
    image2 = {}
    image2['oUrl'] = 'http://192.168.1.240/image/t/201407/750eaa13-e048-41d8-bc47-69a3aa6129ad.jpg'
    image2['tUrl'] = 'http://192.168.1.240/image/t/201407/750eaa13-e048-41d8-bc47-69a3aa6129ad.jpg'
    
    return [image1, image2]
def createBody(userId):
    
    dbObj = {}
    dbObj['title'] = '测试标题'
    dbObj['text'] = '%s测试文字%s' % (time.time(), userId)
    dbObj['type'] = 4
    dbObj['images'] = createImageList()
    dbObj['audios'] = []
    dbObj['videos'] = ["http://192.168.1.240/video/201407/8a5a6b00-bf6a-4510-ac22-d03690e8f8dd.mp4"]
    dbObj['time'] = int(time.time())
    dbObj['address'] = '测试地址'
    dbObj['remark'] = '测试备注'
    
    return dbObj

def createCount():
    dbObj = {}
    dbObj['play'] = 0
    dbObj['forward'] = 0
    dbObj['share'] = 0
    dbObj['collect'] = 0
    dbObj['praise'] = 0
    dbObj['commnet'] = 0
    dbObj['money'] = 0
    dbObj['total'] = 0
    
    return dbObj

def createMsgList():
    msgList = []
    
#     for i in range(100729, 100829):
    for i in range(100729, 100829):
        userId = i
        nickname = '测试昵称%s' % i
        msgList.append(createMsg(userId, nickname))
    
    return msgList

if __name__ == '__main__':
    for i in range(0, 100, 1):
        msgList = createMsgList()
        message.insert(msgList)
        
