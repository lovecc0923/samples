# -*- coding: UTF-8 -*-
'''
Created on 2014年6月16日

@author: Administrator
'''

import utils, Test, time

def getMsgList(access_token, userId):
    uri = "/circle/msg/list"
    params = {}
    params['access_token'] = access_token
    params['userId'] = userId
    params['pageIndex'] = 0
    params['pageSize'] = 10
    
    utils.httpInvoke(uri, params)

def getSquareMsgList():
    uri = "/circle/msg/square"
    params = {}
    params['pageIndex'] = 0
    params['pageSize'] = 15
    
    utils.httpInvoke(uri, params)
    
def getUserMsgList(access_token, userId):
    uri = "/circle/msg/user"
    params = {}
    params['access_token'] = access_token
    params['userId'] = userId
    params['pageIndex'] = 0
    params['pageSize'] = 10
    
    utils.httpInvoke(uri, params)

def getMsg(access_token, messageId):
    uri = "/circle/msg/get"
    params = {}
    params['access_token'] = access_token
    params['messageId'] = messageId
    
    utils.httpInvoke(uri, params)



def getCommentList(access_token, messageId):
    uri = '/circle/msg/comment/list'
   
    params = {}
    params['access_token'] = access_token
    params['messageId'] = messageId
    params['pageIndex'] = 0
    params['pageSize'] = 5
    
    utils.httpInvoke(uri, params)

def addMsg(access_token, bodyType, flag, text, images, videos, audios):
    uri = '/circle/msg/add'
    
    params = {}
    params['access_token'] = access_token
    params['type'] = bodyType
    params['flag'] = flag
    params['visible'] = 3
    params['text'] = text
    params['images'] = images
    params['videos'] = videos
    params['audios'] = audios
    
    utils.httpInvoke(uri, params)
def addComment(access_token, messageId, body):
    uri = '/circle/msg/comment/add'
    
    params = {}
    params['access_token'] = access_token
    params['messageId'] = messageId
    params['body'] = body
#     params['toUserId'] = ''
#     params['toNickname'] = ''
#     params['toBody'] = ''
    
    utils.httpInvoke(uri, params)
     
def addGift(access_token, messageId):
    uri = '/circle/msg/gift/add'
    
    params = {}
    params['access_token'] = access_token
    params['messageId'] = messageId
    params['gifts'] = '[{goodsId:1,count:2},{goodsId:2,count:3}]'
    
    utils.httpInvoke(uri, params)

def test1():
    for telephone in range (1530, 1536, 1):
        print telephone
#         images = '[{originalUrl: "http://192.168.1.239:8081/images/o/201406/3027f2ab-3ae4-45a6-850b-2232fda210b4.jpg",status: 1,thumbnailUrl: "http://192.168.1.239:8081/images/t/201406/3027f2ab-3ae4-45a6-850b-2232fda210b4.jpg"},{originalUrl: "http://192.168.1.239:8081/images/o/201406/c77c6d70-14a6-4aa8-b571-f91a46d32192.jpg",status: 1,thumbnailUrl: "http://192.168.1.239:8081/images/t/201406/c77c6d70-14a6-4aa8-b571-f91a46d32192.jpg"}]'
        # type：1=文字；2=图片；3=语音；4=视频；5=图片、语音
        addMsg('7353cdd18d5b4eb59b4a9a714a366056', 4, 3, '这个不错哦！！！', '', 'http://192.168.1.239:8081/video/VID_20140519_190116.mp4', '')
def test2():
    for telephone in range (12354, 12360, 1):
        obj = Test.User.UserLogin('2001', 'qqq')
        access_token = obj['data']['access_token'].encode('utf-8')
        # images = '[{originalUrl: "http://192.168.1.239:8081/images/o/201406/3027f2ab-3ae4-45a6-850b-2232fda210b4.jpg",status: 1,thumbnailUrl: "http://192.168.1.239:8081/images/t/201406/3027f2ab-3ae4-45a6-850b-2232fda210b4.jpg"},{originalUrl: "http://192.168.1.239:8081/images/o/201406/c77c6d70-14a6-4aa8-b571-f91a46d32192.jpg",status: 1,thumbnailUrl: "http://192.168.1.239:8081/images/t/201406/c77c6d70-14a6-4aa8-b571-f91a46d32192.jpg"}]'
        # type：1=文字；2=图片；3=语音；4=视频；5=图片、语音
        addMsg(access_token, 4, 3, '这个不错哦！！！%s' % telephone, '', 'http://192.168.1.239:8081/video/VID_20140519_190116.mp4', '')

if __name__ == '__main__':
# test2()
    access_token = Test.User.getAccessToken('2012', 'qqq')
    getSquareMsgList()
    getMsg(access_token, '53b13d58e4b0f3109f9d602f')
    getMsgList(access_token, '')
# access_token = Test.User.getAccessToken('2000', 'qqq')
# addComment(access_token, '53a42944e4b022229de651d3', '我敢你大爷哦！！！')
# # getCommentList(access_token, '53a2a03b45c95483107c64cf')
    
# # getUserMsgList(access_token, 8)
# # getSquareMsgList()
# 
# 
# 
# # addMsg(access_token, 4, 3, '这个不错哦！！！', '', 'http://192.168.1.239:8081/video/VID_20140519_190116.mp4', '')
# # addGift(access_token, '53a7a775e4b0ceca1419e58e')
# start = time.time()
# 
# # addMsg(access_token, 4, 3, '这个不错哦！！！', '', 'http://192.168.1.239:8081/video/VID_20140519_190116.mp4', '')
# 
# 
# addComment(access_token, '53a7a775e4b0ceca1419e58e', '我敢你大爷哦！！！')
# getSquareMsgList()
# 
# end = time.time()
# 
# print (end - start) * 1000
# # getMsgList()
# # 53871464daf87f37e2ea42d1
# 
# getMsg(access_token, '53a42944e4b022229de651d3')
# getCommentList('7353cdd18d5b4eb59b4a9a714a366056', '538695d8daf82d61d2a87aa6')
# 538695d8daf82d61d2a87aa6

