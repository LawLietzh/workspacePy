#coding:utf-8
import  random
str = '  赞     绝对 5 星 好评 '
line = str.strip()
print(line)
#随机从list中获取几个元素，作为一个片段返回，
list = [1,2,3,4,5,6,7,8,9,0,1,2]
slice = random.sample(list,5)
print(slice)
print(list)



