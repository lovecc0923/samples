# -*- coding: UTF-8 -*-
'''
Created on 2014年11月21日

@author: Administrator
'''

import utils, Test, json

if __name__ == '__main__':
    pass
    uri = '/exam/get'
    params = {}
    params['access_token'] = Test.User.getAccessToken('18908983800', utils.md5('123456'))
    params['examId'] = 19
    
    utils.httpInvoke(uri, params)
    
    
    
