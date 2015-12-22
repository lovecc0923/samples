# -*- coding: UTF-8 -*-
'''
Created on 2014年6月27日

@author: luorc
'''

import utils, Test, thread, json
import TestUser

class BCircle(object):
    
    def __init__(self):
        pass

    @staticmethod
    def addMsg(access_token, bType, flag, text, images, videos, audios):
        uri = '/b/circle/msg/add'
        
        params = {}
        params['access_token'] = access_token
        params['type'] = bType
        params['flag'] = flag
        params['visible'] = 3
        params['title'] = 'title'
        params['text'] = text
        params['address'] = 'address'
        params['remark'] = 'remark'
        params['time'] = utils.timestamp()
        params['images'] = images
        params['videos'] = videos
        params['audios'] = audios
        
        params['model'] = 'Windows 7'
        params['osVersion'] = '123456'
        params['serial'] = '123456'
        params['latitude'] = '123456'
        params['longitude'] = '123456'
        params['location'] = 'location'

        utils.httpInvoke(uri, params)

    @staticmethod
    def getMsg(access_token, messageId):
        uri = "/b/circle/msg/get"
        params = {}
        params['access_token'] = access_token
        params['messageId'] = messageId
        
        utils.httpInvoke(uri, params)
    
    @staticmethod
    def getMsgList(access_token, userId, messageId):
        uri = "/b/circle/msg/list"
        params = {}
        params['access_token'] = access_token
        params['userId'] = userId
        params['messageId'] = messageId
        params['pageSize'] = 10
        
        utils.httpInvoke(uri, params)
    
    @staticmethod
    def getSquareMsgList(messageId, pageSize):
        uri = "/b/circle/msg/square"
        params = {}
        params['messageId'] = messageId
        params['pageSize'] = pageSize
        
        return utils.httpInvoke(uri, params)
    
    @staticmethod
    def getMsgHotList(messageId, pageSize):
        uri = "/b/circle/msg/hot"
        params = {}
        params['messageId'] = messageId
        params['cityId'] = 440300
        
#         params['pageSize'] = pageSize
#         params['pageSize'] = pageSize
        
        return utils.httpInvoke(uri, params)
     
    @staticmethod   
    def getUserMsgList(access_token, userId):
        uri = "/b/circle/msg/user"
        params = {}
        params['access_token'] = access_token
        params['userId'] = userId
        params['pageIndex'] = 0
        params['pageSize'] = 10
        
        return utils.httpInvoke(uri, params)
        
    @staticmethod   
    def addComment(access_token, messageId, body):
        uri = '/b/circle/msg/comment/add'
        
        params = {}
        params['access_token'] = access_token
        params['messageId'] = messageId
        params['body'] = body
    #     params['toUserId'] = ''
    #     params['toNickname'] = ''
    #     params['toBody'] = ''
        
        utils.httpInvoke(uri, params)

    @staticmethod
    def deleteComment(access_token, messageId, commentId):
        uri = '/b/circle/msg/comment/delete'
       
        params = {}
        params['access_token'] = access_token
        params['messageId'] = messageId
        params['commentId'] = commentId
        
        utils.httpInvoke(uri, params)
   
    @staticmethod
    def getCommentList(access_token, messageId, commentId):
        uri = '/b/circle/msg/comment/list'
       
        params = {}
        params['access_token'] = access_token
        params['messageId'] = messageId
        params['commentId'] = commentId
        params['pageSize'] = 5
        
        utils.httpInvoke(uri, params)
    
    @staticmethod
    def addPraise(access_token, messageId):
        uri = '/b/circle/msg/praise/add'
        
        params = {}
        params['access_token'] = access_token
        params['messageId'] = messageId
        
        utils.httpInvoke(uri, params)  

    @staticmethod
    def getPraiseList(access_token, messageId, praiseId):
        uri = '/b/circle/msg/praise/list'
       
        params = {}
        params['access_token'] = access_token
        params['messageId'] = messageId
        params['_id'] = praiseId
        params['pageSize'] = 5
        
        utils.httpInvoke(uri, params)

    @staticmethod     
    def addGift(access_token, messageId):
        uri = '/b/circle/msg/gift/add'
        
        params = {}
        params['access_token'] = access_token
        params['messageId'] = messageId
        params['gifts'] = '[{goodsId:1,count:2},{goodsId:2,count:3}]'
        
        utils.httpInvoke(uri, params)

    @staticmethod
    def getGiftList(access_token, messageId, giftId):
        uri = '/b/circle/msg/gift/list'
       
        params = {}
        params['access_token'] = access_token
        params['messageId'] = messageId
        params['_id'] = giftId
        params['pageSize'] = 5
        
        utils.httpInvoke(uri, params)
        
    @staticmethod
    def getMsgIdList(access_token):
        uri = '/b/circle/msg/ids'
       
        params = {}
        params['access_token'] = access_token
        
        utils.httpInvoke(uri, params)
        
    @staticmethod
    def getMsgListByIds(access_token, ids):
        uri = '/b/circle/msg/gets'
       
        params = {}
        params['access_token'] = access_token
        params['ids'] = ids
        
        utils.httpInvoke(uri, params)
