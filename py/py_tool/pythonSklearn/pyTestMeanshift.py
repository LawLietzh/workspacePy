#coding:utf-8
'''
实验meanshift 聚类
'''
import numpy as np
from sklearn.cluster import MeanShift, estimate_bandwidth
from sklearn.datasets.samples_generator import make_blobs

centers = [[1, 1], [-1, -1], [1, -1]]
X, _ = make_blobs(n_samples = 10000, centers = centers, cluster_std = 0.6)
print(X[0:100])
#用于估计加权核的带宽
bandwidth = estimate_bandwidth(X, quantile = 0.2, n_samples = 500)

#bin_seeding用来设定初始核的位置参数的生成方式，default False,默认采用所有点的
#位置平均，当改为True时使用离散后的点的平均，前者比后者慢。
ms = MeanShift(bandwidth = bandwidth, bin_seeding = True)
ms.fit(X)
labels = ms.labels_
cluster_centers = ms.cluster_centers_

labels_unique = np.unique(labels)
n_clusters_ = len(labels_unique)
print(n_clusters_)
print("number of estimated clusters: %d" % n_clusters_)

import matplotlib.pyplot as plt
from itertools import cycle

plt.figure(1)
plt.clf()

colors = cycle('bgrcmyk')
for k, col in zip(range(n_clusters_), colors):
    my_members = labels == k
    cluster_center = cluster_centers[k]
    plt.plot(X[my_members, 0], X[my_members, 1], col + '.')
    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor = col, markeredgecolor = 'k', markersize = 14)

plt.title("Estimated number of clusters: %d" % n_clusters_)
plt.show()