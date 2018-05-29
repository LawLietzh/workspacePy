#coding:utf-8
from matplotlib import pyplot
import  os
import numpy as np
import matplotlib.pyplot as plt

#读取文件 下的所以 数据列表
path = 'E://数据资料//数据集合//test//'

l = []
pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)

for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        line = line.strip()
        str = line.split('\t')[2].strip()
        t = float(str)
        l.append(t)
