# -*- coding: UTF-8 -*-
'''
Created on 2014年12月1日

@author: Administrator
'''

import utils, Test

def resumeAdd(access_token):
    uri = '/resume/add'
    params = {}
    params['access_token'] = access_token
    params['resumeName'] = '.Net工程师'
    
    utils.httpInvoke(uri, params)
    
def resumeUpdate(access_token, resumeId, nodeName, text):
    uri = '/resume/update'
    params = {}
    params['access_token'] = access_token
    params['resumeId'] = resumeId
    params['nodeName'] = nodeName
    params['text'] = text
    
    utils.httpInvoke(uri, params)

def resumeDelete(access_token, text):
    uri = '/resume/delete'
    params = {}
    params['access_token'] = access_token
    params['text'] = text
    
    utils.httpInvoke(uri, params)
    
def resumeGet(access_token, resumeId, nodeName):
    uri = '/resume/get'
    params = {}
    params['access_token'] = access_token
    params['resumeId'] = resumeId
    params['nodeName'] = nodeName
    
    utils.httpInvoke(uri, params)
    
def resumeList(access_token):
    uri = '/resume/list'
    params = {}
    params['access_token'] = access_token
    
    utils.httpInvoke(uri, params)
    
def resuemNameList(access_token):
    uri = '/resume/name/list'
    params = {}
    params['access_token'] = access_token
    
    utils.httpInvoke(uri, params)

def addChild(access_token):
    uri = '/resume/e/add'
    params = {}
    params['access_token'] = access_token
    params['text'] = '{"begin" : 1251734400,"end" : 1338480000,"name" : "华中科技大学","degree" : 6,"degreeText" : "大专","major" : 1327,"majorText" : "软件工程","isForeign" : 0}'
    params['resumeId'] = '5481269248262558254af36b'
    utils.httpInvoke(uri, params)
    
def updateChild(access_token):
    uri = '/resume/e/update'
    params = {}
    params['access_token'] = access_token
    params['resumeId'] = '5481563aa310fbb3cf944e6a'
    
    #"id":"5481269148262558254af360",
    params['text'] = '{"begin" : 1251734400,"end" : 1338480000,"name" : "华中科技大学123","degree" : 6,"degreeText" : "大专","major" : 1327,"majorText" : "软件工程","isForeign" : 0}'
    
    utils.httpInvoke(uri, params)
    
def deleteChild(access_token):
    uri = '/resume/e/delete'
    params = {}
    params['access_token'] = access_token
    params['resumeId'] = '5481269248262558254af36b'
    params['childId'] = '54812b464826cd6abf8f0d0b'
    
    utils.httpInvoke(uri, params)    

if __name__ == '__main__':
#     access_token = Test.User.getAccessToken('18503054765', '123456')18938880752
    access_token = Test.User.getAccessToken('18938880001', '123456')
#     addChild(access_token)
# deleteChild(access_token)
# updateChild(access_token)
#     resumeAdd(access_token)
#     resumeUpdate(access_token, '547c2b6da310bc5906dc9e2d', 'eduList', '[{"begin" : 1251734400,"degree" : 6,"end" : 0,"major" : "软件工程","name" : "测试测试"},{"begin" : 1251734400,"degree" : 6,"end" : 0,"major" : "软件工程","name" : "测试测试"}]')
#     resumeDelete(access_token, '["547c2a21a31064388b4f75f0"]')
    resumeGet(access_token, '54b88d24a310f26add3b0024', '')
#     resumeList(access_token)
# resuemNameList(access_token)



