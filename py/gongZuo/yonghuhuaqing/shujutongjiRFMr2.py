#coding:utf-8
from matplotlib import pyplot
import  os
import numpy as np
import matplotlib.pyplot as plt
'''
统计天数
'''
#读取数据
path = 'E://数据资料//数据集合//test//'

pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)



#购买tian数
c = []

for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        line = line.strip()
        str = line.split('\t')
        if str.__len__()!=4:
            print(line)

        #strc = str[str.__len__()-1].strip()
        strc = str[3].strip()
        cc = float(strc)
        c.append(cc)

c.sort()
print(c[0:100])
print(max(c))
print(c[-100:])


a = 0
z = 0
t = 0
m =0
n =0
y=0



for i in c:
    if i <= 1:
        a = a+1
    elif i>1 and i<90:
        z=z+1
    elif i>90 and i<=180:
        t=t+1
    elif i>180 and i<=365:
        m=m+1
    elif i>365 and i<=500:
        n=n+1
    elif i>500 :
        y=y+1

print('等于1',a,"   ",a/c.__len__())
print('1 到 90：   ',z,"   ",z/c.__len__())
print('90 到180 ：   ',t,"   ",t/c.__len__())
print('180 到365：   ',m,"   ",m/c.__len__())
print('365 到 500：   ',n,"   ",n/c.__len__())
print('500 到 ：   ',y,"   ",y/c.__len__())



