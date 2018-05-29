#coding:utf-8
import  numpy as np
import datetime
import  time
#获取当前时间
now = time.strftime('%y-%m-%d')
print(now)

import datetime
now_time = datetime.datetime.now()
yes_time = now_time + datetime.timedelta(days=-1)
yes_time_nyr = yes_time.strftime("%Y-%m-%d")#格式化输出
print(yes_time_nyr)

l = [[1,2],[3,4],[5,6],[3,4],[5,6]]
l = np.array(l)


x = (l[:,0]).reshape(-1,1)
print(x)



print(l.shape)
t = 0
p =2
while t < l.__len__():
    ll = l[t:t+p]
    print(ll)

    t = t+p



print("11111111111111111111111111")
print(l.__len__())
print(l[0:13])
print(l)
s = [1,2]
s = np.array(s)
print(s)

s = []

for line in l:
    print(type(line))



