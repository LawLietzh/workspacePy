#coding:utf-8
'''

练习使用sklearn，实现感知机模型 perceptron


'''
from sklearn import datasets
import numpy as np
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from matplotlib.colors import ListedColormap


def plot_decision_regions(X, y, classifier, test_idx=None, resolution=0.02):
    # setup marker generator and color map
    markers = ('s', 'x', 'o', '^', 'v')
    colors = ('red', 'blue', 'lightgreen', 'gray', 'cyan')
    cmap = ListedColormap(colors[:len(np.unique(y))])
    # plot the decision surface
    x1_min, x1_max = X[:, 0].min() - 1, X[:, 0].max() + 1
    x2_min, x2_max = X[:, 1].min() - 1, X[:, 1].max() + 1
    xx1, xx2 = np.meshgrid(np.arange(x1_min, x1_max, resolution), np.arange(x2_min, x2_max, resolution))
    Z = classifier.predict(np.array([xx1.ravel(), xx2.ravel()]).T)
    Z = Z.reshape(xx1.shape)
    plt.contourf(xx1, xx2, Z, alpha=0.4, cmap=cmap)
    plt.xlim(xx1.min(), xx1.max())
    plt.ylim(xx2.min(), xx2.max())
    # plot class samples
    for idx, cl in enumerate(np.unique(y)):
        plt.scatter(x=X[y == cl, 0], y=X[y == cl, 1],alpha=0.8, c=cmap(idx),marker=markers[idx], label=cl)
    # highlight test samples
    if test_idx:
        X_test, y_test = X[test_idx, :], y[test_idx]
        plt.scatter(X_test[:, 0], X_test[:, 1], c='', alpha=1.0, linewidth=1, marker='o', s=55, label='test set')
#获得数据集  4个特征，3个类别
iris = datasets.load_iris()
print(type(iris.data))
print(iris.data[0:1])
print(iris.target[0:1])
#获取第2  和第 3 列的数据
X = iris.data[:, [2, 3]]
#取标签  标签已经转换成 0，1,2
y = iris.target
#取样本的30%作为测试
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=0)

print("查看数据  ：")
print(X_train[0:3])
print(y_train[0:3])

#为了追求机器学习和最优化算法的最佳性能，我们将特征缩放
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
#估算每个特征的平均值和标准差
sc.fit(X_train)
#查看特征的平均值
print(sc.mean_)
#查看特征的标准差
print(sc.scale_)
#注意：这里我们要用同样的参数来标准化测试集，使得测试集和训练集之间有可比性
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)

# 训练感知机模型 （一种二分类模型）
from sklearn.linear_model import Perceptron
#n_iter:可以理解为梯度下降中迭代的次数
#eta0：可以理解成梯度下降中的学习率
#random_state :设置随机种子的，为了每次迭代都有相同的训练集顺序
#构建模型
ppn = Perceptron(n_iter=40,eta0=0.1,random_state=0)
#训练模型
ppn.fit(X_train_std,y_train)

#分类测试集，这将返回一个测试
y_pred = ppn.predict(X_test_std)
print(y_pred)
#计算模型在测试集上的准确性，
#  测试，      测试集样本，测试集标签
t = ppn.score(X_test_std,y_test,sample_weight=None)
print(t)

#print(t)
#统计结果
from sklearn.metrics import f1_score, classification_report
print(classification_report(y_test, y_pred))