def test1():
    for telephone in range (1530, 1536, 1):
        print telephone
#         images = '[{originalUrl: "http://192.168.1.239:8081/images/o/201406/3027f2ab-3ae4-45a6-850b-2232fda210b4.jpg",status: 1,thumbnailUrl: "http://192.168.1.239:8081/images/t/201406/3027f2ab-3ae4-45a6-850b-2232fda210b4.jpg"},{originalUrl: "http://192.168.1.239:8081/images/o/201406/c77c6d70-14a6-4aa8-b571-f91a46d32192.jpg",status: 1,thumbnailUrl: "http://192.168.1.239:8081/images/t/201406/c77c6d70-14a6-4aa8-b571-f91a46d32192.jpg"}]'
        # type：1=文字；2=图片；3=语音；4=视频；5=图片、语音
        BCircle.addMsg('7353cdd18d5b4eb59b4a9a714a366056', 4, 3, '这个不错哦！！！', '', 'http://192.168.1.239:8081/video/VID_20140519_190116.mp4', '')

# def test2():
#     for telephone in range (12354, 12360, 1):
#         obj = Test.User.UserLogin('2001', 'qqq')
#         access_token = obj['data']['access_token'].encode('utf-8')
#         # images = '[{originalUrl: "http://192.168.1.239:8081/images/o/201406/3027f2ab-3ae4-45a6-850b-2232fda210b4.jpg",status: 1,thumbnailUrl: "http://192.168.1.239:8081/images/t/201406/3027f2ab-3ae4-45a6-850b-2232fda210b4.jpg"},{originalUrl: "http://192.168.1.239:8081/images/o/201406/c77c6d70-14a6-4aa8-b571-f91a46d32192.jpg",status: 1,thumbnailUrl: "http://192.168.1.239:8081/images/t/201406/c77c6d70-14a6-4aa8-b571-f91a46d32192.jpg"}]'
#         # type：1=文字；2=图片；3=语音；4=视频；5=图片、语音
#         BCircle.addMsg(access_token, 1, 3, '新商务圈改造完毕，视频是测试效果！！！', '', 'http://192.168.1.240:8081/video/VID_20140519_190116.mp4', '')

def singleUserMultiMsg():
    access_token = Test.User.getAccessToken('2012', 'qqq')
    for i in range(84855, 100000):
        print i
        BCircle.addMsg(access_token, 1, 3, '%s新商务圈改造完毕，视频是测试效果！！！%s' % (i, i), '', '["http://192.168.1.240:8081/video/VID_20140519_190116.mp4"]', '')

def multiUserSingleMsg():
    for telephone in range(2000, 2100):
        access_token = Test.User.getAccessToken('%s' % telephone, 'qqq')
        BCircle.addMsg(access_token, 1, 3, '%s多用户单消息测试%s' % (telephone, telephone), '', '["http://192.168.1.240:8081/video/VID_20140519_190116.mp4"]', '')

def pageTest():
    BCircle.getSquareMsgList('', 10)
    BCircle.getSquareMsgList('', 5)
    BCircle.getSquareMsgList('53ad627745c9c9a69b28066b', 5)
    
def multi_praise(messageId):
    for telephone in range(2001, 2057):
        access_token = Test.User.getAccessToken('%s' % telephone, 'qqq')
        BCircle.addPraise(access_token, messageId)
        
def multi_comment(access_token, messageId, size):
    for i in range(10000, 10000 + size, 1):
        BCircle.addComment(access_token, messageId, '%sNice%s' % (i, i))


def timer(no, interval):  
        # cnt = 0  
        # while cnt < 10:  
        #    print 'Thread:(%d) Time:%s\n' % (no, time.ctime())  
        #    time.sleep(interval)  
        #    cnt += 1  
        
#         thread.exit_thread()
    try:
        BCircle.getSquareMsgList('', 5)
        thread.exit_thread()
    except Exception, e:
        print e

def test2():
    for i in range(0, 2000, 1):
        print i
        thread.start_new_thread(timer, (1, 1))
     
    while True:
        pass
  
