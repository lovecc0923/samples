# -*- coding: UTF-8 -*-

import v2, json
from v2 import TestAuth

def interestJob(access_token, op, userId, jobId):
    uri = '/job/interest/%s' % op
        
    params = {}
    params['access_token'] = access_token
    params['userId'] = userId
    params['jobId'] = jobId
        
    s = v2.utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

def getInterestList(access_token):
    uri = '/job/interestList'
        
    params = {}
    params['access_token'] = access_token
    params['id'] = ''
    params['pageSize'] = ''
        
    s = v2.utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

def getInterestRevList(access_token):
    uri = '/job/interestRevList'
        
    params = {}
    params['access_token'] = access_token
    params['id'] = ''
    params['pageSize'] = ''
        
    s = v2.utils.httpInvoke(uri, params)
    obj = json.loads(s)
    return obj["resultCode"] == 1

if __name__ == '__main__':
    pass
telephone = '17708450926'
password = 'qqq'
version = 1
if TestAuth.Auth.Verify(telephone):
    print '*'
else:
    access_token = TestAuth.Auth.GetAccessToken(telephone, password, version)
    interestJob(access_token, 0, 100017, '55dd8a77903bc6fcfa464c97')
    # 感兴趣的职位
    getInterestList(access_token)
    # 对职位感兴趣的
    access_token = TestAuth.Auth.GetAccessToken('18908983800', 'qqq', 2)
    getInterestRevList(access_token)
    
