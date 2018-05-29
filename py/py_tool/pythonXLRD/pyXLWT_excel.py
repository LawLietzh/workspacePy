#coding:utf-8
import  xlwt
biaotou=['学号','学生姓名']
path = "d://xx.xls"
filename = xlwt.Workbook()
sheet = filename.add_sheet("hel")
#下面是把 表头写上
for i in range(0,len(biaotou)):
    sheet.write(0,i,biaotou[i])

zh = 1
for i in range(5):
    for j in range(5):
        for k in range(2):
            sheet.write(zh,k,"id")# zh 是行   ，k 是列  ，“id”是要写的内容
        zh = zh +1

filename.save(path)