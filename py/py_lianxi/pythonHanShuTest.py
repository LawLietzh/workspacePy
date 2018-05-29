#coding:utf-8
#调用 另一个类中的函数
#from pythonHanShu import my_abs
#a = my_abs(-8)
#print(a)

#高阶函数
#map/reduce
#map  map()函数接收两个参数，一个是函数，一个是序列，map将传入的函数依次作用到序列的每个元素，并把结果作为新的list返回。

def f(x):
    return x*x

l = list(map(f,[1,2,3,4,5]))
#好像 map() 函数返回的Iterator  智能输出一次

print(l)

print('dddddd')
k = [8,9,0]
print(k)

#reduce  reduce把一个函数作用在一个序列[x1, x2, x3, ...]上，这个函数必须接收两个参数，reduce把结果继续和序列的下一个元素做累积计算
from functools import  reduce
def ad(x,y):
    return x+y
su = reduce(ad,[1,2,3,5])
print(su)
#sum是一个内置的  求和 函数
k = sum([1,2,3,4,5])
print(k)
#现在看来，map 是吧函数 作用在 每一个 迭代值上
#reduce 是 连续的操作，

#reduce的例子  把序列[1, 3, 5, 7, 9]变换成整数13579，reduce就可以派上用场
def fn(x,y):
    return x*10+y

t = reduce(fn,[1 ,3,5,7,9])
print(t)

#把 str 转成 int
def char3num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]
# map 以后 返回的 迭代  要有list 在转一下
print(  list (map(char3num, '1234')))

#filter 过滤 函数
#filter()把传入的函数依次作用于每个元素，然后根据返回值是True还是False决定保留还是丢弃该元素。

def is_odd(n):
    return n%2 == 1

print( list(  filter(is_odd,[1,2,3,4,5,6,]) ) )

#python 内置函数 sorted()
so = sorted([36,5,-12,9,-21])
print(so)
# sorted() 函数也是 一个高阶函数，它还可以接收一个 key 函数，来实现自定义的排序

so = sorted([36,5,-12,9,-21],key=abs)
print(so)
ss = sorted(['bob', 'about', 'Zoo', 'Credit'])
print(ss)
#我们给sorted传入key函数，即可实现忽略大小写的排序：
ss = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower)
print(ss)
#要进行反向排序，
ss = sorted(['bob', 'about', 'Zoo', 'Credit'], key=str.lower, reverse=True)
print(ss)
#另一种 翻转
ss = [1,2,3,4,5]
print(ss[::])
print(ss[::-1])
#排序 元组
def by_name(t):
    return t[0]

L =[('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
#按照名字排序
print(sorted(L ,key=by_name))

def by_sort(t):
    return t[1]
#按照分数 排序
print(sorted(L, key=by_sort))

#匿名 函数 lambda

l = list(map(lambda x:x*x,[1,2,3,4,5]))
print(l)