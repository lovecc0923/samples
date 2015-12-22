# -*- coding: utf-8 -*-
'''
Created on 2014年5月27日

@author: Administrator
'''
import redis

host = '114.119.6.150'
port = 6380
redisClient = redis.Redis(host=host, port=port, db=0)

def test():
    print redisClient.hgetall('goodsSet')
    for key in redisClient.keys('*'):
        if key != 'goodsSet':
            print key, redisClient.get(key), redisClient.ttl(key)
            
def clearAll():
    redisClient.flushdb()
def listKey(pattern):
    
    for key in redisClient.keys(pattern):
        print key
if __name__ == '__main__':
    pass
listKey('msg.id.hot.list:*')
print redisClient.zcard('msg.id.hot.list:440300')
b = redisClient.zrevrange('msg.id.hot.list:440300', 0, 50)
a = redisClient.hgetall('msg.hot.list:440300')
print 'a'
# listKey()
# redisClient.flushdb()



