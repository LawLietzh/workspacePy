#coding:utf-8
'''

LSHash(hash_size, input_dim, num_of_hashtables=1, storage=None, matrices_filename=None, overwrite=False)
parameters:

hash_size:
The length of the resulting binary hash.
input_dim:
The dimension of the input vector.
num_hashtables = 1:
(optional) The number of hash tables used for multiple lookups.
storage = None:
(optional) Specify the name of the storage to be used for the index storage. Options include “redis”.
matrices_filename = None:
(optional) Specify the path to the .npz file random matrices are stored or to be stored if the file does not exist yet
overwrite = False:
(optional) Whether to overwrite the matrices file if it already exist


'''
import lshash
import numpy
lsh = lshash.LSHash(6,8)
lsh.index(numpy.array([1,2,3,4,5,6,7,8]))

lsh.index([2,3,4,5,6,7,8,9])
lsh.index([10,12,99,1,5,31,2,3])
t = lsh.query([1,2,3,4,5,6,7,7])
print(type([1,2,3,4,5,6,7,8]))
print(t)
print(type(t))
l = []
l.append('aaa')
l.append('ccc')
l = numpy.array(l)
print(l)
print(type(l))
