#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/17 16:33
# @Author  : gaoxudong
# @File    : hhzconfig.py
# @Software: PyCharm
import time
import uiautomator2 as u2
def connect():
    d = u2.connect_adb_wifi("172.16.222.55:5555")
    # d.healthcheck()
    d.settings['xpath_debug'] = True  # 开启xpath插件的调试功能
    d.settings['wait_timeout'] = 20.0  # 默认控件等待时间（原生操作，xpath插件的等待时间）
    return d
def star_app(pkg):
    d=connect()
    d.toast.show("正在启动app")
    d.app_start('com.hzhu.m', stop=True)  # 启动应用前停止应用
    d.app_start(pkg)
    time.sleep(2)
def app_stop(pkg):
    d = connect()
    d.app_stop(pkg)
    pkginfo=d.app_info("com.hzhu.m")
    sbingo=d.device_info
    sess = d.session('com.hzhu.m')
    sess.close()
    time.sleep(2)
    return pkginfo,sbingo


