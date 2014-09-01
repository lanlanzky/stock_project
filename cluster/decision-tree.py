#coding=utf8
#用决策树来预测眼睛类型
#信息增益 熵
from math import log
import operator
lables=['age','prescript','astigmatic','terarfate']
lableset=['no-lenses','soft','no-lenses','hard','no-lenses','soft','no-lenses','hard','no-lenses','soft','no-lenses','hard','no-lenses','soft','no-lenses','no-lenses','no-lenses','no-lenses','no-lenses','hard','no-lenses']
dataset = [
['young','myope',	'no',	'educed',] ,
['young','myope',	'no',	'normal'],
['young','myope',	'yes',	'reduced'],
['young','myope',	'yes',	'normal'],
['young','hyper',	'no',	'reduced'],
['young','hyper',	'no',	'normal'],
['young','hyper',	'yes',	'reduced'],
['young','hyper',	'yes',	'normal'],
['pre',	'myope'	,'no',	'reduced'	],
['pre',	'myope'	,'no',	'normal'],
['pre',	'myope'	,'yes',	'reduced'],
['pre',	'myope','yes',	'normal'],
['pre',	'hyper',	'no',	'reduced'	],
['pre',	'hyper',	'no',	'normal'	],
['pre','hyper',	'yes',	'reduced'],
['pre',	'hyper',	'yes',	'normal'],
['presbyopic',	'myope',	'no',	'reduced'],
['presbyopic',	'myope'	,'no',	'normal'],
['presbyopic',	'myope'	,'yes',	'reduced'],
['presbyopic',	'myope'	,'yes',	'normal'],
['presbyopic',	'hyper'	,'no',	'reduced']]
for i in dataset:
	i.append(lableset[dataset.index(i)])
test=[
['presbyopic',	'hyper',	'no',	'normal'],
['presbyopic',	'hyper'	,'yes',	'reduced'],
['presbyopic',	'hyper'	,'yes',	'normal']
]
testlable=['soft','no-lenses','no-lenses']
for i in test:
	i.append(testlable[test.index(i)])
for i in test:
	i.append(testlable[test.index(i)])
#[1,1,'maybe'],[1,1,'yes'],[1,1,'yes'],[1,0,'no'],[0,1,'no'],[0,1,'no']]
def calcShannonEnt(dataset):
	numEntries = len(dataset)
	labelCounts = {}
	for featVec in dataset:
		currentLabel = featVec[-1]
		if currentLabel not in labelCounts.keys():
			labelCounts[currentLabel] = 0
		labelCounts[currentLabel] += 1
	shannonEnt = 0.0
	for key in labelCounts:
		prob = float(labelCounts[key])/numEntries
		if prob != 0:
			shannonEnt -= prob*log(prob,2)
	return shannonEnt
#print calcShannonEnt(dataset) #得到最后一个属性的熵
def splitDataSet(dataSet, axis, value):
    retDataSet = []
    for featVec in dataSet:
        if featVec[axis] == value:
            reducedFeatVec = featVec[:axis]     #chop out axis used for splitting
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet
def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1      #the last column is used for the labels
    baseEntropy = calcShannonEnt(dataSet)
    bestInfoGain = 0.0; bestFeature = -1
    for i in range(numFeatures):        #iterate over all the features
        featList = [example[i] for example in dataSet]#create a list of all the examples of this feature
        uniqueVals = set(featList)       #get a set of unique values
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEnt(subDataSet)     
        infoGain = baseEntropy - newEntropy     #calculate the info gain; ie reduction in entropy
        if (infoGain > bestInfoGain):       #compare this to the best gain so far
            bestInfoGain = infoGain         #if better than current best, set to best
            bestFeature = i
    return bestFeature
print chooseBestFeatureToSplit(dataset)
def majorityCnt(classList):
    classCount={}
    for vote in classList:
        if vote not in classCount.keys(): classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet,labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList): 
        return classList[0]#stop splitting when all of the classes are equal
    if len(dataSet[0]) == 1: #stop splitting when there are no more features in dataSet
        return majorityCnt(classList)
    bestFeat = chooseBestFeatureToSplit(dataSet)
    bestFeatLabel = labels[bestFeat]
    myTree = {bestFeatLabel:{}}
    del(labels[bestFeat])
    featValues = [example[bestFeat] for example in dataSet]
    uniqueVals = set(featValues)
    for value in uniqueVals:
        subLabels = labels[:]       #copy all of labels, so trees don't mess up existing labels
        myTree[bestFeatLabel][value] = createTree(splitDataSet(dataSet, bestFeat, value),subLabels)
    return myTree  
def classify(inputTree,featLabels,testVec):
    firstStr = inputTree.keys()[0] 
    print 'test'
    print firstStr
#    print featLabels
    secondDict = inputTree[firstStr]
    featIndex = featLabels.index(firstStr)
    key = testVec[featIndex]
    valueOfFeat = secondDict[key]
    if isinstance(valueOfFeat, dict): 
        classLabel = classify(valueOfFeat, featLabels, testVec)
    else: classLabel = valueOfFeat
    return classLabel
mytree=createTree(dataset,lables)
def testdeciton():
	testdd=test
	lei=[i[-1]for i in test]
	return testdd,lei
print testdeciton()
