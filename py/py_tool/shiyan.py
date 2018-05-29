#conding:utf-8
import jieba
import  numpy
from datetime import datetime
import time

seg_list = list(jieba.cut('请帮查一订单物流',cut_all = True))
a = (','.join(seg_list)).replace(',',' ')

print(a)
l = [1,2,3]
print(l[0])
print(l[1])
print(l[2])

l = numpy.arange(5)
print(l)
print(datetime.now())
t = time.strftime("%Y-%m-%d")
print(type(t))

str = "insert into dm_tag.hytx partition(log_day = "+"\'"+ t + "\'"+")"
print(str)