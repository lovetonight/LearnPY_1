import re
import os
import io
import numpy
import openpyxl as xl


def updateValueExcel(filename, cellname, value):  # Chèn giá trị excel
    wb = xl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    Sheet1[cellname].value = value
    wb.close()
    wb.save(filename)


def getValueExcel(filename, cellname):  # Lấy giá trị excel
    wb = xl.load_workbook(filename)
    Sheet1 = wb['Sheet1']
    wb.close()
    return Sheet1[cellname].value


def writeUtf8(filename, data):  # Ghi có dấu vào file
    f = io.open(filename, mode='a', encoding='utf-8')
    f.write(data+'\n')
    f.close()
filename='test.txt'


f = io.open(filename, mode='r', encoding='utf-8')  # Đọc có dấu từ file
list_lines = f.readlines()
print(max(list_lines))
for line in list_lines:
    print(line)


filename = 'Book1.xlsx'
user = 'A'
password = 'B'
for i in range(3, 10, 1):
    get_user = "%s%s" % (user, i)
    get_password = "%s%s" % (password, i)
    _user = getValueExcel(filename, get_user)
    _password = getValueExcel(filename, get_password)
    print("current_user:", _user)
    print("current_password:", _password)

