#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 20:24
# @Author  : gaoxudong
# @File    : UItestcase.py
# @Software: PyCharm
import unittest
import time
# import HTMLTestRunner
from HTMLTestRunner_Chart import HTMLTestRunner
from common.report import CreateReprt
from common.logger import logger
from config.config_T import test_suite_dir
from common.Sendmail import send_mail
from config.hhzconfig import app_stop
@logger('开始测试')
def creatsuite():
    testunit = unittest.TestSuite()
    discover = unittest.defaultTestLoader.discover(test_suite_dir, pattern = 'UItest*.py', top_level_dir = None)
    for test_suite in discover:
        for test_case in test_suite:
            testunit.addTests(test_case)
    return testunit
if __name__ == '__main__':
    fp = CreateReprt()
    runner = HTMLTestRunner(stream=fp, title='hahaozhuapp UI自动化测试例结果', description='测试例执行结果')
    allcase=creatsuite()
    runner.run(allcase)
    fp.close()
    x,y=app_stop('com.hzhu.m')
    # 优化格式化化版本
    timestring = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    send_mail('本次UI自动化安卓app测试完成'+'\n'+'完成时间：'+timestring+'\n'+'【测试包信息】'+'\n'+str(x)+'\n'+'【设备信息】'+'\n'+str(y)+'\n')

