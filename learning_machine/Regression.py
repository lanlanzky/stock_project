#coding=utf8
import numpy
import math
from math import exp
# 利用线性回归来分析某一天股票的最小值 不需要进行数据归一化处理
# 分为三个类别 cha=high-low/open <0.03 无明显波动 0.03< <0.5 小范围波动 >0.5 波动比较大
def sigmoid(inX):
	return 1.0/(1+exp(-inX))
#New_stock.object.all()[0:10]
def loaddata(reobject):
	datamat=[];labelmat=[]
	for i in reobject:
		datamat.append([1.0,float(i.high),float(i.low),float(i.close),float(i.open),float(i.adjclose),float(i.volume)])
		label=abs(float(i.high)-float(i.low))/float(i.open)
		if label < 0.03:
			labelmat.append(1)
		elif label <0.5:
			labelmat.append(2)
		else:
			labelmat.append(3)
	return datamat,labelmat 
		
def gradascent(datamatin,classlabels):
	datamtrix=numpy.mat(datamatin)
	labelmat=(numpy.mat(classlabels)).transpose()
	m,n=numpy.shape(datamtrix)
	alpha=0.001
	maxcyclass=500
	weights=numpy.ones((n,1))
	for k in range(maxcyclass):
		test=datamtrix*weights
		h=[]
		for i in test:
			for j in i:
				b=[]
				b.append(sigmoid(j))
			h.append(b)
		error=(labelmat-h)
		weights+=alpha*datamtrix.transpose()*error
	return weights
