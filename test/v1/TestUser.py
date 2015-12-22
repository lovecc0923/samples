# -*- coding: UTF-8 -*-

import Test
import urllib2, urllib, utils, time

if __name__ == '__main__':
    pass

# 114.05265,22.608367
# Test.User.UserRegister('18908983801', 'qqq')
# Test.User.UserRegister('2002', 'qqq')
# access_token = Test.User.getAccessToken('18503054711', '123456')

access_token = Test.User.getAccessToken('15015168186', '123456')

# params = {}
# params['access_token'] = access_token
# params['toUserId'] = 48
# utils.httpInvoke2('http://192.168.97.252:8092/friends/attention/add', params)
# 
# 
# params = {}
# params['access_token'] = access_token
# params['oldPassword'] = utils.md5('qqq')
# params['newPassword'] = utils.md5('abc')
# utils.httpInvoke2('http://192.168.97.252:8092/user/password/update', params)

# params = {}
# params['telephone'] = 18908983801
# params['randcode'] = 123456
# params['newPassword'] = utils.md5('qqqq')
# utils.httpInvoke2('http://192.168.97.252:8092/user/password/reset', params)


# params = {}
# params['access_token'] = access_token
# params['userId'] = 50
# params['pageSize'] = 1
# utils.httpInvoke2('http://192.168.97.252:8092/user/query', params)


# access_token = Test.User.getAccessToken('18908983800', 'qqq')
# params = {}
# params['access_token'] = access_token
# params['longitude'] = 1
# params['latitude'] = 1
# utils.httpInvoke2('http://localhost:8092/nearby/user_v2', params)

# params = {}
# params['app_id'] = '216461910000035461'
# params['app_secret'] = '6ee8640fa58fb452c69e265f455cabac'
# params['grant_type'] = 'client_credentials'
# utils.httpInvoke2('https://oauth.api.189.cn/emp/oauth2/v3/access_token', params)
# Test.User.UserLogin('18908983800', '123456')
# access_token = Test.User.getAccessToken('18908983800', '123456')

# params = {}
# params['access_token'] = access_token
# params['receiver'] = 10000018
# params['startTime'] = 0
# params['endTime'] = 0
# params['pageIndex'] = 0
# params['pageSize'] = 50
# utils.httpInvoke2('http://localhost:8092/tigase/shiku_msgs', params)
# 
# params = {}
# params['access_token'] = access_token
# params['roomId'] = 'abc'
# params['startTime'] = 0
# params['endTime'] = 0
# params['pageIndex'] = 0
# params['pageSize'] = 50
# utils.httpInvoke2('http://localhost:8092/tigase/shiku_muc_msgs', params)

# access_token = Test.User.getAccessToken('18908983800', 'qqq')
# params = {}
# params['longitude'] = '114.05265'
# params['latitude'] = '22.608367'
# params['nickname'] = 'tj'
# params['minAge'] = 0
# params['maxAge'] = 200
# params['sex'] = ''
# params['access_token'] = access_token
# params['pageIndex'] = 0
# params['pageSize'] = 50
# utils.httpInvoke2('http://imapi.youjob.co/nearby/user', params)
# utils.httpInvoke2('http://localhost:8092/nearby/user', params)
# 
# 
# params = {}
# params['longitude'] = '114.05265'
# params['latitude'] = '22.608367'
# params['access_token'] = access_token
# params['pageIndex'] = 1
# params['pageSize'] = 50
# utils.httpInvoke2('http://imapi.youjob.co/nearby/user', params)


# 
# 
# Test.User.UserQuery(access_token)
# # 自己
# Test.User.UserGet(access_token, '')

# access_token = Test.User.getAccessToken('18503054767', '123456')
# access_token = Test.User.getAccessToken('18908983801', 'qqq')
# Test.User.UserGet(access_token, '100001')
# # 陌生人关系
# Test.User.UserGet(access_token, 100406)
# # 关注关系
# Test.User.UserGet(access_token, 100406)
# # 好友关系
# Test.User.UserGet(access_token, 100406)
# 
# for i in range(100729, 100829):
#     Test.User.UserRegister(i, 'qqq')

# params = {}
# params['telephone'] = '18076983260'
# params['password'] = utils.md5('a')
# params['nickname'] = '测试昵称%s' % 18076983260
# params['sex'] = 1
# params['birthday'] = utils.timestamp()
# params['companyId'] = 1
# 
# data = urllib.urlencode(params)
# print data
# req = urllib2.Request('http://192.168.1.240:8080/api/v1/user/register', data)
# response = urllib2.urlopen(req)
# the_page = response.read()
# print the_page
