#coding:utf-8
import  numpy as np

x = np.random.rand(9).reshape(3,3)
print(x)
print(type(x))
#取每一行的，第0 和第1 列
print(x[:,[0,1]])
#获取第一行的数据
print(x[0,:])
#取前两个样本，的第0 列数据
print(x[:2,0])


#np.bincount()从 零开始计数   统计 类别个数
t = np.bincount([3, 4, 4, 3, 3, 5])
#分别表示0 ，1，2,3,4,5 出现的次数
print(t)

#np.average()
'''
np.average(X, axis=0, weights=w) == w.dot(X)
等式左部 表示加权平均 ，sum（w） == 1 时 才有意义，也即等式的左部比等式的右部多了一层加权平均的意义，内积代表着实现该意义的动作
'''

X = np.array([[9,1],[8,2],[4,6]])
print(X)
print("ssssssssssssss")
print(X[0][0])
he = (X[:,0] + X[:,1]).reshape(-1,1)
hebing = np.hstack((he,he))
print(hebing)


w = np.array([2,2,6])
print(w.dot(X))
print(np.average(X, axis=0, weights=w))
print(X)
print(X[:,0])
#矩阵 只能 按照列来 乘  /除
t = X*[0.5,0.5]
print('**************')
print(t)
#axis = 0 ,按列求和
print(t.sum(axis=0))
d = t.sum(axis=0)
#按行求和
d = t.sum(axis=1)
print(d)
#实现每一列 乘以一个数，然后除以这一行的和
print((t.T/d).T)

