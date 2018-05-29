#coding:utf-8

import xlrd
import  jieba
import re

#停用词 列表
stopwordSet = set()
pathstop = 'C://Users//zhangheng//Desktop//张芬数据分析//stopwords.txt'
with open(pathstop,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        stopwordSet.add(line)

path = 'C://Users//zhangheng//Desktop//张芬数据分析//400//17年7月至2月11日诉求数据.xlsx'
#path = 'C://Users//zhangheng//Desktop//张芬数据分析//400//22.xlsx'
pathW = "C://Users//zhangheng//Desktop//张芬数据分析//400//sanjifenlei.txt"
w = open(pathW,'w',encoding='utf-8')

data = xlrd.open_workbook(path)
table = data.sheets()[0]
nrows = table.nrows
print(nrows)
ncols = table.ncols
print(ncols)
date_dict = {}

for i in range(1, nrows):
    brand = str(table.row_values(i)[5]).strip().replace(" ","")
    #brand = str(table.row_values(i)[43])
    #print(brand)

    array = brand.split("-")
    if(len(array) == 3 ):
        x = array[2]
        if x not in date_dict:
            date_dict[x] = 1
        else:
            date_dict[x] += 1

date_dict = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)
set = set()
print(type(date_dict))
for i in date_dict:
    newline = str(i[0])+" "+str(i[1])
    w.write(newline)
    w.write("\n")
    w.flush()
w.close()




'''
    #按照不同得分，进行收集
    if(brand== '1' or brand== '2' or brand== '3' or brand== '4' or brand== '5'):
        question = str(table.row_values(i)[6])
        question  = re.sub("[0-9\!\%\[\]\,\。.]", "", question)
        if len(question) > 1:
            seg_list = list(jieba.cut(question,cut_all = False))
            query = (','.join(seg_list)).replace(',',' ')
            #print(type(query))
            array = query.split(" ")
            for x in iter(array):
                if(len(x)>1 and x not  in stopwordSet):
                    #print(x)
                    if x not in date_dict:
                        date_dict[x] = 1
                    else:
                        date_dict[x] += 1



date_dict = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)
print(type(date_dict))
for i in date_dict:
    newline = str(i[0])+" "+str(i[1])
    w.write(newline)
    w.write("\n")
    w.flush()
w.close()

'''
