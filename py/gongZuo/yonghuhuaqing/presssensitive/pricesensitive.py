#coding:utf-8
import  sklearn
import  numpy as np
'''
价格 敏感度计算 

'''
import  os
import numpy as np
#读取数据
path = 'E://数据资料//数据集合//price//'
pathW =  'E://数据资料//数据集合//price.txt'
pathW1 =  'E://数据资料//数据集合//price1.txt'
#写数据
w = open(pathW1,'w',encoding='utf-8')
w = open(pathW,'w',encoding='utf-8')
pathDir = os.listdir(path)
pathdir = []

for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)


train = []
uid   = []
for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        strArray = line.strip().split('\t')
        #获得会员价值分数
        arr = []
        if strArray.__len__() == 3:
            uid.append(strArray[0].strip())
            #优惠金额
            arr.append(float(strArray[1].strip()))
            #优惠次数
            arr.append(float(strArray[2].strip()))
            train.append(arr)
        elif strArray.__len__() != 3:
            print("数据有误，分隔后不是三列")


train = np.array(train)
uid = (np.array(uid)).reshape(-1,1)
from sklearn.preprocessing import MinMaxScaler


X_train_std = MinMaxScaler().fit_transform(train)


print(train[0:3])
print(X_train_std[0:3])
print(uid[0:3])
#接下来  乘以权重，然后写到文本中
#定义权重
q = [0.5,0.5]
quanzhong = X_train_std*q


he = (quanzhong[:,0] + quanzhong[:,1]).reshape(-1,1)
hebing = np.hstack((uid,he))
print(hebing[0:3])
#写到文本中
for line in hebing:
    str = ''+line[0]+'\t'+line[1]
    w.write(str)
    w.write('\r')
    w.flush()
    str = ''
w.close()






