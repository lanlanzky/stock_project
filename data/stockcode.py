#from stock.models import  New_stock
from stock.models import New_stock
import os
def list_xls():
    a=[]
    for i in os.listdir('.'):
        if i.endswith('xls'):
            a.append(i)
    print "iama"
    print a
    return a

def datatomysql():
    codelist=list_xls()
    print codelist
    for i in codelist:
        data=xlrd.open_workbook(i)
        table = data.sheets()[0]
        aname=i[0:8]
        atime=i[-14:-4]
        rows=table.nrows
        aprice=sum(table.col_values(1))/rows
        snumber=sum(table.col_values(2))/2
        volum=sum(table.col_values(3))/2
        p=New_stock(name=aname,time=atime,price=aprice,numbers=snumber,turnover=volum)
        p.save()
            
    

