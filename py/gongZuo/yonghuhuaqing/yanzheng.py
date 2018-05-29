#coding:utf-8
'''
会员价值等级模型判定

'''
import  os
import numpy as np
#读取数据
path = 'E://数据资料//数据集合//test1//'
pathW =  'E://数据资料//数据集合//test1.txt//'
#写数据

pathDir = os.listdir(pathW)
pathdir = []
t = 0
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (pathW,allDir))
    print(child)
    pathdir.append(child)


for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        t= t+1

print(t)
