#coding=utf8
import os,sys
import datetime
import time
import numpy
from brain import newalldate,backnormal
from PCA import *
from Regression import loaddata,gradascent
from django.http import HttpResponse
from stock.models import  New_stock
from django.shortcuts import render_to_response
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
from pybrain.structure import SoftmaxLayer
from pybrain.structure import TanhLayer

def pybrain_high():
	back=[]
	alldate=New_stock.objects.filter().exclude(name='CIHKY')[0:100]
	wholelen=len(alldate)
	test=New_stock.objects.filter(name__contains="CIHKY")
	testlen=len(test)
	# test dateset
	testdata= SupervisedDataSet(5, 1)
	testwhole=newalldate(test,testlen)
	for i in testwhole:
		testdata.addSample((i[0],i[2],i[3],i[4],i[5]), (0,))	
	# 实验 dateset
	data= SupervisedDataSet(5, 1)
	wholedate=newalldate(alldate,wholelen)
	for i in wholedate:
		data.addSample((i[0],i[2],i[3],i[4],i[5]), (i[1]))	
	#print testwhole
	# 建立bp神经网络
	net = buildNetwork(5, 3, 1,bias=True,hiddenclass=TanhLayer, outclass=SoftmaxLayer)
	
	trainer = BackpropTrainer(net,data)
	trainer.trainEpochs(epochs=100)
	# train and test the network
#	print trainer.train()
	trainer.train()
	print 'ok'
	out=net.activateOnDataset(testdata)
	for j in  test:
                back.append((j.high))
	print back
	print out
	backout=backnormal(back,out)
	print 'okokokoko'
	print backout # 输出22的测试集合
	return out 
def Rgession():
	re_data=New_stock.objects.all()[0:1000]
	datamat,label=loaddata(re_data)
	weight=gradascent(datamat,label)
	print 'weight'
	return 	weight
def method(request):
	context={}
	knndata=[[0.833921748,0.560733679,0.381229963],[0.27499438,  0.346274739 ,0.353645499 ],[0.356473217,  0.430978784, 0.07547164]]
	testdata=[]
	test=New_stock.objects.filter(name__contains="CIHKY")[0:1]
	retest=New_stock.objects.filter(name__contains="CIHKY")[1:2]
	context['test']=test
	context['retest']=retest
	context['knn']=1#knndata
	#context['out']=pybrain_high()
	#out=Rgession()
	#context['weight']=out#out 里面为7个数组 每个数组有一个元素
	out=[2.98,2.0031,1.90,1.952,1.959,1.95,5.509]
	context['weight']=out
	for i in retest:
		testdata.append(1.0)
		testdata.append(float(i.high))
		testdata.append(float(i.low))
		testdata.append(float(i.close))
		testdata.append(float(i.open))
		testdata.append(float(i.adjclose))
		testdata.append(float(i.volume))
                label=abs(float(i.high)-float(i.low))/float(i.open)
                if label < 0.03:
			mubiaolable=1
                elif label <0.5:
			mubiaolable=2
                else:
			mubiaolable=3
	print 'mubiaoleibie' *4
	print mubiaolable
	print 'testdata'*10
	print testdata
	testlable=0
	for j in range(len(testdata)):
		testlable+=testdata[j]*out[j]
	print 'ceshi leibie'
	context['mubiaolable']=mubiaolable
	if testlable >1:
		testlable=1
	else:
		testlable=2
	context['testlable']=testlable 
	pcadata=New_stock.objects.filter(date__gte='2014-08-14',date__lte='2014-08-21')
	#pcadataarr=pcaloaddata(pcadata)
	#print 'pca'*10
	#lowmat,reconmat= testpca(pcadataarr,1)
	#print numpy.shape(lowmat)
	pca=[['open',4.04,67.33,67.33],['high',1.005,16.754,84.083],['low',0.955,15.915,99.998],['close',5.444e-5,0.001,99.999],[
'volue',3.77e-5,0.001,100],['adjclose',9.681e-6,0,100]]
	context['pca']=pca
        return render_to_response('method.html',context)

