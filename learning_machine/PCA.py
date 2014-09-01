#coding=utf8
#分析数据的最主要的关键元素
import os
from numpy import *
def pcaloaddata(pcalist):
	dataarr=[]
	for i in pcalist:
		every=[]
		every.append(float(i.open))
		every.append(float(i.high))
		every.append(float(i.low))
		every.append(float(i.close))
		every.append(float(i.volume))
		every.append(float(i.adjclose))
		dataarr.append(every)
	return dataarr
def testpca(dataMat, topNfeat=99999):
	meanVals = mean(dataMat, axis=0)
	meanRemoved = dataMat - meanVals #remove mean
	covMat = cov(meanRemoved, rowvar=0)
	eigVals,eigVects = linalg.eig(mat(covMat))
	eigValInd = argsort(eigVals)            #sort, sort goes smallest to largest
	eigValInd = eigValInd[:-(topNfeat+1):-1]  #cut off unwanted dimensions
	redEigVects = eigVects[:,eigValInd]       #reorganize eig vects largest to smallest
	lowDDataMat = meanRemoved * redEigVects#transform data into new dimensions
	reconMat = (lowDDataMat * redEigVects.T) + meanVals
	return lowDDataMat, reconMat
		
