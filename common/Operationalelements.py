#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 14:39
# @Author  : gaoxudong
# @File    : Operationalelements.py
# @Software: PyCharm
import time
from config.config_T import imagepath
from common.creatfdir import creatdir
from config.hhzconfig import star_app
from config.hhzconfig import connect
class BaseOperate(object):
    def __init__(self):
        self.d = connect()
        self.d.healthcheck()
        self.d.screen_on()
        time.sleep(3)
        self.d.swipe_points([(0.485, 0.708), (0.481, 0.286)], 0.05)  # 滑动解锁界面
        star_app('com.hzhu.m')
        sess = self.d .session('com.hzhu.m')
        sess.running()  #
#点击
    def textclick(self,txt):
        self.d(text=txt).click(timeout=5)
    def texexists(self,txt):
        txt=self.d(text=txt).exists(timeout=5)
        if txt==True:
            return txt
        else:
            return False
    def ByIdexists(self,id):
        id=self.d(resourceId=id).exists(timeout=5)
        if id==True:
            return True
        else:
            return False
    def ByIdclick(self,id):
        self.d(resourceId=id).click()

    def ByIdexistsclick(self,id):
        id=self.d(resourceId=id).click_exists(timeout=5)
        if id==True:
            return id
        else:
           return False

    def ByIdTxtclick(self, id,txt):
        id = self.d(resourceId=id, text=txt).click_exists(timeout=5)
        if id == True:
            return id
        else:
            return False
    def ByIdsetvalue(self,id,value):
        if self.ByIdexists(id)==True:
            self.d(resourceId=id).send_keys(value)
            return True
        else:
            return False
    def classNameclick(self,className):
        self.d(className=className).click(timeout=5)
    def xpathclick(self,xpath):
        self.d.xpath(xpath).wait(10.0)
        if self.d.xpath(xpath).exists:
            self.d.xpath(xpath).click()
            return True
        else:
            return False
    #获取元素值
    def getvalue(self,txt):
        gettxt=self.d(text=txt).get_text()
        if gettxt:
            return gettxt
        else:
            return False
            #给元素输入值
    def setvalue(self,gtxt,stxt):
        if self.texexists(gtxt):
            self.d(text=gtxt).set_text(stxt)
            return True
        else:
            return False
    #清除元素的值
    def clearvalue(self,ctxt):
        ct=self.texexists(ctxt)
        if ct==True:
            self.d(text=ctxt).clear_text()
            return True
        else:
            return False
    #滚动操作
    def scroll(self):
        self.d(scrollable=True).scroll.vert.backward() # b.向下滑动：
        self.d(scrollable=True).scroll.horiz.forward(steps=50)#c.水平向右滚动：
        self.d(scrollable=True).scroll.horiz.backward(steps=50)#d.水平向左滚动：
        self.d(scrollable=True).scroll.horiz.toBeginning(steps=100,max_swipes=1000) #e.水平滑动到最左边：
        self.d(scrollable=True).scroll.horiz.toEnd(steps=100, max_swipes=1000)# f.水平滑动到最右边：
        self.d(scrollable=True).scroll.toEnd() #g.竖直滑动到结尾：
        self.d(scrollable=True).scroll.toBeginning(steps=50)#    h.竖直滑动到开头：
        self.d(scrollable=True).scroll.to(text ='测试')#i.滑动到指定位置（测试）
    #获取 toast
    def gettoast(self,toast):
        toasttxt=self.d.toast.get_message(5.0, 10.0)
        if toasttxt:
            return toasttxt
        else:
            return  False
        #assert "发布成功1" in d.toast.get_message(5.0, )
    #文案存在后点击
    def existsclick(self,txt):
        elctxt= self.d(text=txt).click_exists(timeout=5.0)
        if elctxt==True:
            return elctxt
        else:
            return False
    #根据描述点击
    def descriptionclick(self,txt):
        self.d(description=txt).click()
    #截图
    def screenshot(self):
        st = time.strftime("%Y-%m-%d_%H-%M-%S")
        shotph = creatdir(imagepath)
        filename = shotph + "\%s.jpg" % st  # 修改截图文件的存放路径为相对路径
        self.d.screenshot(filename)
        print(filename)


    def add_img(self):
        self.d = connect()
        basedata=self.d.screenshot(format='base64')
        dedata=basedata.decode("utf-8")
        self.imgs.append(dedata)
    # 等待元素的出现
    def waitele(self,txt):
        eletxt= self.d(text=txt).wait(timeout=10.0)
        return eletxt
    def getSize(self):
        u"获取屏幕大小"
        x=self.d.window_size()[0]
        y=self.d.window_size()[1]
        return (x, y)
    # 屏幕向上滑动
    def swipeUp(self,frequency):
        frequency=int(frequency)
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.75)  # 起始y坐标
        y2 = int(l[1] * 0.25)  # 终点y坐标
        for i in range(0,frequency):
            time.sleep(1)
            self.d.swipe(x1, y1, x1, y2)
        return True
    def swipLeft(self,frequency):
        '''屏幕向左滑动'''
        frequency = int(frequency)
        l = self.getSize()
        x1 = int(l[0] * 0.75)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.05)
        for i in range(0, frequency):
            time.sleep(1)
            self.d.swipe(x1, y1, x2, y1)
        return True
    # 屏幕向右滑动
    def swipRight(self,frequency):
        frequency = int(frequency)
        '''屏幕向右滑动'''
        l = self.getSize()
        x1 = int(l[0] * 0.05)
        y1 = int(l[1] * 0.5)
        x2 = int(l[0] * 0.75)
        for i in range(0, frequency):
            time.sleep(1)
            self.d.swipe(x1, y1, x2, y1)
        return True

    def swipeDown(self,frequency):
        frequency = int(frequency)
        '''屏幕向下滑动'''
        l = self.getSize()
        x1 = int(l[0] * 0.5)  # x坐标
        y1 = int(l[1] * 0.25)  # 起始y坐标
        y2 = int(l[1] * 0.75)  # 终点y坐标
        for i in range(0, frequency):
            time.sleep(1)
            self.d.swipe(x1, y1, x1, y2)
        return True
    def press(self, pressback,frequency):
        frequency = int(frequency)
        for i in range(0, frequency):
            time.sleep(1)
            self.d.press(pressback)
        return True

#SwipeExt扩展功能
    def swipe_ext(self,way):
        self.d.swipe_ext(way)  # 屏幕右滑，4选1 "left", "right", "up", "down"
        self.d.swipe_ext(way, scale=0.9)  # 默认0.9, 滑动距离为屏幕宽度的90%
        self.d.swipe_ext(way, box=(0, 0, 100, 100))  # 在 (0,0) -> (100, 100) 这个区域做滑动