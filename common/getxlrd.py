#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/20 20:24
# @Author  : gaoxudong
# @File    : getxlrd.py
# @Software: PyCharm
import xlrd
class ExcelUtil():
    def __init__(self, excelPath):
        self.data = xlrd.open_workbook(excelPath)
    def dict_data(self):
        ddtdata = []
        me = self.data.sheet_names()
        for i in range(len(me)):
            sheetname=me[i]
            self.table = self.data.sheet_by_name(sheetname)
            # 获取第一行作为key值
            self.keys = self.table.row_values(0)
            # 获取总行数
            self.rowNum = self.table.nrows
            # 获取总列数
            self.colNum = self.table.ncols

            if self.rowNum <= 1:
                print("总行数小于1")
            else:
                k = 1
                for j in list(range(self.rowNum-1)):
                    sdict = {}
                    # 从第二行取对应values值
                    sdict['rowNum'] = j+2
                    values = self.table.row_values(k)
                    for x in list(range(self.colNum)):
                        sdict[self.keys[x]] = values[x]
                    if sdict['Y/N']=='Y':
                        ddtdata.append(sdict)
                    k += 1
        return ddtdata
if __name__ == "__main__":
    path='C:\\Users\\xhhf2\\PycharmProjects\\hhzUIAutomator2\\data\\casedaata.xlsx'
    data = ExcelUtil(path)
    print(data)
    print(data.dict_data())