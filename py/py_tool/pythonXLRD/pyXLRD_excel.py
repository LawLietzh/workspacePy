#coding:utf-8
import xlrd
import xlwt
path = 'D://excel.xlsx'
workbook = xlrd.open_workbook(path)
#获取excel 文件并获取所有sheet
print(workbook.sheet_names())
#根据下标获取sheet 名称
print(workbook.sheet_names()[0])

#根据sheet索引或者名称获取sheet内容 同时获取sheet名称 行数  列数
sheet1 = workbook.sheets()[0]
nrows = sheet1.nrows
ncols = sheet1.ncols
print(nrows,ncols)
path = 'E://数据资料//数据分析//诉求工单（4月-11月）.xlsx'
data = xlrd.open_workbook(path)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
date_dict = {}
for i in range(1, nrows):
    date = table.row_values(i)[5].strip().split("-")[0]
    if u"门店客诉" in date:
        brand = table.row_values(i)[57]

        if brand not in date_dict:
            date_dict[brand] = 1
        else:
            date_dict[brand] += 1

date_dict = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)

for time in date_dict:
    print(time[0])
for time in date_dict:
    print(time[1])

