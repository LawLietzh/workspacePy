#coding:utf-8
import  lshash
lshash.LSHash(6,7)
lsh = lshash.LSHash(6, 8)
lsh.index([1,2,3,4,5,6,7,8])

lsh.index([2,3,4,5,6,7,8,9])
lsh.index([10,12,99,1,5,31,2,3])
t = lsh.query([1,2,3,4,5,6,7,7])
print('sss')
print(t)