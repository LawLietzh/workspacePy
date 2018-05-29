#coding:utf-8
import numpy as np
'''
path = 'E://数据资料//数据集合//test//000002_0'
with open(path,'r',encoding='UTF-8') as f:
    for line in f.readlines():
        line = line.strip()
        print(line)
        str = line.split('\t')[1]
        print(str)
        t = float(str)
        print(t)
        #t = int(line.split('\t')[1])
        #print(line)

'''

shuju = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12,],[13,14,15,16]])
print(shuju)
for pa in shuju:
    print(pa[0])


#t = int('2399.0000')
#print(t)

l = [4,1]
s = [3,1]
print(l)
#l.sort()
#print(l[-3:])
l = np.matmul(l,s)
print(l)
