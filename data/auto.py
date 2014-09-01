#coding=utf8
import time
import datetime
import MySQLdb
import os
text=open('stock.txt','a')
conn=MySQLdb.connect(host='127.0.0.1',port=3306,user='root',passwd='lanlan521',db='stock')
cur=conn.cursor()
try:	
	cur.execute("select * from stock_new_stock")
	data = cur.fetchall()
	for row in data:
		for i in  row[3:]:
			text.write(i)
			text.write('\t')
		text.write('\n')
			
except:
   print "Error: unable to fecth data"	
cur.close()
conn.commit
conn.close()
text.close()
