# -*- coding: UTF-8 -*-
'''
Created on 2014年6月24日

@author: Administrator
'''

import urllib, urllib2, utils



if __name__ == '__main__':
    pass
# http://api.map.baidu.com/location/ip?ak=OuLCe9EHc0v6Ik5BiAE4oxfN
# response = urllib2.urlopen('http://api.map.baidu.com/location/ip?ak=%s' % 'OuLCe9EHc0v6Ik5BiAE4oxfN', None, 30)
# body = response.read()
# print body

url = 'http://api.map.baidu.com/geodata/v3/poi/create'
 
params = {}
# params['title'] = '2560682.35'
# params['address'] = '2560682.35'
params['latitude'] = 22.634549
params['longitude'] = 114.087448
params['coord_type'] = 3
params['geotable_id'] = '59906'
params['ak'] = 'OuLCe9EHc0v6Ik5BiAE4oxfN'
params['userId'] = 100281
params['nickname'] = '小灿'
params['description'] = '蛋疼！！！'
params['birthday'] = '19989-10-26'
params['sex'] = 1
params['avatar'] = 'http://tb1.bdstatic.com/tb/cms/ls06201.jpg'
 
data = urllib.urlencode(params)
response = urllib2.urlopen(url, data, 30)
body = response.read()

print body.decode('unicode_escape')
