#coding:utf-8
from matplotlib import pyplot
import  os
import numpy as np
import matplotlib.pyplot as plt

#读取数据
path = 'E://数据资料//数据集合//test//'
#统计 消费金额
pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)

line = []
l = []
tt = 0
for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        line = line.strip()
        str = line.split('\t')[1].strip()
       # str1 = line.split('\t')[0].strip()
        t = float(str)
        l.append(t)





l.sort()
print(l[0:100])
print(max(l))
print(l[-100:])
m = 0
z = 0
t = 0
t1 = 0
t2 = 0
t21=0
t22=0
t3 =0
t4 = 0
t41 = 0
t5 = 0
t6= 0
t7 = 0
t11 = 0
for i in l:
    if i == 0:
        m = m+1
    elif i>=1 and i<=50:
        z=z+1
    elif i>50 and i<=100:
        t =t+1
    elif i>100 and i<=500:
        t1= t1+1
    elif i>500 and i<=1000:
        t11= t11+1
    elif i>1000 and i<=3000:
        t2= t2+1
    elif i>3000 and i<=5000:
        t21= t21+1
    elif i>5000 and i<=8000:
        t22= t22+1
    elif i>8000 and i<=10000:
        t3= t3+1
    elif i>10000 and i<=30000:
        t4= t4+1
    elif i>30000 and i<=50000:
        t41= t41+1

    elif i>50000 and i<=100000:
        t5= t5+1
    elif i>100000 and i<=1000000:
        t6 = t6+1
    elif i>1000000 :
        t7 = t7+1
print('等于0',m,"   ",m/l.__len__())
print('小于50：   ',z,"   ",z/l.__len__())
print('大于50小于100：   ',t,"   ",t/l.__len__())
print('大于100 小于500：   ',t1,"   ",t1/l.__len__())
print('大于500 小于1000：   ',t11,"   ",t11/l.__len__())
print('大于1千，小于3千：   ',t2,"   ",t2/l.__len__())
print('大于3千，小于5千：   ',t21,"   ",t21/l.__len__())
print('大于5千，小于8千：   ',t22,"   ",t22/l.__len__())

print('8千到1万：   ',t3,"   ",t3/l.__len__())
print('1万到3万：   ',t4,"   ",t4/l.__len__())
print('3万到5万：   ',t41,"   ",t41/l.__len__())
print('5万到十万：   ',t5,"   ",t5/l.__len__())
print('大于10万小于100万：    ',t6,"   ",t6/l.__len__())
print('大于100万：    ',t7,"   ",t7/l.__len__())


'''
等于0 167     2.1795022382313404e-05
小于50：    75738     0.009884499432285344
大于50小于100：    108063     0.014103206608981638
大于100 小于500：    807483     0.10538389256489566
大于500 小于1000：    675016     0.0880957414875429
大于1千，小于3千：    2389361     0.31183339206243554
大于3千，小于5千：    1450394     0.18928963888127587
大于5千，小于8千：    926598     0.12092948592459184
8千到1万：    295103     0.03851363167717265
1万到3万：    773770     0.10098403873510564
3万到5万：    111787     0.01458922255719562
5万到十万：    39815     0.005196220455998851
大于10万小于100万：     8636     0.0011270767263093326
大于100万：     116     1.5139057463163802e-05

从上面的统计看，在1千到三万之前的比重占到了 76% 
所以用1 千 和三万来分类 
'''
