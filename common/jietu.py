#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/26 10:40
# @Author  : gaoxudong
# @File    : jietu.py
# @Software: PyCharm
# coding: utf-8
import uiautomator2 as u2
class ScreenshotBase64(object):
    def __init__(self, d):
        self.d = d

    def screenshot_base64(self):
        import base64
        base64_data = base64.b64encode(self.d.screenshot(format='raw'))
        return base64_data


u2.plugin_register("screenshot_base64", ScreenshotBase64)

d = u2.connect('LNKREEMV99999999')
print (d.ext_screenshot_base64.screenshot_base64())