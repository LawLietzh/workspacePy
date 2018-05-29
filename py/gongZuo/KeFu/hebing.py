#coding:utf-8
import random
import  numpy as np
path = 'E://数据资料//数据集合//情感词挖掘//FuXcontent_quchong.txt'
path1 = 'E://数据资料//数据集合//情感词挖掘//ZhengXcontent_quchong.txt'
#未加倍，负 正比例  7:1
path2 = 'E://数据资料//数据集合//情感词挖掘//qgTrain0.txt'
path3 = 'E://数据资料//数据集合//情感词挖掘//qgTest0.txt'
t = 0
l = []
w =  open(path2,'w',encoding='utf-8')
te = open(path3,'w',encoding='utf-8')
#写负向，负的数据多，
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        t = t+1
        line = line.strip()
        l.append(line)
        #w.write(line)
        #w.write('\n')
#写正向
with open(path1,"r",encoding='utf-8') as f:
    for line in f.readlines():
        t=t+1
        line = line.strip()
        l.append(line)
        #w.write(line)
        #w.write('\n')

print(t)
print(len(l))
#内存小，数据量大，无法完成打乱顺序
'''
#打乱 l 中顺序
np.random.seed(10)
shuffle_indices = np.random.permutation(np.arange(len(l)))
l = np.array(l)
l = l[shuffle_indices]
l = l.tolist()
'''
# 现在是随机的从所有文本中抽取10000数据，然后，把这一万数据作为测试，剩下的部分作为训练
slice = random.sample(l,5000)
ret = list(set(l) ^ set(slice))
print(len(ret))
print(len(slice))
for str in ret:
    w.write(str)
    w.write('\n')
for str in slice:
    te.write(str)
    te.write('\n')


'''
for i in range(4):
    with open(path1,"r",encoding='utf-8') as f:
        for line in f.readlines():
            line = line.strip()
            w.write(line)
            w.write('\n')
'''


