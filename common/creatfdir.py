#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/3/18 17:37
# @Author  : gaoxudong
# @File    : creatfdir.py
# @Software: PyCharm

import os.path
import time
def creatdir(filePath):
    # 系统当前时间年份
    year = time.strftime('%Y', time.localtime(time.time()))
    # 月份
    month = time.strftime('%m', time.localtime(time.time()))
    # 日期
    day = time.strftime('%d', time.localtime(time.time()))
    # 具体时间 小时分钟毫秒
    fileYear = filePath + year + month
    fileMonth = fileYear + '\\' + year + month + day
    if not os.path.exists(fileYear):
        os.mkdir(fileYear)
        os.mkdir(fileMonth)
    else:
        if not os.path.exists(fileMonth):
            os.mkdir(fileMonth)
    fileDir = fileMonth
    return fileDir
