#coding=utf8
from numpy import *
from django.http import HttpResponse
from django.shortcuts import render_to_response
from stock.models import New_stock 
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
#归一化函数处理
def normal(record):
        return [ "%.5f" % round(float((i-min(record)))/(max(record)-min(record)),4) for i in record]
#测试数据归一化
test=New_stock.objects.filter(name__contains="CIHKY")
#实验数据归一化处理
context={}
allopen=[]
allhigh=[]
alllow=[]
allclose=[]
allvolumn=[]
alladjclose=[]
alldate=New_stock.objects.filter().exclude(name='CIHKY')[0:100]
for date in  alldate:
        allopen.append(date.open)
        allhigh.append(date.high)
        alllow.append(date.low)
        allclose.append(date.close)
        allvolumn.append(date.volume)
        alladjclose.append(date.adjclose)
def newalldate():

        newallopen=normal([ float(i)  for i in allopen])
        newallhigh=normal([ float(i)  for i in allhigh])
        newalllow=normal([ float(i)  for i in alllow])
        newallclose=normal([ float(i)  for i in allclose])
        newallvolume=normal([ float(i)  for i in allvolumn])
        newalladjclose=normal([ float(i)  for i in alladjclose])
        newalldate=[]
        for i in range(10):
                test=[]
                test.append(newallopen[i])
                test.append(newallhigh[i])
                test.append(newalllow[i])
                test.append(newallclose[i])
                test.append(newallvolume[i])
                test.append(newalladjclose[i])
                newalldate.append(test)
	return newalldate
# 用神经网络来预测最大值
# 用神经网络来预测最小值
