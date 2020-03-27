#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/7/15 12:53
# @Author  : gaoxudong
# @File    : Elementway.py
# @Software: PyCharm
from common.Operationalelements import BaseOperate
op = BaseOperate()
class Baseway(object):
    def __init__(self, testdata):
        self.listid = testdata['id']
        self.listTestscenarios = testdata['Testscenarios']
        self.listFunctioname= testdata['Functioname']
        self.listOpmethod= testdata['Opmethod']
        self.listPagelements= testdata['Pagelements']
        self.listinputparamete=testdata['inputparamete']
        self.listgetparameters = testdata['getparameters']

    def Uiaototest(self):
        if self.listOpmethod =='ByIdclick':
            self.Element= self.listPagelements
            id=op.ByIdclick(self.Element)
            return id
        elif self.listOpmethod=='ByIdexistsclick':
            self.Element=self.listPagelements
            id=op.ByIdexistsclick(self.Element)
            return id
        elif self.listOpmethod=='ByIdTxtclick':
            self.Element=self.listPagelements
            self.paramete = self.listinputparamete
            id=op.ByIdTxtclick(self.Element,self.paramete )
            return id
        elif self.listOpmethod == 'ByIdsetvalue':
            self.Element = self.listPagelements
            self.paramete=self.listinputparamete
            va=op.ByIdsetvalue(self.Element,self.paramete)
            return va
        elif self.listOpmethod == 'setvalue':
            self.Element = self.listPagelements
            self.paramete=self.listinputparamete
            sv=op.setvalue(self.Element,self.paramete)
            return sv
        elif self.listOpmethod == 'textclick':
            self.Element = self.listPagelements
            op.textclick(self.Element)
        elif self.listOpmethod == 'classNameclick':
            self.Element = self.listPagelements
            op.classNameclick(self.Element)
        elif self.listOpmethod == 'xpathclick':
            self.Element = self.listPagelements
            xp=op.xpathclick(self.Element)
            return xp
        elif self.listOpmethod == 'getvalue':
            self.Element = self.listPagelements
            gv=op.getvalue(self.Element)
            return gv
        elif self.listOpmethod == 'clearvalue':
            self.Element = self.listPagelements
            cl=op.clearvalue(self.Element)
            return cl
        elif self.listOpmethod == 'gettoast':
            self.inputcs = self.listinputparamete
            toast=op.gettoast(self.inputcs)
            return toast
        elif self.listOpmethod == 'existsclick':
            self.Element = self.listPagelements
            elctxt=op.existsclick(self.Element)
            return  elctxt
        elif self.listOpmethod == 'swipeUp':
            self.inputcs = self.listinputparamete
            up=op.swipeUp(self.inputcs)
            return up
        elif self.listOpmethod == 'swipeDown':
            self.inputcs = self.listinputparamete
            Down=op.swipeDown(self.inputcs)
            return Down
        elif self.listOpmethod == 'swipLeft':
            self.inputcs = self.listinputparamete
            Left=op.swipLeft(self.inputcs)
            return Left
        elif self.listOpmethod == 'swipRight':
            self.inputcs = self.listinputparamete
            Right=op.swipRight(self.inputcs)
            return Right
        elif self.listOpmethod == 'press':
            self.Element = self.listPagelements
            self.paramete = self.listinputparamete
            pre=op.press( self.Element,self.paramete)
            return pre




