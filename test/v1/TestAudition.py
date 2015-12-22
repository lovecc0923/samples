# -*- coding: UTF-8 -*-
'''
Created on 2014年6月17日

@author: Administrator
'''

import utils, Test

def AuditionAdd(access_token, userId):
    uri = '/audition/add'
    params = {}
    params['access_token'] = access_token
    params['jobId'] = 1
    params['jobName'] = 'JAVA工程师'
    params['wExamId'] = 1
    params['iExamId'] = 0
    params['isVideo'] = 0
    params['startTime'] = utils.timestamp()
    params['expiredTime'] = utils.timestamp()
    params['userId'] = userId
    
    utils.httpInvoke(uri, params)
    
def AuditionGet(access_token, auditionId):
    uri = '/audition/get'
    params = {}
    params['access_token'] = access_token
    params['auditionId'] = auditionId
    
    utils.httpInvoke(uri, params)
    
def AuditionList(access_token):
    uri = '/audition/list'
    params = {}
    params['access_token'] = access_token
    
    utils.httpInvoke(uri, params)


def wExamGet(access_token, examId):
    uri = '/audition/wExam/get'
    
    params = {}
    params['access_token'] = access_token
    params['examId'] = examId
    
    utils.httpInvoke(uri, params)

def wExamAnswer(access_token, auditionId, answer):
    uri = '/audition/wExam/answer'
    
    params = {}
    params['access_token'] = access_token
    params['auditionId'] = auditionId
    params['answer'] = answer
    
    utils.httpInvoke(uri, params)

def iExamAnswer(access_token, auditionId, questionId, answer):
    uri = '/audition/iExam/answer'
    
    params = {}
    params['access_token'] = access_token
    params['auditionId'] = auditionId
    params['questionId'] = questionId
    params['answer'] = answer
    
    utils.httpInvoke(uri, params)

def iScore(access_token, auditionId, score):
    uri = '/audition/iScore'
    
    params = {}
    params['access_token'] = access_token
    params['auditionId'] = auditionId
    params['score'] = score
    
    utils.httpInvoke(uri, params)

def vScore(access_token, auditionId, score):
    uri = '/audition/video/score'
    
    params = {}
    params['access_token'] = access_token
    params['auditionId'] = auditionId
    params['score'] = score
    
    utils.httpInvoke(uri, params)
    
def bstj(access_token):
    auditionId = '53c5105a45c91f605040188a'
    answer = '[{questionId:1,answer:125,score:10,correct:1},{questionId:2,answer:125,score:10,correct:0},{questionId:3,answer:2,score:10,correct:1},{questionId:4,answer:9,score:10,correct:0}]'
    wExamAnswer(access_token, auditionId, answer)
def jttj(access_token):
    auditionId = '53c5105a45c91f605040188a'
    answer = 'http://192.168.1.240/video/test.mp4'
    iExamAnswer(access_token, auditionId, 5278, answer)
def test2():
    access_token = Test.User.getAccessToken('100729', 'qqq')
#     AuditionAdd(access_token, 100731)
    AuditionList(access_token)
#     for i in range(1, 5, 1):
#         AuditionAdd(access_token, 100731)
#     print utils.timestamp()

# 笔试提交
#     bstj(access_token)

# 面试提交
# jttj(access_token)


# 视频评分
# auditionId = '53c2f377c443dd1f5478c544'
# for socre in range(60, 110, 10):
#     vScore(access_token, auditionId, 100)

# 静态面试评分
# for socre in range(60, 110, 10):
#     iScore(access_token, auditionId, 100)

# AuditionGet(access_token, auditionId)
# AuditionList(access_token)
#

# AuditionAdd(access_token, 100731)
# AuditionGet(access_token, '53a94f4845c9d03bc3560b9a')
# access_token = Test.User.getAccessToken('2012', 'qqq')
# access_token = Test.User.getAccessToken('100731', 'qqq')
# # AuditionList(access_token)
# 
# wExamGet(access_token, 1)
# 
if __name__ == '__main__':
    access_token = Test.User.getAccessToken('18908983800', 'qqq')
    AuditionAdd(access_token, 100000)
#     AuditionAdd(access_token, 100731)
#     access_token = Test.User.getAccessToken('100729', 'qqq')
#     for i in range(1, 10, 1):
#         AuditionAdd(access_token, 100731)
