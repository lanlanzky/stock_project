#coding=utf8
import numpy,random
testlist=[1,2,3,4,5,10,16,17,18,19,20,21,26,27,28,29,30,31]
k_list= random.sample(testlist,6)
tuple1=[k_list[0]]
tuple2=[k_list[1]]
tuple3=[k_list[2]]
tuple4=[k_list[3]]
tuple5=[k_list[4]]
tuple6=[k_list[5]]
def mimin(value,klist):#找出value与klist数组中哪个值最接近
	flag=0
	min=abs(value-klist[0])
	for i in klist[1:]:
		if abs(i-value) < min:
			min=abs(i-value)
			flag=klist.index(i)
	return flag
	#return klist[flag]
for i in testlist:
	if i not in k_list:
		means=mimin(i,k_list)
		print means
		if means==0:
			tuple1.append(i)
		elif means==1:
			tuple2.append(i)
		elif means==2:
			tuple3.append(i)
		elif means==3:
			tuple4.append(i)
		elif means==4:
			tuple5.append(i)
		else:
			tuple6.append(i)
	else:
		print ''
tuple1=map(float,tuple1)
tuple2=map(float,tuple2)
tuple3=map(float,tuple3)
tuple4=map(float,tuple4)
tuple5=map(float,tuple5)
tuple6=map(float,tuple6)
print 'the 1_mens is %.2f,2_means is %.2f,3_means is %.2f,4_means is %.2f ,5_means is %.2f,6_means is %.2f' %((sum(tuple1))/len(tuple1),(sum(tuple2))/len(tuple2),(sum(tuple3))/len(tuple3),(sum(tuple4))/len(tuple4),(sum(tuple5))/len(tuple5),(sum(tuple6))/len(tuple6))
