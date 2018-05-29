#coding:utf-8

'''
会员价值等级模型 julei 

'''
import sklearn
import  os
import numpy as np
from sklearn.cluster import  KMeans
#读取数据
path = 'E://数据资料//数据集合//test//'


pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)

# 会员id  uid
#  金额  阈值设为 大于 5000   uidM =
#次数   uid 设为 大于等于3   uidF = []
#  天数 为 100   uidR = []

q = [0.5,0.3,0.2]
lines = []
for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        strArray = line.strip().split('\t')
        if strArray.__len__() == 4:
            uid  = strArray[0].strip()
            uidM = float(strArray[1].strip())
            uidF =float(strArray[2].strip())
            uidR = float(strArray[3].strip())
            linshi = []
            linshi.append(uidM)
            linshi.append(uidF)
            linshi.append(uidR)
            #每一行一个列表
            lines.append(linshi)

lineArray = np.array(lines)
print(type(lineArray))
print((lineArray).shape)
from sklearn.preprocessing import StandardScaler

sc = StandardScaler().fit(lineArray)

#注意：这里我们要用同样的参数来标准化测试集，使得测试集和训练集之间有可比性
X_train_std = sc.transform(lineArray)
print('X',type(X_train_std))

quanzhong = X_train_std*[0.5,0.3,0.2]
print('*************')
print(quanzhong[0:2])

he = quanzhong.sum(axis=1)
X_train_std = ((quanzhong.T)/he).T
print(X_train_std[0:2])
clf = KMeans(n_clusters=5)
s = clf.fit(X_train_std)
print(s)
#用来评估簇的个数是否合适，距离越小说明簇分的越好，选取临界点的簇个数
print(s.inertia_)

# meanshift 聚类
from sklearn.cluster import MeanShift
clf = MeanShift()
clf.fit(X_train_std)
#获取聚类标签  每个样本的聚类类别
labels = clf.labels_
#获取聚类中心
cluster_centers = clf.cluster_centers_
#统计有几个类别
n_cluster = len(np.unique(labels))
print('meanshift:    ',n_cluster)












