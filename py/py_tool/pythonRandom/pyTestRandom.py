#coding:utf-8
'''
练习 python 中random模块用于生成
random.random() 用于生成一个0 到 1 的随机浮点数 
random.uniform（a,b） 用于生成一个指定范围内的随机浮点数 ，一个是上限，一个是下线
random.randint（a,b） 用于生成 一个指定 范围内 的整数。 其中a 是下线，b 是上线
random.randrange(10,100,2)  结果相当于 [10，,12,14,16，。。。]    random.choice(range(10, 100, 2) 等效。
random.choice（sequence） sequence 表示一个有序类型 类似 list  tuple ，

random.shuffle（x[,random]）。用于将一个列表中的元素打乱  。
random.sample（sequence，k） 从指定序列中随机获取指定长度 的片段  。sample 不会修改原有序列 
'''
import  numpy
print(numpy.random.choice(["学习Python"]))
print(numpy.random.choice(["JGood", "is", "a", "handsome", "boy"]))

p = ["Python", "is", "powerful", "simple", "and so on..."]
numpy.random.shuffle(p)
print(p)


y_test = numpy.random.randint(10, size=(100, 1))
print(y_test)





























