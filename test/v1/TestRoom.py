# -*- coding: UTF-8 -*-
'''
Created on 2014年6月24日

@author: luorc
'''

import Test, utils

def roomAdd(access_token):
    uri = '/room/add'
    params = {}
    params['access_token'] = access_token
    params['name'] = '大房间'
    params['desc'] = '这是个大房间'
    utils.httpInvoke(uri, params)
    
def roomList(access_token):
    uri = '/room/list'
    params = {}
    params['access_token'] = access_token
    utils.httpInvoke(uri, params)
    
def roomGet(access_token, roomId):
    uri = '/room/get'
    params = {}
    params['access_token'] = access_token
    params['roomId'] = roomId
    utils.httpInvoke(uri, params)


def addMember(access_token, roomId, userId):
    uri = '/room/member/update'
    params = {}
    params['access_token'] = access_token
    params['roomId'] = '54d49a846aa3b6ef83b60a46'
    params['userId'] = userId
    params['role'] = 1
    utils.httpInvoke(uri, params)
    
def deleteMember(access_token, roomId, userId):
    uri = '/room/member/delete'
    params = {}
    params['access_token'] = access_token
    params['roomId'] = '54d49a846aa3b6ef83b60a46'
    params['userId'] = userId
    utils.httpInvoke(uri, params)
    
def getMember(access_token, roomId, userId):
    uri = '/room/member/get'
    params = {}
    params['access_token'] = access_token
    params['roomId'] = roomId
    params['userId'] = userId
    utils.httpInvoke(uri, params)
    
def getMemberList(access_token, roomId):
    uri = '/room/member/list'
    params = {}
    params['access_token'] = access_token
    params['roomId'] = roomId
    utils.httpInvoke(uri, params)
    
if __name__ == '__main__':
    pass
# Test.User.UserRegister('18908983803', '123456')
# 

# addMember('2fa4229766cd4f278ebd060ddbb03d3d', '1', 100101)

#     uri = '/room/list/his'
#     params = {}
#     params['access_token'] = Test.User.getAccessToken('18503054765', '123456')
#     params['type'] = 1
#     utils.httpInvoke(uri, params)
#     
    access_token = Test.User.getAccessToken('15015168186', '123456')
#     uri = '/room/list'
#     params = {}
#     params['access_token'] = Test.User.getAccessToken('15015168186', '123456')
#     params['type'] = 1
#     utils.httpInvoke(uri, params)
    roomGet(access_token, '55d3e28ce4b0e7560faa6e68')

#     uri = '/room/update'
#     params = {}
#     params['access_token'] = Test.User.getAccessToken('18503054765', '123456')
#     params['roomId'] = '5514c72e5b92949b5ca8de28'
#     params['notice'] = '哈哈哈哈'
#     utils.httpInvoke(uri, params)

#     access_token = Test.User.getAccessToken('18908983801', '123456')
#     uri = '/nearby/user'
#     params = {}
#     params['access_token'] = access_token
#     params['longitude'] = 114.054799
#     params['latitude'] = 22.607759
#     
#     utils.httpInvoke(uri, params)



# getMember(access_token, '54d49a846aa3b6ef83b60a46', 10000001)
# getMember(access_token, '54d49a846aa3b6ef83b60a46', 100102)

# getMemberList(access_token, '54d49a846aa3b6ef83b60a46')
# access_token = Test.User.getAccessToken('18908983801', '123456')

# addMember(access_token, '54d49a846aa3b6ef83b60a46', 10000001)
# deleteMember(access_token, '54d49a846aa3b6ef83b60a46', 10000001)

# roomGet(access_token, '54d49a846aa3b6ef83b60a46')

# roomList(access_token)
# roomAdd(access_token)
# uri = '/room/update'
# params = {}
# params['access_token'] = access_token
# params['roomId'] = '54d49a846aa3b6ef83b60a46'
# params['sub'] = 0
# params['talkTime'] = 123
# utils.httpInvoke(uri, params)

# uri = '/room/delete'
# params = {}
# params['access_token'] = access_token
# params['roomId'] = '54d490106aa3b6ef83b60a45'
# utils.httpInvoke(uri, params)






# 
# uri = '/exam_goods/buy'
# params = {}
# params['access_token'] = access_token
# params['text'] = '[15]'
# utils.httpInvoke(uri, params)

# get()
# access_token = Test.User.getAccessToken('18503054766', '123456')
# goodsList(access_token)


# uri = '/pay_goods/buy'
# params = {}
# params['access_token'] = access_token
# params['rechargeType'] = 2
# params['goodsId'] = 2
#           
# utils.httpInvoke(uri, params)

# buyBizGoods()
# buyBizGoods2()


# Test.Company.jobList(access_token)
# Test.Company.examList(access_token)
# Test.Goods.goodsList(access_token)



# uri = '/pay/callback'
# params = {}
# params['access_token'] = access_token
# params['nickname'] = '97'
# params['pageSize'] = 10
#        
# utils.httpInvoke(uri, params)













