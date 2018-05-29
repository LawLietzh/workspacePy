#coding:utf-8
import numpy as np
import sklearn
from sklearn import cross_validation
from sklearn import svm
from sklearn import metrics
from urllib import request
import matplotlib as mpl
import matplotlib.pyplot as plt
url = 'http://aima.cs.berkeley.edu/data/iris.csv'
response = request.urlopen(url)
#以下为本地样本存储路径，请根据实际情况设定！
#localfn='/mnt/hgfs/sharedfolder/iris.csv' #for linux
#localfn='C:\\TEMP\\iris.csv' #for windows
path = 'E://iris.data'
#localf = open(path, 'w')
#localf.write(response.read().decode('utf-8'))
#localf.close()

def iris_type(s):
    it = {b'setosa': 0, b'versicolor': 1, b'virginica': 2}
    if s not  in it:
        print(s)
    return it[s]

data = np.loadtxt(path, dtype=float, delimiter=',' , converters = {4: iris_type})
x, y = np.split(data, (4,), axis=1)
print("type",type(x))
print("x.shape():",x.shape)
print("y.shape():",y.shape)
x = x[:, :2]
x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, random_state=1, train_size=0.6)
'''
C 是惩罚项，也就是松弛变量 
kernel 是你选的可函数 默认是rbf（高斯）可以是‘linear’, ‘poly’, ‘rbf’, ‘sigmoid’, ‘precomputed’ 
gamma 核函数系数
'''
clf = svm.SVC(C=0.8, kernel='rbf', gamma=20, decision_function_shape='ovr')
#训练模型
clf.fit(x_train, y_train.ravel())
print(clf.score(x_train, y_train) ) # 精度
print(clf.score(x_test, y_test))




print ('decision_function:\n', clf.decision_function(x_train))
print ('\npredict:\n', clf.predict(x_train))


x1_min, x1_max = x[:, 0].min(), x[:, 0].max()  # 第0列的范围
x2_min, x2_max = x[:, 1].min(), x[:, 1].max()  # 第1列的范围
x1, x2 = np.mgrid[x1_min:x1_max:200j, x2_min:x2_max:200j]  # 生成网格采样点

grid_test = np.stack((x1.flat, x2.flat), axis=1)  # 测试点

mpl.rcParams['font.sans-serif'] = [u'SimHei']
mpl.rcParams['axes.unicode_minus'] = False
cm_light = mpl.colors.ListedColormap(['#A0FFA0', '#FFA0A0', '#A0A0FF'])
cm_dark = mpl.colors.ListedColormap(['g', 'r', 'b'])

grid_hat = clf.predict(grid_test)       # 预测分类值
grid_hat = grid_hat.reshape(x1.shape)  # 使之与输入的形状相同
plt.pcolormesh(x1, x2,grid_hat, cmap=cm_light)
plt.scatter(x[:, 0], x[:, 1], c=y, edgecolors='k', s=50, cmap=cm_dark)  # 样本
plt.scatter(x_test[:, 0], x_test[:, 1], s=120, facecolors='none', zorder=10)  # 圈中测试集样本
plt.xlabel(u'花萼长度', fontsize=13)
plt.ylabel(u'花萼宽度', fontsize=13)
plt.xlim(x1_min, x1_max)
plt.ylim(x2_min, x2_max)
plt.title(u'鸢尾花SVM二特征分类', fontsize=15)
# plt.grid()
plt.show()

