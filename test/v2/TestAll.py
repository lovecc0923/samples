# -*- coding: UTF-8 -*-
import json

from v2 import utils, TestAuth


def jobUpdate(access_token):
    uri = '/job/update'
        
    params = {}
    params['access_token'] = access_token
#     params['jobId'] = '罗融春'
    params['fnId'] = 1
    params['jobName'] = 'iOS工程师'
    params['salary'] = 2
    params['workTime'] = 2
    params['degree'] = 2
    params['cityId'] = 44578
    params['desc'] = '不错的职位'
        
    s = utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

def jobGet(access_token, jobId):
    uri = '/job/get'
        
    params = {}
    params['access_token'] = access_token
    params['jobId'] = jobId
        
    s = utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

def jobSearch(access_token, jobId):
    uri = '/job/searchByFn'
        
    params = {}
    params['access_token'] = access_token
    params['pageIndex'] = 0
    params['pageSize'] = 10
        
    s = utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

def browseList(access_token, jobId):
    uri = '/job/browseList'
        
    params = {}
    params['access_token'] = access_token
    params['jobId'] = jobId
    params['id'] = ''
    params['pageSize'] = ''
        
    s = utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

def publishList(access_token):
    uri = '/job/publishList'
        
    params = {}
    params['access_token'] = access_token
    params['pageIndex'] = '0'
    params['pageSize'] = '10'
        
    s = utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

def GetActivity(access_token):
    uri = '/activity/get'
        
    params = {}
    params['access_token'] = access_token
    params['pageIndex'] = '0'
    params['pageSize'] = '10'
        
    s = utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

if __name__ == '__main__':
    pass

telephone = '18908983800'
password = 'qqq'
version = 1

# telephone = '18908983800'
# password = 'qqq'
# version = 2

if TestAuth.Auth.Verify(telephone):
#     User.SendSms(telephone)
    TestAuth.Auth.Register(telephone, password)
else:
    access_token = TestAuth.Auth.GetAccessToken(telephone, password, version)
    GetActivity(access_token)
#     User.Update2(access_token)
#     User.ResumeUpdate(access_token)
#     User.ResumeGet(access_token)

# jobUpdate(access_token)
# jobId = '55dd81bc903bcc0200b310cf'
# jobGet(access_token, jobId)
# publishList(access_token)
# browseList(access_token, jobId)
jobSearch(access_token, '')
