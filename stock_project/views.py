#coding=utf8
import os,sys
import datetime
import time
from django.http import HttpResponse
from django.shortcuts import render_to_response
import datetime
from stock.models import New_stock
from data.stockcode import datatomysql
from pybrain.datasets import SupervisedDataSet
from pybrain.tools.shortcuts import buildNetwork
from pybrain.supervised.trainers import BackpropTrainer
def index(request):
        return render_to_response('index.html')
def bigdata(request):
        return render_to_response('bigdata.html')
def stock(request):
	context={}
	codename=['GOOG','QIHU','SOHU','SINA','NCTY','PWRD','CTRP','JOBS','LONG','UTSI','CNTF','SMI','VIMC','ACTS','EDU','HMIN','VISN','EJ','AMCN','ACH','CEO']
        now = datetime.datetime.now()
        #print "asdfasdfasda\n" * 10 
        #dates=datatomysql()
        #stock_data=New_stock.objects.all()
	context['codename']=codename
	return render_to_response('stock.html', context)
def strtodatetime(datestr,format="%Y-%m-%d"):      
    	da=time.strptime(datestr,format) 
	return time.strftime(format,da)
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
    	start=starttime[-4:]+'-'+context[starttime[3:-5]]+'-'+starttime[0:2]
    	end=endtime[-4:]+'-'+context[endtime[3:-5]]+'-'+endtime[0:2]
    	context['start']=start
    	context['end']=end
     	try:
    	 	search_stock=New_stock.objects.filter(name=code_name).exclude(date__gte='%s' %(end)).filter(date__gte='%s' %(start))
    		context['search_stock']=search_stock
		context['length']=search_stock.__len__()
    		return render_to_response('search.html', context)
	except Exception as e:
		print e
    else:
    	return render_to_response('search.html','YOU must submit the informations:')
