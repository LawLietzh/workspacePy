#coding:utf-8
from matplotlib import pyplot
import  os
import numpy as np
import matplotlib.pyplot as plt

#读取数据
path = 'E://数据资料//数据集合//test//'

pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)

line = []
#购买次数
l = []


for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        line = line.strip()
        str = line.split('\t')[2].strip()
        t = float(str)
        l.append(t)





l.sort()
print(l[0:100])
print(max(l))
print(l[-100:])
m = 0
m1 = 0
z = 0
t = 0
t1 = 0
t2 = 0
t22 = 0
t21 = 0
t3 =0
t4 = 0
t5 = 0
t6= 0
t7 = 0
for i in l:
    if i == 0:
        m = m+1
    elif i==1 :
        m1 = m1 + 1
    elif i>1 and i<=2:
        z=z+1
    elif i>2 and i<=3:
        t =t+1
    elif i>3 and i<=5:
        t1= t1+1
    elif i>5 and i<=8:
        t2= t2+1
    elif i>8 and i<=10:
        t22= t22+1
    elif i>10 and i<=50:
        t21= t21+1
    elif i>50 and i<=100:
        t3= t3+1
    elif i>100 and i<=200:
        t4= t4+1
    elif i>200 and i<=500:
        t5= t5+1
    elif i>500 and i<=1000:
        t6 = t6+1
    elif i>1000 :
        t7 = t7+1
print('等于0',m,"   ",m/l.__len__())
print('等于1',m1,"   ",m1/l.__len__())
print('1 到 2：   ',z,"   ",z/l.__len__())
print('2 到3 ：   ',t,"   ",t/l.__len__())
print('3 到5 ：   ',t1,"   ",t1/l.__len__())
print('5 到 8：   ',t2,"   ",t2/l.__len__())
print('8 到 10：   ',t22,"   ",t22/l.__len__())

print('10 到 50 ：   ',t21,"   ",t21/l.__len__())
print('50到100：   ',t3,"   ",t3/l.__len__())
print('100到200：   ',t4,"   ",t4/l.__len__())
print('200万到500：   ',t5,"   ",t5/l.__len__())
print('500到1000：    ',t6,"   ",t6/l.__len__())
print('大于1000：    ',t7,"   ",t7/l.__len__())


'''
等于1 4026577     0.525505005024601
1 到 2：    1858503     0.2425515837281234
2 到3 ：    716608     0.0935238766427835
3 到5 ：    597026     0.07791733552588648
5 到 8：    285737     0.03729128329613823
8 到 10：    73763     0.009626743928063375
10 到 50 ：    100614     0.01313104420343761
50到100：    2341     0.0003055218407005729
100到200：    698     9.109536301110633e-05
200万到500：    343     4.476462680918262e-05
500到1000：     73     9.527165472508255e-06
大于1000：     17     2.2186549730498674e-06

经过统计： 一次和两次的占了76%  
所以用 2 ，8 分类
'''
