# -*- coding: UTF-8 -*-
'''
Created on 2014��6��16��

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