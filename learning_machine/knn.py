#coding=utf8
#KNN聚类算法
import xlrd
setdata=[
[0.516971452,	0.544261026,	0.548248459,	3],
[0.167466646,	0.467559217,	0.99211529,	2],
[0.320374998,	0.094242398,	0.456492602,	1],
[0.969402462,	0.859329264,	0.224581381,	1],
[0.482909543,	0.109139324,	0.042911837,	1],
[0.941066021,	0.662876154,	0.59695561,	1],
[0.451227736,	0.446468666,	0.708075832,	3],
[0.540058445,	0.867759222,	0.295429716,	3],
[0.868393563,	0.564170109,	0.422062269,	1],
[0.445079138,	0.802188881,	0.889864365,	3],
[0.640234308,	0.243372245,	0.473011097,	1],
[0.81256694,	0.548110996,	0.989390875,	1]
]
dset=[]
t=[]
for i in setdata:
	d=[]
	d.append(i[0])
	d.append(i[1])
	d.append(i[2])
	dset.append(d)
	t.append(i[3])
#testdata=[0.833921748,0.560733679,0.381229963],
#testdata=[0.27499438,	0.346274739	,0.353645499	]

testdata=[0.356473217,	0.430978784,	0.07547164]	

testlable=[1,2,3]
def classfy(X ,dataset,labels,K):
    l=0
    jieguo=[]
    for i in dataset:
        sum_every=0
        for j in range(3):
            sum_every+=(X[j]-i[j])**2
        every_jie=[]
        every_jie.append(labels[l])
        every_jie.append(sum_every**0.5)
        jieguo.append(every_jie)
        l+=1
    odl=sorted(jieguo,key=lambda every:every[1])
    return odl[0:K]
k_data=classfy(testdata,dset,t,4)
lei=[]
for i in range(4):
    lei.append(k_data[i][0])

def leibie(nlist):
    max=0
    for i in nlist:
        if nlist.count(i) > max :
            max=nlist.count(i)
            flag=i
    return flag
print "the test data is lei bie %s" %(leibie(lei))
