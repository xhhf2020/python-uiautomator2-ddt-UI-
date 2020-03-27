#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 20:24
# @Author  : gaoxudong
# @File    : report.py
# @Software: PyCharm
import datetime
from common.creatfdir import creatdir
from config.config_T import filePath
import os.path
import time
def CreateReprt():
    #生成报告的Title,描述
    ReportTime=datetime.datetime.now()
    ReportTime=str(ReportTime.strftime('%Y-%m-%d-%H-%M-%S'))
    Folderpath = creatdir(filePath)
    filepath = os.path.join(Folderpath + '/Report'+ReportTime+'.html')
    filename=filepath
    fp = open(filename, 'wb')
    return fp
    #fp.close()


