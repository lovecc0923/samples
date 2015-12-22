# -*- coding: UTF-8 -*-
'''
Created on 2014年11月17日

@author: Administrator
'''
# import wxPython
# from Tkinter import *
import wx

if __name__ == '__main__':
    pass
app = wx.App(False)  # Create a new app, don't redirect stdout/stderr to a window.
frame = wx.Frame(None, wx.ID_ANY, "Hello World")  # A Frame is a top-level window.
frame.Show(True)  # Show the frame.
app.MainLoop()