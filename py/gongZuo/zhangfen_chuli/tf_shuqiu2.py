#conding:utf-8
'''
诉求工单中 来电原因 词频分析 

'''

import xlrd
import  jieba
import re
#加载停用词
stopwordSet = set()
pathstop = 'C://Users//zhangheng//Desktop//张芬数据分析//stopwords.txt'
with open(pathstop,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        stopwordSet.add(line)




path = 'C://Users//zhangheng//Desktop//张芬数据分析//1月诉求建档明细.xlsx'
#pathW = "C://Users//zhangheng//Desktop//张芬数据分析//suqiu_reason.txt"
pathW = "C://Users//zhangheng//Desktop//张芬数据分析//suqiu_response.txt"

w = open(pathW,'w',encoding='utf-8')

data = xlrd.open_workbook(path)
table = data.sheets()[0]
nrows = table.nrows
print(nrows)
ncols = table.ncols
date_dict = {}

for i in range(1, nrows):

    brand = str(table.row_values(i)[46]).strip().replace(" ","")
    #print(brand)

    #过滤掉 数字
    brand  = re.sub("[0-9\!\%\[\]\,\。]", "", brand)
    if len(brand)>1:
        seg_list = list(jieba.cut(brand,cut_all = False))
        query = (','.join(seg_list)).replace(',',' ')
        #print(type(query))
        array = query.split(" ")
        for x in iter(array):
            if(len(x)>1 and x not  in stopwordSet and x !=""):
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

