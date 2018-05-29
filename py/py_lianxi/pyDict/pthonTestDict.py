#coding：utf-8
'''
python 两种遍历字典的方法
'''

d = {'a':1,'b':0,'c':1,'d':0}
#遍历一个dict结构，大部分都是适用的，但是并不是完全安全的
#for k in d:
    # d[k] == 0:
        #del(d[k])

#d.keys(） 可以返回一个下标的数组
print(d.keys())
'''
keys = list(d.keys())
for key in keys:
    if
    del(d[key])
print(d)
'''
#d.keys() 将字典 d 中所有的键以dict_keys形式返回（Python 2 中d.iterkeys() 返回一个针对键的迭代器对象，Python 3 没有此语法）
l = list(d.keys())
print(l[0])
for k in l:
    if d[k] == 0:
        del(d[k])

print(d)