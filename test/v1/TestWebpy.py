# -*- coding: UTF-8 -*-
'''
Created on 2014年10月23日

@author: Administrator
'''

import webpy

mapping = ('/hello', 'hello', '/view/(\d+)', 'View')
 
class hello(object):
    def GET(self):
        return 'hello world'

class View(object):
    def GET(self, args1):
        params = webpy.input()
        print params
        print args1
        return "1"
    
 
if __name__ == "__main__":
    app = webpy.application(mapping, globals())
    app.run()
