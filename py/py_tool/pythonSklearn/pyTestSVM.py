#coding:utf-8
'''

练习svm的使用

'''
#分类模型 SVC(support vectors classification)
from sklearn.svm import  SVC
#回归模型
from sklearn.svm import  SVR

x = [[0,0],[1,1],[1,0]]
y=[0,1,1]
'''
#加上括号里的参数，可以输出概率值
#分类
clf = SVC(probability=True)
clf.fit(x,y)
result = clf.predict([[2,2]])
print(result)
print(clf.support_vectors_)
result = clf.predict_proba([[2,2]])
print(result)
'''

#回归
clf = SVR()
clf.fit(x,y)
#result = clf.predict_proba([[2,2]])
result = clf.predict([[2,2]])
print(result)
