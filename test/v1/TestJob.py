# -*- coding: UTF-8 -*-
'''
Created on 2014年11月11日

@author: Administrator
'''

import utils, Test, json

def newJob(access_token):
    uri = '/job/add'
    params = {}
    params['access_token'] = access_token
    params['jobName'] = '.Net工程师'
    params['description'] = '<div style="padding-bottom:30px;">岗位职责：<br>1、负责公司手机平台的后台即时通讯(IM)模块的设计，开发和优化工作，并可支持百万级并发量；<br>2、负责IM服务器架构搭建、数据库搭建、后台程序开发、与手机客户端接口的开发；<br>3、负责研究和应用OpenFire等开源技术；<br>4、配合andriod端、IOS端研发人员完成开发或提供支持；<br>职位要求：<br>1、大学专科或以上学历，计算机相关专业；<br>2、三年以上开发经验，有架构设计经验者优先；<br>3、从事过即时通讯(IM)相关产品或项目开发，有海量用户分布式系统开发经验;<br>4、编程基础扎实，熟悉io、多线程、集合等基础框架，熟悉分布式、缓存等机制。<br>5、熟悉OpenFire等开源IM框架；<br>6、熟悉TCP/IP、Socket、UDP、HTTP,深入理解XMPP、jingle、SIP、SIMPLE通讯协议;</div>'
    params['countryId'] = 1
    params['provinceId'] = 1
    params['cityId'] = 1
    params['areaId'] = 1
    params['workExp'] = 1
    params['diploma'] = 1
    params['salary'] = 1
    params['vacancy'] = 100
    params['isVideo'] = 1
    params['isOffline'] = 1
    params['examList'] = '[1,2,3,4]'
    
    utils.httpInvoke(uri, params)

def updateJob(access_token, jobId):
    uri = '/job/update'
    params = {}
    params['jobId'] = jobId
    params['access_token'] = access_token 
#     params['jobName'] = 'Unity3D场景工程师137'
#     params['examList'] = '[1,3,7]'
    params['isOffline'] = 0
    params['isVideo'] = 0
    
    utils.httpInvoke(uri, params)
    
def newJobApply(access_token, text):
    uri = '/job/apply'
    params = {}
    params['access_token'] = access_token
    params['resumeId'] = '5423000fa310b743c412ed7d'
    params['text'] = text
    return utils.httpInvoke(uri, params)
    
def agreeJobApply(access_token, text):
    uri = '/job/apply/agree'
    params = {}
    params['access_token'] = access_token
    params['text'] = text
    utils.httpInvoke(uri, params)
    
def agreeArt(access_token, text):
    uri = '/art/agree'
    params = {}
    params['access_token'] = access_token
    params['text'] = text
    utils.httpInvoke(uri, params)    
    
        
def passAft(access_token, text):
    uri = '/aft/pass'
    params = {}
    params['access_token'] = access_token
    params['text'] = text
    params['startTime'] = utils.timestamp()
    
    utils.httpInvoke(uri, params)

def getAft(access_token, aftId):
    uri = '/aft/get'
    params = {}
    params['access_token'] = access_token
    params['id'] = aftId
    utils.httpInvoke(uri, params)

def applyList(access_token):
    uri = '/job/apply/list'
    params = {}
    params['access_token'] = access_token
    params['status'] = 0
    utils.httpInvoke(uri, params)
    
def jobQuery(access_token, companyId, status):
    uri = '/job/query'
    params = {}
    params['access_token'] = access_token
    params['keyword'] = 'java'
    params['days'] = 0
#     params['companyId'] = companyId
#     params['status'] = status
    
    utils.httpInvoke(uri, params)
    
def jobList(access_token, status):
    uri = '/job/query'
    params = {}
    params['access_token'] = access_token
    params['status'] = status
    
    utils.httpInvoke(uri, params)
    
def jobGet():
    uri = '/job/get'
    params = {}
    params['access_token'] = Test.User.getAccessToken('18503054766', '123456')
    params['jobId'] = '547427a3a3106ccc168bc0da'
    
    utils.httpInvoke(uri, params)
        
def answer(access_token, aftId, examId):
    uri = '/aft/answer'
    params = {}
    params['access_token'] = access_token
    params['aftId'] = aftId
    params['examId'] = examId
    params['answer'] = '[{"questionId" : 1,"correct" : 1,"score" : 10,"answer" : "0"},{"questionId" : 2,"correct" : 1,"score" : 20,"answer" : "0"}]'
    params['score'] = 30
        
    utils.httpInvoke(uri, params)
    
