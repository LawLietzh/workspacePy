#coding:utf-8

path = 'E://数据资料//数据分析//10.1-11.15(1).xlsx'

import xlrd
import openpyxl
data = xlrd.open_workbook(path)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
date_dict = {}
num = 0
for i in range(1, nrows):
    date = table.row_values(i)[5].strip().split("-")[0]
    if u"门店客诉" in date:
        brand = table.row_values(i)[5].strip().split("-")[2]

        if brand not in date_dict:
            date_dict[brand] = 1
        else:
            date_dict[brand] += 1

date_dict = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)

for time in date_dict:
    print(time[0])
for time in date_dict:
    print(time[1])




