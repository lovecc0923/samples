# -*- coding: UTF-8 -*-
'''
Created on 2014年6月24日

@author: luorc
'''

import Test, utils


def buyBizGoods():
    access_token = Test.User.getAccessToken('18908983800', 'qqq')
    
    uri = '/biz_goods/buy'
    params = {}
    params['access_token'] = access_token
    params['goodsId'] = 7
             
    utils.httpInvoke(uri, params)
    
def buyBizGoods2():
    access_token = Test.User.getAccessToken('18503054766', '123456')
  
    uri = '/biz_goods/buy'
    params = {}
    params['access_token'] = access_token
    params['goodsId'] = 7
             
    utils.httpInvoke(uri, params)
    
def goodsList(access_token):
    uri = '/pay_goods/list'
    params = {}
    params['access_token'] = access_token
             
    utils.httpInvoke(uri, params)
     
    uri = '/biz_goods/list'
    params = {}
    params['access_token'] = access_token
             
    utils.httpInvoke(uri, params)
     
    uri = '/exam_goods/list'
    params = {}
    params['access_token'] = access_token
             
    utils.httpInvoke(uri, params) 
def get():
    access_token = Test.User.getAccessToken('18503054711', '123456')
    
    uri = '/company/get'
    params = {}
    params['access_token'] = access_token
    params['companyId'] = 1
              
    utils.httpInvoke(uri, params)
    
    uri = '/company/get/simple'
    params = {}
    params['access_token'] = access_token
              
    utils.httpInvoke(uri, params)

def nearby():
    access_token = Test.User.getAccessToken('18908983800', 'qqq')
        
    uri = '/nearby/company'
    params = {}
    params['access_token'] = access_token
    params['longitude'] = 114.054872
    params['latitude'] = 22.607732
                  
    utils.httpInvoke(uri, params)
    
    uri = '/nearby/job'
    params = {}
    params['access_token'] = access_token
    params['longitude'] = 114.054872
    params['latitude'] = 22.607732
                  
    utils.httpInvoke(uri, params)

if __name__ == '__main__':
    pass

    access_token = Test.User.getAccessToken('18908983899', 'qqq')
    goodsList(access_token)
    uri = '/company/exam/list'
    params = {}
    params['access_token'] = access_token
    params['type'] = 0
    utils.httpInvoke(uri, params)


# 
# uri = '/exam_goods/buy'
# params = {}
# params['access_token'] = access_token
# params['text'] = '[15]'
# utils.httpInvoke(uri, params)

# get()
# access_token = Test.User.getAccessToken('18503054766', '123456')
# goodsList(access_token)


# uri = '/pay_goods/buy'
# params = {}
# params['access_token'] = access_token
# params['rechargeType'] = 2
# params['goodsId'] = 2
#           
# utils.httpInvoke(uri, params)

# buyBizGoods()
# buyBizGoods2()


# Test.Company.jobList(access_token)
# Test.Company.examList(access_token)
# Test.Goods.goodsList(access_token)



# uri = '/pay/callback'
# params = {}
# params['access_token'] = access_token
# params['nickname'] = '97'
# params['pageSize'] = 10
#        
# utils.httpInvoke(uri, params)













