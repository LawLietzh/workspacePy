#coding:utf-8
import  numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import  KMeans
from  sklearn.datasets import  make_blobs
plt.figure(figsize=(12,12))

'''
make_blobs函数是为聚类产生数据集 产生一个数据集和相应的标签
 n_samples:表示数据样本点个数,默认值100 
n_features:表示数据的维度，默认值是2 
centers:产生数据的中心点，默认值3 
cluster_std：数据集的标准差，浮点数或者浮点数序列，默认值1.0 
center_box：中心确定之后的数据边界，默认值(-10.0, 10.0) 
shuffle ：洗乱，默认值是True 
random_state:官网解释是随机生成器的种子 
'''

n_samples = 1500
random_state = 170
X,y = make_blobs(n_samples=n_samples,random_state=random_state)
print(X[0:3])

#y_pred = KMeans(n_clusters=2, random_state=random_state).fit_predict(X)
y_pred = KMeans(n_clusters=2).fit(X)
#获取聚类标签  每个样本的聚类类别
label_pred = y_pred.labels_
print(type(label_pred))
print(label_pred[0:100])
#获取聚类中心
centroids = y_pred.cluster_centers_
print('聚类中心：',centroids)
#获得聚类准则 的总和
inertia = y_pred.inertia_
print('聚类准则的总和：',inertia)

#返回各自文本所被分配到的 类索引
yy = KMeans(n_clusters=2).fit_predict(X)
print('文本所被分配到的 类索引：   ',yy[0:100])
#
dd = y_pred.predict(X)
print(dd[0:100])

# 下面 实验meanshift 聚类
#数据归一化
from sklearn import preprocessing
#导入 meanshift
from sklearn.cluster import MeanShift
X = preprocessing.scale(X)
print(type(X))
clf = MeanShift()
clf.fit(X)
#获取聚类标签  每个样本的聚类类别
labels = clf.labels_
#获取聚类中心
cluster_centers = clf.cluster_centers_
#统计有几个类别
n_cluster = len(np.unique(labels))
print('meanshift:    ',n_cluster)