#coding:utf-8
'''
统计舆情权重，参看 设的阈值，下，有多少满足需求的样本
'''

path = 'E://数据资料//数据集合//舆情权重.txt'
t = 0
with open(path,"r",encoding='GBK') as f:
    for line in f.readlines():
        str = line.strip().split(',')[1]
        str = float(str)
        if str>=0.95:
            t = t+1
            print(str)

print(t,"   :",t/140)