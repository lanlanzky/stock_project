#coding=utf8
# Create your views here.
import os,sys
from django.http import HttpResponse
from byes import testbyes
from kmeans import kMeans
from stock.models import  New_stock
from django.shortcuts import render_to_response
#afrom decision-tree import testdeciton
def cluster(request):
	context={}
	lables=[1,2,3]
	knndata=[[0.833921748,0.560733679,0.381229963,1,1],[0.27499438,  0.346274739 ,0.353645499,2,2 ],[0.356473217,  0.430978784, 0.07547164,3,3]]
	context['knn']=knndata
	context['lables']=lables
	#下面是决策树的数据
	#testdata=testdeciton()
	testdata=[['presbyopic', 'hyper', 'no', 'normal', 'soft', 'soft'], ['presbyopic', 'hyper', 'yes', 'reduced', 'no-lenses', 'no-lenses'], ['presbyopic', 'hyper', 'yes', 'normal', 'no-lenses', 'no-lenses']]
	context['deci']=testdata
	suxing=['age','prescript','astigmatic','terarfate']
        newstock=New_stock.objects.filter(name='CEO')
	#以下是贝叶斯
	lajifenlei={1:'spam',0:'ham'}
	testEntry=[['love my dalmation'],['stupid garbage']]
	print 'test'*10
	byeslei=[]
	for i in testbyes(testEntry):
		byeslei.append(lajifenlei[i])
	print byeslei
	context['byeslei']=byeslei
	context['byestest']=testEntry
	byes=[['love my dalmation','ham','ham'],['stupid garbage','spam','spam']]
	context['byes']=byes
	#以下是smo-svm
	svm=[[7.551510,	-1.580030,1,1],	[2.114999,	-0.004466,-1,-1]]
	context['svm']=svm
	# 以下是kmeans聚类算法
	kmeans=kMeans(1)#K值为4
	#print kmeans[0,0] #返回的是一个矩阵 这样取第一行第一列的元素
	kmeandata=[kmeans[0,0],kmeans[0,1]]
	context['kmeans']=kmeandata
        return render_to_response('cluster.html', context)

