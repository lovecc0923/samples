# -*- coding: UTF-8 -*-

import urllib, urllib2, hashlib, time, gzip, StringIO
from __builtin__ import int

def httpInvoke(uri, params):
    try:
        url = 'http://%s:%s%s%s' % ('114.119.6.150', 8094, '', uri) 
#         url = 'http://%s:%s%s%s' % ('localhost', 8094, '', uri)   
        data = urllib.urlencode(params)
         
        print '接口地址：%s' % url
        print '请求参数：%s' % data
        start = time.time()
        
        request = urllib2.Request(url, data)
        request.add_header('accept-encoding', 'gzip,deflate')
        response = urllib2.urlopen(request)
        
        isGzip = response.headers.get('Content-Encoding')
        if isGzip:
            compresseddata = response.read()
            compressedstream = StringIO.StringIO(compresseddata)
            gzipper = gzip.GzipFile(fileobj=compressedstream)
            body = gzipper.read()
        else:
            body = response.read()
        
        print 'Content-Encoding：%s' % response.headers.get('Content-Encoding') 
        
        print "耗时：%s 毫秒" % int(((time.time() - start) * 1000))
        print '响应结果：%s' % body
        
        return body
    except Exception, e:
        print e
        
def httpInvoke2(url, params):
    try:
        data = urllib.urlencode(params)
         
        print '接口地址：%s' % url
        print '请求参数：%s' % data
        start = time.time()
        
        request = urllib2.Request(url, data)
        response = urllib2.urlopen(request)
        body = response.read()
         
        print "耗时：%s 毫秒" % int(((time.time() - start) * 1000))
        print '响应结果：%s' % body
        
        return body
    except Exception, e:
        print e
        
def getParamString(p):
    params = []
    
    for (k, v) in p.items():
        params.append('%s=%s' % (k, urllib.quote(v) if isinstance(v, str) else v))

    return '&'.join(params)

def md5(s):
    digest = hashlib.md5()
    digest.update(s)
    return digest.hexdigest()

def my_urlencode(str1) :
    reprStr = repr(str1).replace(r'\x', '%')
    return reprStr[1:-1]

def timestamp():
    return int(time.time())