def jobLatest():
    uri = '/job/latest'
    params = {}
    params['access_token'] = Test.User.getAccessToken('18503054766', '123456')
    
    utils.httpInvoke(uri, params)
    
def artQuery(pageIndex):
    uri = '/art/query'
    params = {}
    params['access_token'] = Test.User.getAccessToken('18503054711', '123456')
    params['pageIndex'] = pageIndex
    params['pageSize'] = 5
    params['type'] = 1
    utils.httpInvoke(uri, params)
    
def aftQuery():
    uri = '/aft/query'
    params = {}
    params['access_token'] = Test.User.getAccessToken('18503054767', '123456')
    params['type'] = 1
    utils.httpInvoke(uri, params)
    
def jobDelete():
    uri = '/job/delete'
    params = {}
    params['access_token'] = Test.User.getAccessToken('18908983800', 'qqq')
    params['text'] = '["547ee7daa310bc5906dc9e4a"]'
    
    utils.httpInvoke(uri, params)

def republish():
    uri = '/job/republish'
    params = {}
    params['access_token'] = Test.User.getAccessToken('18908983800', 'qqq')
    params['jobId'] = '5472b1dd48268cec2dbec1ca'
    params['jobName'] = '.Net工程师1234'
    params['description'] = '6、熟悉TCP/IP、Socket、UDP、HTTP,深入理解XMPP、jingle、SIP、SIMPLE通讯协议;</div>'
    params['countryId'] = 1
    params['provinceId'] = 1
    params['cityId'] = 1
    params['areaId'] = 1
    params['workExp'] = 1
    params['diploma'] = 1
    params['salary'] = 1
    params['vacancy'] = 100
    params['isVideo'] = 1
    params['isOffline'] = 1
    params['examList'] = '[1]'
    
    
    utils.httpInvoke(uri, params)    
    
    
if __name__ == '__main__':
    pass
# republish()
# jobDelete()
# artQuery()
# jobQuery(Test.User.getAccessToken('18503054765', '123456'), 1, 1)
# agreeArt(Test.User.getAccessToken('18503054765', '123456'), '["54768ea5a310ac668a0529f2"]')
# newJob(Test.User.getAccessToken('18503054766', '123456'))
# updateJob(Test.User.getAccessToken('18503054766', '123456'), '5472b1dd48268cec2dbec1ca')

# jobList(Test.User.getAccessToken('18503054767', '123456'), 1)
# 申请职位
# s = newJobApply(Test.User.getAccessToken('18503054765', '123456'), '["547ee6fba310bc5906dc9e46"]')
# obj = json.loads(s)


# 同意申请
# agreeJobApply(Test.User.getAccessToken('18908983800', 'qqq'), json.dumps(obj["data"]))
# agreeJobApply(Test.User.getAccessToken('18503054766', '123456'), '["5473f633a7c4ea8652fa21bf"]')

# passAft(Test.User.getAccessToken('18503054766', '123456'), '["54b4c3fea310072b9f69d815"]')

# answer(Test.User.getAccessToken('18503054765', '123456'), '5473f7f3a7c4ea8652fa21c0', 1)


# uri = '/job/hot'
# params = {}
# params['access_token'] = Test.User.getAccessToken('18503054767', '123456')
# utils.httpInvoke(uri, params)

# updateJob(Test.User.getAccessToken('18908983800', 'qqq'), '546eb01ea31046874cf206d4')
#     uri = '/job/query'
#     params = {}
#     params['access_token'] = Test.User.getAccessToken('18503054767', '123456')
#     params['companyId'] = 1
#     params['pageIndex'] = 1
#     
#     utils.httpInvoke(uri, params)

artQuery(1)
# artQuery(1)
# artQuery(1)
# artQuery(2)


# aftQuery()
# uri = '/art/start'
# params = {}
# params['access_token'] = Test.User.getAccessToken('18503054767', '123456')
# params['artId'] = '54b4e483a3102b00b4e3d31b'
# utils.httpInvoke(uri, params)
# uri = '/art/start'
# params = {}
# params['access_token'] = Test.User.getAccessToken('18503054765', '123456')
# params['artId'] = '54b4e483a3102b00b4e3d31b'
# utils.httpInvoke(uri, params)
# 
# json.load('')