if __name__ == '__main__':
    access_token = Test.User.getAccessToken('18908983800', 'qqq')
    BCircle.getMsgList(access_token, '', '');
# http://localhost:8080/mianshi-api/api/v1/b/circle/msg/gift/gbgift?access_token=0c4370fe461a48d8a0de8eaae442da04&messageId=53d544a2c443f0470ea4d0cc
# http://localhost:8080/mianshi-api/api/v1/b/circle/msg/gift/gbuser?access_token=0c4370fe461a48d8a0de8eaae442da04&messageId=53d544a2c443f0470ea4d0cc
#     test2()
#     singleUserMultiMsg()
#     
#     access_token = Test.User.getAccessToken('18908983800', '274314')
#     BCircle.addPraise(access_token, '5408478ee4b0524b6e448d03')
#     BCircle.getMsg(access_token, '53d9aff0e4b0b9e205148de7')
#     BCircle.addGift(access_token, '53d544a2c443f0470ea4d0cc')
#     access_token = Test.User.getAccessToken('100730', 'qqq')
#     BCircle.addGift(access_token, '53d544a2c443f0470ea4d0cc')
#     access_token = Test.User.getAccessToken('100731', 'qqq')
#     BCircle.addGift(access_token, '53d544a2c443f0470ea4d0cc')
#     BCircle.addMsg(access_token, 1, 3, '%s我TM可以干你大爷不？%s' % (2012, 2012), '', '["http://192.168.1.240:8081/video/VID_20140519_190116.mp4"]', '')
#     singleUserMultiMsg()
#     multiUserSingleMsg()

#     pageTest()
#     praiseTest('53ad627745c9c9a69b28066f')

#     BCircle.getMsg(access_token, '53b550b645c9a91afa67b465')
#     BCircle.addGift(access_token, '53b550b645c9a91afa67b465')
#     addComment(access_token, '53b550b645c9a91afa67b465', '大家好')
#     BCircle.getCommentList(access_token, '53b550b645c9a91afa67b465', '')
#     BCircle.getGiftList(access_token, '53b550b645c9a91afa67b465', '')
#     for i in range(10000, 10034, 1):
#         BCircle.addComment(access_token, '53b550b645c9a91afa67b465', '%s很不錯哦！！！%s' % (i, i))
#     singleUserMultiMsg()
#     multiUserSingleMsg()//84855

#     BCircle.addMsg(access_token, 1, 3, '%saaaaaaaaadfadsfadsgad%s' % (2012, 2012), '', '["http://192.168.1.240:8081/video/VID_20140519_190116.mp4"]', '')
    
#     multi_comment(access_token, '53bb5364e4b0ea03991c73b4', 34)
    
#     BCircle.getSquareMsgList('', 50)

    
#     BCircle.addPraise(access_token, '53b6740aaaa71a40c241938b')
#     BCircle.getMsgList(access_token, '', '')
#     BCircle.getPraiseList(access_token, '53b6740aaaa71a40c241938b', '')
#     BCircle.getCommentList(access_token, '53b6740aaaa71a40c241938b', '')
#     BCircle.getCommentList(access_token, '53b6740aaaa71a40c241938b', '53b69fa6e4b097fc664187ee')

#     msgList = json.loads(BCircle.getSquareMsgList('', 100))
#     for msg in msgList['data']:
#         multi_comment(access_token, msg['messageId'].encode('utf-8') , 200)
#     access_token = Test.User.getAccessToken('100729', 'qqq')
#     BCircle.getCommentList(access_token, '53bba86491685d0534dabcd0', '')

#     access_token = Test.User.getAccessToken('100729', 'qqq')
#     BCircle.getMsgList(access_token, '', '')
#     BCircle.getMsgIdList(access_token)
# #     BCircle.getMsg(access_token, '53bbcdc9e4b08a5650e234fe')
#     BCircle.getMsgListByIds(access_token, '["53bbb6e091685d1deca4c67b","53bbb6e091685d1deca4c617"]')
#     BCircle.getMsgHotList('', 50)
#     BCircle.getSquareMsgList('', 50)


#     BCircle.getUserMsgList(access_token, userId)
#     access_token = Test.User.getAccessToken('18503054765', '123456')
#     BCircle.getUserMsgList(access_token, '')
#     
#     BCircle.getMsgIdList(access_token)
#     BCircle.getMsgListByIds(access_token, '["54252f2aa310caf83a822ba5","5425224fa310caf83a822ba3","5422afbaa310b7e74204f477","5422aed1a310b7e74204f475"]')
