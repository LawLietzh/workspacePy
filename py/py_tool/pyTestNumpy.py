#coding:utf-8
'''
这个文件  主要用来 练习numpy的使用 

'''
import numpy as np
print(np.__version__)
#随机产生 12个 0 到 1 之间的随机数，并变成 三行 四列 的矩阵
arr = np.random.rand(12).reshape(3,4)
print(arr)

#创建 对角线为 1 的对角矩阵 s
arr = np.eye(3, 3)
print(arr)
#创建 全为 1 的矩阵   注意和eye()创建的区别
arr1 = np.ones([3, 3])
print(arr1)


#转置，是多维数组的基本运算之一，
#          随机产生六个 0 -1 之间的数
arr = np.random.rand(6).reshape(2,3)
print(arr)
print(arr.T)

#数组的运算
arr = np.arange(9).reshape(3,3)
print(arr)
print(arr*arr)
print(arr+arr)
#arr个个元素的平方
print(np.square(arr))
#列表 变数组
l = [1,2,3,4]
print(l)
print(np.array(l))

#list 或 tuple 变量 为元素 产生二位数组
print(np.array([[1,2],[3,4]]))
#生成数组的时候，可以指定数据类型，例如：numpy.int32 ,numpy.int16, and numpy.float64

#使用 numpy.arange()
print(np.arange(15))
print(np.arange(15).reshape(3,5))

#numpy.linspace 方法
#在1 到 3 中       产生9个数
print(np.linspace(1,3,9))
# 0 矩阵  1 矩阵  对角为1 的矩阵
print(np.zeros((3,4)))
print(np.ones((3,4)))
print(np.eye(3))
print(np.zeros(3))
c = np.zeros(3)
t = np.multiply(3,c)
print(t)

#数组的索引，切片，赋值
print("#########################################")
a = np.array([[2,3,4],[5,6,7]])


print(a)
print(((a.T)[1:]).T)
#索引
print(a[1,2])
#列  输出第二行
print(a[1,:])
#第2 行的  前两个元素
print(a[1,:2])
#第2行，
print(a[1,1:2])
#行[1：2）
print(a[1:2])
print(a[1,1])

#lie
print(a[:,1])

#使用for 操作元素
#             从1，到3  产生 3 个数(float)
for x in np.linspace(1,3,3):
    print(x)

#数组的基本运算

a = np.ones((2,2))
b = np.eye(2)
print(a)
print(b)
#数组的 加减乘除
print(a>2)
print(a+b)
print(a-b)


#使用数组 对象自带的方法
#所有元素求和
print(a.sum())
#计算每一列的和
print(a.sum(axis=0))
c = np.array([[1,2],[3,4]])
#计算每一列的和
print(c.sum(axis=0))
#计算每一行的和
print(c.sum(axis=1))
#最大值，最小值
print(c.min())
print(c.max())


#使用numpy下的方法
#正弦
np.sin(a)
#取整
np.floor(c)
#e的几次方
np.exp(a)
#
print(a)
#a 是二维 相当于矩阵乘法
#a是一维 相当于 内积
print(np.dot(a,a))

#合并数组

a = np.ones((2,2))
b = np.eye(2)
#竖着合并
print(np.vstack((a,b)))

#横着 合并
print(np.hstack((a,b)))

#深拷贝  ，浅拷贝

# 浅拷贝就是 索引指向 同一个地址
a = np.ones((2,2))
b = a
#true
print(b is a )

#深拷贝，就是 开辟新的内存空间，
c = a.copy()
#false
print(c is a )



#基本的矩阵 运算
a = np.array([[1,0],[2,3]])
print(a)
#转置
print(a.transpose())

#numpy 中矩阵 ，矩阵必须是二维的，他是数组的一个分支，拥有和
#数组同样的操作和特性

a = np.mat('4 3;2 1')
print(a)
#矩阵转置
print(a.T)
#矩阵的  逆矩阵
print(a.I)
b = np.mat('1 2;3 4')
print(b)
#矩阵的积
print(a*b)
print(np.dot(a,b))

c=np.array([[4, 3], [2, 1]])
d=np.array([[1, 2], [3, 4]])
print(a*d)
print(c)
e = np.mat('4 3;2 1')
print(e)
print(np.asmatrix(c))

'''
如果一个程序里面既有matrix 又有array，会让人脑袋大。但是如果只用array，你不仅可以实现matrix所有的功能，还减少了编程和阅读的麻烦。

当然你可以通过下面的两条命令轻松的实现两者之间的转换：np.asmatrix和np.asarray
'''

