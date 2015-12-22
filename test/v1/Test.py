# -*- coding: UTF-8 -*-
'''
Created on 2014年6月19日

@author: Administrator
'''
import thread, time, json
import utils

class User(object):
    
    def __init__(self):
        pass
    
    @staticmethod
    def UserRegister(telephone, password):
        uri = '/user/register'
        
        params = {}
        params['telephone'] = telephone
        params['password'] = utils.md5(password)
        params['nickname'] = '测试昵称%s' % telephone
        params['sex'] = 1
        params['longitude'] = 1
        params['latitude'] = 1
        params['birthday'] = utils.timestamp()
        params['companyId'] = 0
        
        utils.httpInvoke(uri, params)
        
    @staticmethod    
    def UserLogin(telephone, password):
        uri = '/user/login'
        
        params = {}
        params['telephone'] = utils.md5(telephone) 
        params['password'] = utils.md5(password)
        params['grant_type'] = 'grant_type'
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        
        return obj
    
    @staticmethod    
    def UserGet(access_token, userId):
        uri = '/user/get'
        
        params = {}
        params['access_token'] = access_token 
        params['userId'] = userId
       
        utils.httpInvoke(uri, params)
        
    @staticmethod        
    def UserQuery(access_token):
        uri = '/user/query'
        
        params = {}
        params['access_token'] = access_token
        params['nickname'] = '97'
#         params['sex'] = 1
#         params['pageIndex'] = 0
        params['pageSize'] = 10
       
        utils.httpInvoke(uri, params)
        
    @staticmethod    
    def getAccessToken(telephone, password):
        obj = User.UserLogin(telephone, password)
        access_token = obj['data']['access_token']
        
        return access_token.encode('utf-8')

class Company(object):
    
    def __init__(self, params):
        pass
    
    @staticmethod
    def jobList(access_token):
        pass
        uri = '/company/job/list'
        
        params = {}
        params['access_token'] = access_token
        
        utils.httpInvoke(uri, params)
    
    @staticmethod
    def examList(access_token):
        pass
        uri = '/company/exam/list'
        
        params = {}
        params['access_token'] = access_token
        params['type'] = 0
        
        utils.httpInvoke(uri, params)

class Goods(object):
    def __init__(self):
        pass
    
    @staticmethod
    def goodsList(access_token):
        uri = '/goods/list'
        
        params = {}
        params['access_token'] = access_token
        
        utils.httpInvoke(uri, params)
        
def timer(no, interval):  
        # cnt = 0  
        # while cnt < 10:  
        #    print 'Thread:(%d) Time:%s\n' % (no, time.ctime())  
        #    time.sleep(interval)  
        #    cnt += 1  
        # thread.exit_thread()
    try:
        thread.exit_thread()
    except Exception, e:
        print e
        print time.time()
 
def test2():
    for i in range(0, 100, 1):
        print i
        thread.start_new_thread(timer, (1, 1))
     
    while True:
        pass
