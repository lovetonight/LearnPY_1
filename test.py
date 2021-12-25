import re
import os
import io
import numpy
import openpyxl as xl

filename='test.txt'

def updateValueExcel(filename,cellname,value):
    wb=xl.load_workbook(filename)
    Sheet1=wb['Sheet1']
    Sheet1[cellname].value=value
    wb.close()
    wb.save(filename)

def getValueExcel(filename,cellname):
    wb=xl.load_workbook(filename)
    Sheet1=wb['Sheet1']
    wb.close()
    return Sheet1[cellname].value



def writeUtf8(filename, data):
    f=io.open(filename,mode='a',encoding='utf-8')
    f.write(data+'\n')
    f.close()
#f=open(filename,'a')
#regex1=re.compile(r'anh (.*) dep')
#writeUtf8(filename,'hoàn'+'\n')
#f.close()   


#f=io.open(filename,mode='r',encoding='utf-8')
#list_lines=f.readlines()
#print(max(list_lines))
#for line in list_lines:
#    print(line)



filereadname='test.txt'
f=io.open('test.txt',mode='r',encoding='utf-8')
list_lines=f.readlines();
f.close();


filename='Book1.xlsx'
cellname_1='A3'
cellname_2='B3'
updateValueExcel(filename,cellname_1,list_lines[0]);
updateValueExcel(filename,cellname_2,list_lines[1]);

#bien_x=getValueExcel(filename,cellname)
#updateValueExcel(filename,cellname,'hoan1234')
#user='A'
#password='B'
#for i in range(3,10):
#    get_user="%s%s"%(user,i)
#    get_password="%s%s"%(password,i)
#    getListValueExcel(filename,get_user)
#    getListValueExcel(filename,get_password)
#print(bien_x)

#kq=regex1.findall(demo)
#name=kq.group(0)
#print(kq[1:3])
