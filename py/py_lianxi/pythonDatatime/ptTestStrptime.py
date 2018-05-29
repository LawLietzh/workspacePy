#coding:utf-8

'''
测试  python time strptime()方法 
strptime（）函数根据指定的格式把一个时间字符串解析为时间元组 
'''
import time
import datetime
'''
print( time.localtime(time.time())  )
print(  time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))  )
print(  time.strftime('%Y-%m-%d',time.localtime(time.time()))  )

print(  datetime.strptime(   time.localtime(time.time())   ,'%Y-%m-%d')  )
'''


#常用的时间转换 和 处理函数
#获取当前时间
d1 = datetime.datetime.now()
print(d1)

#当前时间加上 半个小时
d2 = d1+ datetime.timedelta(hours=0.5)
print(d2)

#格式化字符串 输出
d3 = d2.strftime('%Y-%m-%d %H:%M:%S')
print(d3)

print(d2.strftime('%Y-%m-%d'))

#将字符串传化为时间类型
date="2017-10-09 16:25:42"
#   data的格式要和 后面的一样
d4 = datetime.datetime.strptime(date,'%Y-%m-%d %H:%M:%S')
print(d4)



