#coding:utf-8
'''
关于使用sklearn进行数据预处理  归一化、标准化、正则化


公式为：(X-mean)/std  计算时对每个属性/每列分别进行。

将数据按期属性（按列进行）减去其均值，并处以其方差。得到的结果是，对于每个属性/每列来说所有数据都聚集在0附近，方差为1。

实现时，有两种不同的方式：
'''

#使用sklearn.preprocessing.scale()函数，可以直接将给定数据进行标准化。

from sklearn import preprocessing
import numpy as np
X = np.array([[ 1., -1.,  2.],
              [ 2.,  0.,  0.],
             [ 0.,  1., -1.]])

X_scaled = preprocessing.scale(X)

#处理后数据的均值和方差
X_scaled.mean(axis=0)
X_scaled.std(axis=0)


#2 使用sklearn.preprocessing.StandardScaler类，使用该类的好处在于可以保存训练集中的参数（均值、方差）直接使用其对象转换测试集数据。

scaler = preprocessing.StandardScaler().fit(X)
print('0000',X)
print('1111',scaler)
scaler.mean_
scaler.std_
t = scaler.transform(X)
print('ss',t)
#可以直接使用训练集对测试集数据进行转换
ss = scaler.transform([[-1.,  1., 0.]])
print(ss)


