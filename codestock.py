#coding=utf8
import xlrd
import os
from stock.models import *
for i in os.listdir('.'):
    if i.endswith('.xls'):
        codename=i[0:8]
        datetime=i[-14:-4]
        i=str(i)
        data=xlrd.open_workbook(i)
        table=data.sheets()[0]
        nrows=table.nrows
        chengjiaojia=sum(table.col_values(1))/nrows
        chengjiaoliang=sum(table.col_values(2))/2
        chengjiaoe=sum(table.col_values(3))/2
        p=New_stock(name=codename,time=datetime,price=chengjiaojia,numbers=chengjiaoliang,turnover=chengjiaoe)
        p.save()
