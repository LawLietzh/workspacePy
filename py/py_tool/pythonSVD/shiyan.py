#coding:utf-8
from numpy import *
from numpy import  linalg as la
myMat = [[1,1,1,0,0],
         [2,2,2,0,0],
         [1,1,1,0,0],
         [5,5,5,0,0],
         [1,1,0,2,2],
         [0,0,0,3,3],
         [0,0,0,1,1]
         ]

my = mat(myMat)
std = mat([2,1,2,2,2])
mean =mat( [1,2,1,1,1])
mm = mat([  2.14981892e+03 ,1.47436806e-01  , 4.41978579e+01 ,  2.33697180e+03, 1.03915221e+00 ,  6.00334859e-03,   2.19523834e-02])
sca= mat([  2.13609560e+03  , 1.11963545e+00 ,  1.17390350e+02 ,  2.90146126e+03, 2.59522774e+00 ,  7.72483553e-02  , 1.46528073e-01] )
#print(my-mean)
#print(my/std)
myMat =(my-mean)
print(myMat )
myMat = myMat/std
print(myMat)

print((my-mean)/std)


m = [[0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 5],
     [0, 0, 0, 3, 0, 4, 0, 0, 0, 0, 3],
     [0, 0, 0, 0, 4, 0, 0, 1, 0, 4, 0],
     [3, 3, 4, 0, 0, 0, 0, 2, 2, 0, 0],
     [5, 4, 5, 0, 0, 0, 0, 5, 5, 0, 0],
     [0, 0, 0, 0, 5, 0, 1, 0, 0, 5, 0],
     [4, 3, 4, 0, 0, 0, 0, 5, 5, 0, 1],
     [0, 0, 0, 4, 0, 4, 0, 0, 0, 0, 4],
     [0, 0, 0, 2, 0, 2, 5, 0, 0, 1, 2],
     [0, 0, 0, 0, 5, 0, 0, 0, 0, 4, 0],
     [1, 0, 0, 0, 0, 0, 0, 1, 2, 0, 0]]

'''
print(type(myMat))
print(type(mat(myMat)))

print(type((mat(myMat)).A ))
print(mat(myMat))
print(mat(myMat)
'''
u1,sigma ,v = linalg.svd(mat(m))
print(u1)

u2,sigma ,v = linalg.svd(mat(m))
print(u2)
'''
for i in range(200):
    print(i)
    u1,sigma ,v = linalg.svd(mat(m))
    #print(u1)

    u2,sigma ,v = linalg.svd(mat(m))
    #print(u2)
    t = (u1==u2).all()

    print(t)

'''

print(5/2)