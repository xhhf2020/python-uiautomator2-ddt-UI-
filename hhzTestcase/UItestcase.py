#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 20:24
# @Author  : gaoxudong
# @File    : UItestcase.py
# @Software: PyCharm
import unittest
import ddt
from common.logger import LOG
from common.Elementway import Baseway
# from common.Initialization import getdada
from common.getxlrd import ExcelUtil
import warnings
from config.hhzconfig import connect
# testdata = getdada()
path = 'C:\\Users\\xhhf2\\PycharmProjects\\hhzUIAutomator2\\data\\casedaata.xlsx'
data = ExcelUtil(path)
testdata=data.dict_data()
@ddt.ddt
class TestHhzUi(unittest.TestCase):
    def setUp(self):
        self.imgs = []
        warnings.simplefilter("ignore", ResourceWarning)
        print('setUp')

    def add_img(self):
        self.d = connect()
        basedata=self.d.screenshot(format='base64')
        dedata=basedata.decode("utf-8")
        self.imgs.append(dedata)
        return True
    @ddt.data(*testdata)
    def test_hhzui(self, value):
        UItest = Baseway(value)
        yqString=value['Expected']
        LOG.info('inputdata> 执行步骤:%s,操作名称:%s，操作方法:%s ,元素:%s,参数:%s' % (value['Testscenarios'], value['Functioname'], value['Opmethod'], value['Pagelements'], value['inputparamete']))
        ResultString=UItest.Uiaototest()
        print(str(yqString),str(ResultString))
        self.check(yqString,ResultString)
        # try:
        #     self.assertEqual(str(qw),str(sj),'预期值和实际值不一致')
        # except Exception as e:
        #     self.add_img()
        #     raise AssertionError(e)
        #     # print('测试失败'+str(e))
            # raise
    def check(self, yqString, ResultString):
        try:
            self.assertEqual(str(yqString),str(ResultString),'预期值和实际值不一致')
        except Exception as e:
            self.add_img()
            raise AssertionError(e)