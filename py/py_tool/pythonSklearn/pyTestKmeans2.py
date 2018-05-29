#coding：utf-8

#接k_means.py
#k_means.py中得到三维规范化数据data_zs；
#r增加了最后一列，列索引为“聚类类别”
from sklearn.manifold import TSNE
tsne=TSNE()
data_zs = []
tsne.fit_transform(data_zs)  #进行数据降维,降成两维
