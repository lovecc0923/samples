# -*- coding: UTF-8 -*-
'''
Created on 2015年8月14日

@author: Administrator
'''

import utils, json


class GZ:
    
    @staticmethod
    def SendSms(telephone):
        uri = '/sendSms'
        
        params = {}
        params['telephone'] = telephone
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
    
class Auth:
    def __init__(self):
        pass
    
    @staticmethod
    def GetAccessToken(telephone, password, version):
        uri = '/user/login'
        
        params = {}
        params['telephone'] = telephone
        params['password'] = utils.md5(password)
        params['version'] = version
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        if obj["resultCode"] == 1:
            return obj["data"]["access_token"]
        else:
            return ""
        
    @staticmethod
    def Verify(telephone):
        uri = '/verify'
        
        params = {}
        params['telephone'] = telephone
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        
        return obj["resultCode"] == 1
    
    @staticmethod
    def Register(telephone, password):
        uri = '/user/register'
        
        params = {}
        params['telephone'] = telephone
        params['randcode'] = '137764'
        params['password'] = utils.md5(password)
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
    
    @staticmethod
    def Login(telephone, password, version):
        uri = '/user/login'
        
        params = {}
        params['telephone'] = telephone
        params['password'] = utils.md5(password)
        params['version'] = version
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1   
    
    @staticmethod
    def LoginAuto(access_token, version):
        uri = '/user/login/auto'
        
        params = {}
        params['access_token'] = access_token
        params['version'] = version
        params['serial'] = ''
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
    
    @staticmethod
    def Logout(access_token, version):
        uri = '/user/login/auto'
        
        params = {}
        params['access_token'] = access_token
        params['version'] = version
        params['serial'] = ''
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
    
    @staticmethod
    def UpdatePassword(access_token, oldPassword, newPassword):
        uri = '/user/password/update'
        
        params = {}
        params['access_token'] = access_token
        params['oldPassword'] = utils.md5(oldPassword)
        params['newPassword'] = utils.md5(newPassword)
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
    
    @staticmethod
    def ResetPassword(telephone, randcode, newPassword):
        uri = '/user/password/reset'
        
        params = {}
        params['telephone'] = telephone
        params['randcode'] = randcode
        params['newPassword'] = utils.md5(newPassword)
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1   

class User:
    @staticmethod
    def Update(version, access_token):
        uri = '/user/update'
        
        if 1 == version:
            params = {}
            params['access_token'] = access_token
            params['name'] = '罗融春'
            params['sex'] = 1
            params['degree'] = 10
            params['workTime'] = 10
            params['weixin'] = 'luorongchunwl123'
            
            s = utils.httpInvoke(uri, params)
            obj = json.loads(s)
            return obj["resultCode"] == 1
        elif 2 == version:
            uri = '/user/update'
        
            params = {}
            params['access_token'] = access_token
            params['name'] = '罗罗罗'
            params['weixin'] = 'luorongchun'
            params['shortName'] = '视酷科技'
            params['jobName'] = '打杂'
            params['tags[0]'] = '标签3'
            params['tags[1]'] = '标签4'
            params['tags[2]'] = '标签5'
            params['tags[3]'] = '不加班'
            params['tags[4]'] = '不打卡'
            params['forte'] = '创业公司。。。。。。。。。。。。'
            params['companyName'] = '视酷信息技术有限公司'
            params['website'] = 'www.shiku.co'
            params['address'] = '宝安区龙华大浪街道和平路与布龙路交汇处西南角(地铁4号线龙胜站A、D出口)和平里花园1期3A栋702室 '
            
            s = utils.httpInvoke(uri, params)
            obj = json.loads(s)
            return obj["resultCode"] == 1
        else:
            print ''
    
    @staticmethod
    def GetUser(access_token, userId=''):
        pass
        uri = '/user/get'
        
        params = {}
        params['access_token'] = access_token
        params['userId'] = userId
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
    
    @staticmethod
    def ResumeUpdate(access_token):
        uri = '/resume/update'
        
        params = {}
        params['access_token'] = access_token
#         params['name'] = '罗融春'
#         params['sex'] = 1
#         params['degree'] = 10
#         params['workTime'] = 10
#         params['fnId'] = 10123
#         params['salary'] = 11101
#         params['cityId'] = 123
#         params['jobStatus'] = 1
#         params['tags'] = '["牛B", "叼炸天"]'
#         params['forte'] = '20几年工作经验，油条的很。。。'
        params['workList'] = '[{"fnId": 121312313,"industryId": 312312312,"natureId": 12312312,"scaleId": 31231231,"companyName": "大公司","department": "随便部门","desc": "吃饭、睡觉。。。","begin": 12,"end": 12,"hideMe": 1}]'
#         params['eduList'] = '[{"name": "野鸡大学123","major": 123,"majorText": "什么值专业啊？？？","majorDesc": "随便搞搞","degree": 123,"isForeign": 1,"begin": 123,"end": 123}]'
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
    @staticmethod
    def ResumeGet(access_token):
        uri = '/resume/get'
        
        params = {}
        params['access_token'] = access_token
        
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
    
    @staticmethod
    def UpdateChannelId(access_token):
        uri = '/user/channelId/set'
        
        params = {}
        params['access_token'] = access_token
        params['channelId'] = '4372374992767857630'
        params['device'] = 3
          
        s = utils.httpInvoke(uri, params)
        obj = json.loads(s)
        return obj["resultCode"] == 1
        
     
if __name__ == '__main__':
    pass

  
#     telephone = '17708450921'
#     password = 'bbb'
#     version = 1
    
    telephone = '18637647279'
    password = '123456'
    version = 1  
    # 手机号码未注册
    if Auth.Verify(telephone):
        # 请求短信验证码
        # Auth.SendSms(telephone)
        # 注册帐号
        Auth.Register(telephone, password)
    else:
        access_token = Auth.GetAccessToken(telephone, password, version)
        User.UpdateChannelId(access_token)
#         User.Update(1, access_token)
#         User.LoginAuto('1232131', version)
#         User.ResumeUpdate(access_token)
#         User.GetUser(access_token)
#         User.GetUser(access_token, 100032)
#         Auth.UpdatePassword(access_token, 'qqq', 'bbb');
#         Auth.ResetPassword('17708450926', '123456', 'qqq');
#         # 个人用户资料更新
#         User.Update(1, access_token)
#         # 企业用户资料更新
#         access_token = Auth.GetAccessToken('17708450926', 'bbb', 2)
#         User.Update(2, access_token)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
