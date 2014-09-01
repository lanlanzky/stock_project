#coding=utf8
import os,sys
import datetime
import time
from django.http import HttpResponse
from django.shortcuts import render_to_response
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
def information(request):
	context={}
	context['info']='information'
        return render_to_response('information.html',context)
	'''
def search(request):
    context={}
    context['April']='04'
    context['Janurary']='01'
    context['February']='02'
    context['March']='03'
    context['May']='05'
    context['June']='06'
    context['July']='07'
    context['August']='08'
    context['September']='09'
    context['October']='10'
    context['November']='11'
    context['December']='12'
    code_name=request.GET.get('stock_code', '')
    context['code']=code_name
    starttime=request.GET.get('start', '')
    starttime=str(starttime)
    endtime=request.GET.get('end', '')
    endtime=str(endtime)
    if code_name and starttime and endtime:
        starttime = starttime.strip()
        endtime= endtime.strip()
    	starttime=starttime[-4:]+'-'+context[starttime[3:-5]]+'-'+starttime[0:2]
    	endtime=endtime[-4:]+'-'+context[endtime[3:-5]]+'-'+endtime[0:2]
    	context['start']=starttime
    	context['end']=endtime
	print starttime
	print type(starttime)
	print len(starttime)
     	try:
     		search_stock=New_stock.objects.filter(name=code_name).exclude(date__gte='%s' %(endtime)).filter(date__gte='%s' %(starttime))
    		context['search_stock']=search_stock
		context['length']=search_stock.__len__()
    		return render_to_response('search.html', context)
	except Exception as e:
		print e
    else:
    	return render_to_response('search.html','YOU must submit the informations:')
	'''
