# -*- coding: UTF-8 -*-
'''
Created on 2014年6月16日

@author: Administrator
'''
import utils, Test

def attentionList(access_token):
    uri = '/friends/attention/list'
    params = {}
    params['access_token'] = access_token
    
    utils.httpInvoke(uri, params)
    
def fansList(access_token):
    uri = '/friends/fans/list'
    params = {}
    params['access_token'] = access_token
    
    utils.httpInvoke(uri, params)
    
def friendsDelete(access_token, toUserId):
    uri = '/friends/delete'
    params = {}
    params['access_token'] = access_token
    params['toUserId'] = toUserId
    
    utils.httpInvoke(uri, params)
def friendsAdd(access_token, toUserId):
    uri = '/friends/attention/add'
    
    params = {}
    params['access_token'] = access_token
    params['toUserId'] = toUserId
    
    utils.httpInvoke(uri, params)
    
def attentionAdd(access_token, toUserId):
    uri = '/friends/attention/add'
    
    params = {}
    params['access_token'] = access_token
    params['toUserId'] = toUserId
    
    utils.httpInvoke(uri, params)
    
def remark(access_token, toUserId, remarkName):
    uri = '/friends/remark'
    
    params = {}
    params['access_token'] = access_token
    params['toUserId'] = toUserId
    params['remarkName'] = remarkName
    
    utils.httpInvoke(uri, params)
    
if __name__ == '__main__':
    pass
# 100281 2000
# 100282 2001
# 100283 2002
# 100284 2003
access_token = Test.User.getAccessToken('15015168186', '123456')
attentionList(access_token)
# 加关注
# access_token = Test.User.getAccessToken('100729', 'qqq')
# # remark(access_token, 100731, 'remarkName')
# # 2000关注其他
# attentionAdd(access_token, 100731)
# # attentionAdd(access_token, 100283)
# # attentionAdd(access_token, 100284)
# # 2000的关注
# attentionList(access_token)
# fansList(access_token)

# 2001 2002 2003关注2000
# access_token = TestUser.getAccessToken('2001', 'qqq')
# attentionAdd(access_token, 100281)
# access_token = TestUser.getAccessToken('2002', 'qqq')
# attentionAdd(access_token, 100281)
# access_token = TestUser.getAccessToken('2003', 'qqq')
# attentionAdd(access_token, 100281)


# friendsAdd(access_token, 100282)


# attentionList(access_token.encode('utf-8'))
# friendsDelete(access_token.encode('utf-8'), 100024)
# attentionList(access_token.encode('utf-8'))

