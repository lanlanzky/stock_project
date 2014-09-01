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
#返归一化
def backnormal(backdata,outdata):
        large=max(backdata)
        small=min(backdata)
        bizhi=large-small
        for i in range(len(outdata)):
                for j in range(len(outdata[1])):
                        outdata[i][j]=outdata[i][j]*bizhi+small
	return outdata
			
	
#实验数据归一化处理
def newalldate(alldate,len):
        newalldate=[]
	allopen=[]
	allhigh=[]
	alllow=[]
	allclose=[]
	allvolumn=[]
	alladjclose=[]
	for date in  alldate:
        	allopen.append(date.open)
       	 	allhigh.append(date.high)
        	alllow.append(date.low)
        	allclose.append(date.close)
        	allvolumn.append(date.volume)
        	alladjclose.append(date.adjclose)
        newallopen=normal([ float(i)  for i in allopen])
        newallhigh=normal([ float(i)  for i in allhigh])
        newalllow=normal([ float(i)  for i in alllow])
        newallclose=normal([ float(i)  for i in allclose])
        newallvolume=normal([ float(i)  for i in allvolumn])
        newalladjclose=normal([ float(i)  for i in alladjclose])
        for i in range(len):
                new=[]
                new.append(newallopen[i])
                new.append(newallhigh[i])
                new.append(newalllow[i])
                new.append(newallclose[i])
                new.append(newallvolume[i])
                new.append(newalladjclose[i])
                newalldate.append(new)
	return newalldate
# 用神经网络来预测最大值
# 用神经网络来预测最小值
