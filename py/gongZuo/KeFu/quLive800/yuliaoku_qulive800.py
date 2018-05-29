#coding:utf-8
'''
在现有语料库中，去除live800 语料 
思路：先读取live800 数据
'''
import xlrd
#读取live800 数据
path = 'D://李响//key_word//live800quchong//download3null1487576348532（live800线上知识库）_去掉笑话闲聊.xls'
data = xlrd.open_workbook(path)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
live800_0 = set()
live800_1 = list()
for i in range(1, nrows):
    date = table.row_values(i)[0]
    live800_0.add(date.strip())
    live800_1.append(table.row_values(i)[1].strip())
print(len(live800_0))
print(len(live800_1))


#读取  正式数据库中数据

pathhebing = 'D://李响//key_word//live800quchong//kefu_20171205_QC_jiaSpan.txt'
pathhebing_qulive800 = 'D://李响//key_word//live800quchong//kefu_20171205_QC_jiaSpan_Qulive800.txt'
w_quwuliu = open(pathhebing_qulive800,'w',encoding='utf-8')
live = list()
liveANSWER = list()
tt = 0
ttt = 0
with open(pathhebing,"r",encoding='utf-8') as f:
    for line in f.readlines():
        if '业务分类' not in line:
            w_quwuliu.write(line)
        elif '业务分类' in line:
            lineArray = line.split("\t")
            lineQuery = lineArray[1].replace(" ","").strip()
            lineAnswer = lineArray[2].strip()
            if(lineAnswer not in live800_1):
                ttt = ttt+1
                w_quwuliu.write(line)


w_quwuliu.close()
print(tt)
print(len(live))


print(ttt)












