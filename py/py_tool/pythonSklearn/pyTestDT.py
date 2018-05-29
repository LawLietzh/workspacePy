#coding:utf-8
from sklearn import  tree
x = [[0,0],[1,1]]
y = [0,1]
#建模
clf = tree.DecisionTreeClassifier()
#训练
clf = clf.fit(x,y)
#测试
t = clf.predict([[2,2]])
print(t)
#每个分类的概率可以被预测，即某个叶子中
t = clf.predict_proba([[1,0.1]])
print(t)


#上面是二分类，下面是多分类
#用数据集lris ，可以构造下面的树

from sklearn.datasets import load_iris
from sklearn import  tree
iris = load_iris()
print('kkkkk')
#                             模型构建
clf = tree.DecisionTreeClassifier()
clf = clf.fit(iris.data, iris.target)

#训练完成后，我们可以用export_graphviz 将树导出为Graphviz格式
from sklearn.externals.six import StringIO
with open("iris.dot", 'w') as f:
    f = tree.export_graphviz(clf, out_file=f)

import os
os.unlink("iris.dot")

from IPython.display import Image
#import pydot
dot_data = StringIO()
tree.export_graphviz(clf, out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     special_characters=True)

graph = pydot.graph_from_dot_data(dot_data.getvalue())
Image(graph.create_png())
