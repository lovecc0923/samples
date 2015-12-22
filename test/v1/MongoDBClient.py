# -*- coding: utf-8 -*-
'''
Created on 2014年5月27日

@author: Administrator
'''

import pymongo, json, time
from bson.objectid import ObjectId

mongo = pymongo.Connection('121.37.30.15', 27017)
db = mongo.mianshi

praise = db.praise

def build(size):
    pass

def add(i):
    params = {}
    params['id'] = i
    params['userId'] = i
    
#     o = json.dumps(params)
#     start = time.time()
    
    praise.save(params)
    
#     print time.time() - start

def showAll():
    for o in praise.find():
        print o

def multi():
    start = time.time()
    for i in range(10000, 20000, 1):
        add(i)
#     print (time.time() - start) * 1000
    # 10000条，32.8589999676秒

if __name__ == '__main__':
    pass
db.user.update({},{'companyId':0})
for o in db.user.find():
    print o
# showAll()
# print praise.find().count()
# for o in praise.find().sort([("_id", pymongo.ASCENDING)]).limit(10):
#     print o
# for o in praise.find().sort([("_id", pymongo.DESCENDING)]).limit(5):
#     print o
# print '\n'
# for o in praise.find({'_id': {'$lt': ObjectId('53ac2299ffca2f11a890dbe8')}}).sort([("_id", pymongo.DESCENDING)]).limit(5):
#     print o
#     
# for o in praise.find({'_id': {'$gt': ObjectId('53ac2299ffca2f11a890dbe8')}}).sort([("_id", pymongo.ASCENDING)]).limit(5):
#     print o
# count = 0
# for i in range(40000, 50000, 1):
#     start = time.time()
#     add(i)
#     count += (time.time() - start) * 1000
# print count


# for o in praise.find({'_id': {'$lt': ObjectId('53ac2299ffca2f11a890dbe8')}}).sort([("_id", pymongo.DESCENDING)]).limit(50):
#     print o

# # 最后一页
# for o in praise.find().sort([("_id", -1)]).limit(5):
#     print o
# print '\n'
# # 倒数2页
# for o in praise.find({'_id': {'$lt': ObjectId('53ac2816ffca2f1384aecef4')}}).sort([("_id", -1)]).limit(5):
#     print o
# print '\n' 
# # 倒数3页
# for o in praise.find({'_id': {'$lt': ObjectId('53ac2816ffca2f1384aeceef')}}).sort([("_id", -1)]).limit(5):
#     print o
# praise.drop()
# for o in praise.find():
#     print o
