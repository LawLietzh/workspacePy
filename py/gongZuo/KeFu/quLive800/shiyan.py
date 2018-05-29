#coding:utf-8
import numpy

s = [[1,2,3,4,5],[1,2,3,5,5]]
s = numpy.array(s)
print(s)
print(type(s))
print(s[:,0].reshape(-1,1))

lab_pos=numpy.zeros((1,5)).astype(numpy.int64)
ss = lab_pos[:3]
print(lab_pos)
print(ss)
