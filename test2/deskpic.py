# -*- coding: utf-8 -*-
import urllib.request
import time
import os
import re
from PIL import Image
import win32api
import win32gui
import win32con

from datetime import datetime, date, timedelta


class BingPic:
    def __init__(self):
        self.bgImageUrl = ''
        self.localFileName = ''
        self.localBMPFileName = ''

    def createLocalFileName(self):

        path = 'D:/python-workpace/test2/pic/pic'
        if not os.path.exists(path):
            os.mkdir(path)
        randomStr = time.strftime("%Y%m%d", time.localtime())
        self.localFileName = path + randomStr + '.jpg'
        self.localBMPFileName = path + randomStr + '.bmp'

    def downloadImage(self):
        if self.localFileName == '':
            self.createLocalFileName()

        req = urllib.request.Request("http://cn.bing.com/HPImageArchive.aspx?idx=0&n=1")
        webpage = urllib.request.urlopen(req)
        content = str(webpage.read())
        url_tail = re.search(r'<url>[^\s]*</url>', content)
        path = 'http://cn.bing.com' + str(url_tail.group())[5:-6]
        urllib.request.urlretrieve(path, self.localFileName)

    def updateBGImage(self):
        img = Image.open(self.localFileName)
        img.save(self.localBMPFileName)
        os.remove(self.localFileName)
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, self.localBMPFileName, 1 + 2)

    def setBGImageByDate(self):
        # path = 'D:/python-workpace/test2/pic/pic'
        # if not os.path.exists(path):
        #     os.mkdir(path)
        # randomStr = (date.today() + timedelta(days=-1)).strftime("%Y%m%d")
        # self.localBMPFileName = path + randomStr + '.bmp'
        win32gui.SystemParametersInfo(win32con.SPI_SETDESKWALLPAPER, self.localBMPFileName, 1 + 2)

    def popupBox(self):
        import tkinter
        import traceback

        global mySlef;

        def inputint():
            nonlocal num
            try:
                num = int(var.get().strip())
                path = 'D:/python-workpace/test2/pic/pic'
                mySlef.localBMPFileName = path + str(num) + '.bmp'
                mySlef.setBGImageByDate()
            except:
                num = 'Not a valid integer.'
                traceback.print_exc()

        def inputclear():
            nonlocal num
            var.set('')
            num = ''

        mySlef = self;
        num = 0
        root = tkinter.Tk(className='有种你就输入日期')  # 弹出框框名

        # root.geometry('270x120')  # 设置弹出框的大小 w x h

        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        size = '%dx%d+%d+%d' % (270, 120, (screenwidth - 270) / 2, (screenheight - 120) / 2)
        print(size)
        root.geometry(size)



        var = tkinter.StringVar()  # 这即是输入框中的内容
        var.set('')  # 通过var.get()/var.set() 来 获取/设置var的值

        entry1 = tkinter.Entry(root, textvariable=var)  # 设置"文本变量"为var
        entry1.pack()  # 将entry"打上去"
        btn1 = tkinter.Button(root, text='Input', command=inputint)  # 按下此按钮(Input), 触发inputint函数
        btn2 = tkinter.Button(root, text='Clear', command=inputclear)  # 按下此按钮(Clear), 触发inputclear函数


        # 按钮定位
        btn2.pack(side='right')
        btn1.pack(side='right')

        btn1.focus_set()


        # 上述完成之后, 开始真正弹出弹出框
        root.mainloop()


if __name__ == '__main__':
    stealBing = BingPic()
    stealBing.downloadImage()
    stealBing.updateBGImage()

    # stealBing.popupBox()
