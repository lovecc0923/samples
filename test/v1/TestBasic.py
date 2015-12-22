# -*- coding: UTF-8 -*-
'''
Created on 2014Äê6ÔÂ16ÈÕ

@author: Administrator
'''

import utils

def sendSms(telephone):
    uri = '/basic/randcode/sendSms'
    params = {}
    params['telephone'] = telephone
    
    utils.httpInvoke(uri, params)

if __name__ == '__main__':
    pass
sendSms('18908983800')