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
m = 0
z = 0
t = 0
t1 = 0
t11 = 0
t12 = 0
t2 = 0
t2t =0
t21 = 0
t22 = 0
t23 = 0

t3 =0
t31 =0
t32 =0
t33 =0
t4 = 0
t5 = 0
t6= 0
t7 = 0
for i in c:
    if i <= 1:
        m = m+1
    elif i>1 and i<=2:
        z=z+1
    elif i>2 and i<=3:
        t =t+1
    elif i>3 and i<=5:
        t1= t1+1
    elif i>5 and i<=8:
        t11= t11+1
    elif i>8 and i<=10:
        t12= t12+1

    elif i>10 and i<=12:
        t2= t2+1

    elif i>15 and i<=20:
        t2t= t2t+1

    elif i>20 and i<=30:
        t21= t21+1
    elif i>30 and i<=40:
        t22= t22+1
    elif i>40 and i<=50:
        t23= t23+1

    elif i>50 and i<=100:
        t3 = t3+1
    elif i>100 and i<=120:
        t31= t31+1
    elif i>120 and i<=150:
        t32= t32+1
    elif i>150 and i<=180:
        t33= t33+1
    elif i>180 and i<=200:
        t4= t4+1
    elif i>200 and i<=255:
        t5= t5+1
    elif i>500 and i<=1000:
        t6 = t6+1
    elif i>1000 :
        t7 = t7+1
print('等于1',m,"   ",m/c.__len__())
print('1 到 2：   ',z,"   ",z/c.__len__())
print('2 到3 ：   ',t,"   ",t/c.__len__())
print('3 到 5：   ',t1,"   ",t1/c.__len__())
print('5 到 8：   ',t1,"   ",t11/c.__len__())
print('8 到 10：   ',t1,"   ",t12/c.__len__())


print('10 到 12 ：   ',t2,"   ",t2/c.__len__())
print('15 到 20 ：   ',t2t,"   ",t2t/c.__len__())

print('20 到 30 ：   ',t21,"   ",t21/c.__len__())
print('30 到 40 ：   ',t22,"   ",t22/c.__len__())
print('40 到 50 ：   ',t23,"   ",t23/c.__len__())

print('50到100：   ',t3,"   ",  t3/c.__len__())
print('100到120：   ',t31,"   ",t31/c.__len__())
print('120到150：   ',t32,"   ",t32/c.__len__())
print('150到180：   ',t33,"   ",t33/c.__len__())
print('180到200：   ',t4,"   ",t4/c.__len__())
print('200到255：   ',t5,"   ",t5/c.__len__())
print('500到1000：    ',t6,"   ",t6/c.__len__())
print('大于1000：    ',t7,"   ",t7/c.__len__())



