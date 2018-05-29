#coding:utf-8

from collections import defaultdict
#defaultdict 解决了 dict 中 不存在默认值的问题
dd = defaultdict(int)
print(dd)
print(dd["foo"])#如果defaultdict 不存在 foo  就默认 给一个int类型的数据  其实默认的是

print(dd)

dd['bar'] = 3
print(dd)

l = []
print(type(l))
l.append(defaultdict(int))
l.append(defaultdict(int))
print(l) #列表中 有两个 字典













