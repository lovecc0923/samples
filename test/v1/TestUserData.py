# -*- coding: UTF-8 -*-

import utils

def avatarSet(access_token, photoId):
    uri = '/user/avatar/set'
    params = {}
    params['access_token'] = access_token
    params['photoId'] = photoId
    
    utils.httpInvoke(uri, params)
    
def photoAdd(access_token, photos):
    uri = '/user/photo/add'
    params = {}
    params['access_token'] = access_token
    params['photos'] = photos
    
    utils.httpInvoke(uri, params)
    
def photoDelete(access_token, photoId):
    uri = '/user/photo/delete'
    params = {}
    params['access_token'] = access_token
    params['photoId'] = photoId
    
    utils.httpInvoke(uri, params)
    
def photoUpdate(access_token, photoId, originalUrl, thumbnailUrl):
    uri = '/user/photo/update'
    params = {}
    params['access_token'] = access_token
    params['photoId'] = photoId
    params['originalUrl'] = originalUrl
    params['thumbnailUrl'] = thumbnailUrl
    
    utils.httpInvoke(uri, params)
    
def photoList(access_token, userId):
    uri = '/user/photo/list'
    params = {}
    params['access_token'] = access_token
    params['userId'] = userId
    
    utils.httpInvoke(uri, params)

def test():
    photos = ''
    for i in range(210, 215, 1):
        photos = '[{originalUrl:"%s1.jpg",thumbnailUrl:"%s2.jpg"}]' % (i, i)
        photoAdd('7353cdd18d5b4eb59b4a9a714a366056', photos)

def roomAdd(access_token, roomId, roomAddress):
    uri = '/user/room/add'
    params = {}
    params['access_token'] = access_token
    params['roomId'] = roomId
    params['roomAddress'] = roomAddress
    
    utils.httpInvoke(uri, params)

def roomDelete(access_token, roomId):
    uri = '/user/room/delete'
    params = {}
    params['access_token'] = access_token
    params['roomId'] = roomId
    
    utils.httpInvoke(uri, params)

def roomList(access_token):
    uri = '/user/room/list'
    params = {}
    params['access_token'] = access_token
    
    utils.httpInvoke(uri, params)

if __name__ == '__main__':
    pass
access_token = '7353cdd18d5b4eb59b4a9a714a366056'
# test()
# avatarSet(access_token, '539b352bc1d5a109d720c78e')
# photoUpdate(access_token, "539b352bc1d5a109d720c78e", "1041111.jpg", "10421111.jpg")
# photoList(access_token, '')
#roomAdd(access_token, 21321321, '231231231@roomAddress')
roomDelete(access_token, "21321321")
roomList(access_token)

def a():
    pass