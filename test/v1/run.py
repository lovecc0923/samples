# -*- coding: UTF-8 -*-
'''
Created on 2014年5月29日

@author: Administrator
'''
import httplib, urllib, collections, hashlib

#host = '192.168.1.102'
host = 'localhost'
port = 8080

def _http(url, method, params):
    httpClient = None
    body = None
    try:
        print '接口地址：http://%s:%s%s' % (host, port, url)
        print '请求参数：%s' % params
        
        headers = {"Content-type":"application/x-www-form-urlencoded", "Accept":"text/plain"}
        httpClient = httplib.HTTPConnection(host, port, timeout=20)
        httpClient.request(method, url, params, headers)
        response = httpClient.getresponse()
        body = response.read()
        
        print '响应结果：%s' % body
        # print response.status
        # print response.reason
        # print response.read()
        # print response.getheaders()
    except Exception, e:
        print e
    finally:
        if httpClient:
            httpClient.close()
    
    return body

def _encode_params(**kw):
    '''
    Do url-encode parameters

    >>> _encode_params(a=1, b='R&D')
    'a=1&b=R%26D'
    >>> _encode_params(a=u'\u4e2d\u6587', b=['A', 'B', 123])
    'a=%E4%B8%AD%E6%96%87&b=A&b=B&b=123'
    '''
    def _encode(L, k, v):
        if isinstance(v, unicode):
            L.append('%s=%s' % (k, urllib.quote(v.encode('utf-8'))))
        elif isinstance(v, str):
            L.append('%s=%s' % (k, urllib.quote(v)))
        elif isinstance(v, collections.Iterable):
            for x in v:
                _encode(L, k, x)
        else:
            L.append('%s=%s' % (k, urllib.quote(str(v))))
    args = []
    for k, v in kw.iteritems():
        _encode(args, k, v)
    return '&'.join(args)

def _md5(s):
    h = hashlib.md5()
    h.update(s)
    return h.hexdigest() 

def UserRegister(telephone):
    url = '/api/v1/user/register'
    params = _encode_params(telephone=telephone, password=123456, nickname='hohoho', sex=1, birthday='1989-10-26')
    _http(url, 'POST', params)
def UserLogin():
    url = '/api/v1/user/login'
    params = _encode_params(telephone=_md5('18008983800'), password=123456, grant_type=123)
    _http(url, 'POST', params)
def UserGet():
    url = '/api/v1/user/get'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad')
    _http(url, 'POST', params)
def UserQuery():
    url = '/api/v1/user/query'
    params = _encode_params(access_token='fc77f5174c82416aa2c84ba1b96f7939', sex=1)
    _http(url, 'POST', params)

def AuditionAdd():
    url = '/api/v1/audition/add'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', jobId=1, writeExamId=0, talkExamId=1, talkFlag=0, startTime='2014/05/29', expiredTime='2014/06/15', toUserId=15, toTelephone='')
    _http(url, 'POST', params)
def AuditionGet():
    url = '/api/v1/audition/get'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', auditionId1=1)
    _http(url, 'POST', params)

def getCommentList():
    url = '/api/v1/circle/msg/comment/list'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', messageId='538695d8daf82d61d2a87aa6')
    _http(url, 'POST', params)
    
def addGift():
    url = '/api/v1/circle/msg/gift/add'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', messageId='538695d8daf82d61d2a87aa6', gifts='[{goodsId:1,count:2},{goodsId:2,count:3}]')
    _http(url, 'POST', params)

def getGiftList():
    url = '/api/v1/circle/msg/gift/list'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', messageId='538695d8daf82d61d2a87aa6')
    _http(url, 'POST', params)

def getMsgList():
    url = "/api/v1/circle/msg/list"
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', pageIndex=0, pageSize=5)
    _http(url, 'POST', params)

def addMsg():
    url = '/api/v1/circle/msg/add'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', type=1, source=1, flag=1, text='Hi all', resources='http://d.hiphotos.baidu.com/news/pic/item/0e2442a7d933c895917a0582d31373f0830200c6.jpg,http://a.hiphotos.baidu.com/news/pic/item/faedab64034f78f0c28a100a7b310a55b2191c41.jpg')
    _http(url, 'POST', params)

def getPraiseList():
    url = '/api/v1/circle/msg/praise/list'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', messageId='538695d8daf82d61d2a87aa6')
    _http(url, 'POST', params)
def getGoodsList():
    url = '/api/v1/goods/list'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad')
    _http(url, 'POST', params)
    
def friendsAdd():
    url = '/api/v1/friends/add'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad', friendsUserId=12, friendsName='123')
    _http(url, 'POST', params)

def attentionAdd(access_token, toUserId):
    url = '/api/v1/friends/attention/add'
    params = _encode_params(access_token=access_token, toUserId=toUserId)
    _http(url, 'POST', params)

def attentionList():
    url = '/api/v1/friends/attention/list'
    params = _encode_params(access_token='e72e9eea9b274a0bab27f709d2b809ad')
    _http(url, 'POST', params)

def test():
    for i in range(100, 105, 1):
        UserRegister(i)

if __name__ == '__main__':
    # e72e9eea9b274a0bab27f709d2b809ad
    # UserRegister()
    # UserLogin()
    # UserGet()
    # AuditionAdd()
    # AuditionGet()
    # UserQuery()
    # getCommentList()
    # addGift()
    # getGiftList()
    # getMsgList()
    # addMsg()
    # getPraiseList()
    # getGoodsList()
    # url = 'http://115.28.178.6:80/skapi/v2/user/register'
    # print _md5('123456')
    #
    # friendsAdd()
    # attention()
    # attentionList()
    # test()
    # accessTokenArray = ['bf185e0a78d746c1907331df1434373b', 'd41caa3c01734658a4ba7d07fec7ba4a', '9d20037d944d467eb3c63a035e727208', '492b73efab344bbc89f04896ef0b4dd1', 'f74802e0be8341999a0dffb18fa116b8']
    
    # attentionAdd('d41caa3c01734658a4ba7d07fec7ba4a', 100004)
    # attentionAdd('bf185e0a78d746c1907331df1434373b', 100006)
    #UserRegister('1234561')
    #UserQuery()
    UserLogin()
    
    
