#conding:utf-8
#这类用于 学习Python的函数使用
#Python中很多内置函数，可以方便我们调用
# 求绝对值函数
print(abs(-1))
#help(abs) 可以查看abs 函数 的 帮助信息
#求最大值
print(max(1,2,3,45))
#最小值
print(min(4,5,2,3))

#数据类型 转换
#他数据类型转换为整数
int('123')
#转成字符型
str(1.23)

#定义函数 def    定义一个函数要使用def语句，依次写出函数名、括号、括号中的参数和冒号:

def my_abs(x):
    if not isinstance(x,(int,float)):
        raise TypeError('bad operand type')
    if x >= 0 :
        return x
    else:
        return -x

x = my_abs(98)
print(x)
#函数 默认参数 默认参数 放在后面，且 默认参数 必须指向不变对象 （str None）
def power(x,n =2):
    s = 1
    while n>0:
        n = n-1
        s = s*x
    return s

#可变参数  在参数前面加*
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum  = sum + n*n
    return sum

l  = [1,2,3]
su = calc(*l)
print(su)

# 高级特性 切片
L = ['m','g','h','e','y']
#去前三个元素
#取前三个元素 0 1 2
L[0:3]
L[-1]#取倒数第一个元素
L[-2:]#倒数第二个 到最后 。后两个
L[-2:-1]#倒数第二个 元素

S = list(range(100))
S[:10] #前十个
S[-10:]#后十个

S[:10:2]# 前十个元素   两个取一个
S[::2]#全体元素 ，每5个取一个
S[:] #原样 复制一个

#字符串 也可以 看成是一种list ，每个元素就是一个字符，因此，字符串 也可以用且片 操作 ，操作结果仍是字符串
print('ABCDFGFKL'[:3])


#迭代  Python的for循环不仅可以用在list或tuple上，还可以作用在其他可迭代对象上。

#迭代 字典

d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key,d[key])
    print(key,d.get(key))#词典的两种取值方式

#迭代 value值  如果要同时迭代key和value，可以用for k, v in d.items()。
for value in d.values():
    print(value)


#如果要对list实现类似java那样的下标循环怎么办，Python内置的enumerate函数可以把一个list变成索引-元素对
for i , value in enumerate(['a','b','c']):
    print(i,value)

#列表生成式
p = list(range(1,11))
print(p)

p = [x*x for x in range(1,11)]
print(p)
#for循环后面还可以加上if判断，这样我们就可以筛选出仅偶数的平方：
p = [x*x for x in range(1,11) if x%2 == 0]
print(p)

#还可以使用两层循环
p = [m + n for m in 'ABC' for n in 'XYZ']

#运用列表生成式，可以写出非常简洁的代码，例如，列出当前目录下的所有文件和目录名，可以通过一行代码实现：

import os
di = [d for d in os.listdir('.')]#os.listdir 可以列出文件和目录
#把一个list中所有的字符串变成小写

L = ['Hello', 'World', 'IBM', 'Apple']
[s.lower() for s in L]

tu = (1,2,34)
print(tu)
#在Python中，这种一边循环一边计算的机制，称为生成器：generator。
g = (x * x for x in range(10))
#如果要一个一个打印出来，可以通过next()函数获得generator的下一个返回值：
for n in g:
    print(n)

#斐波拉契数列
def fib(max):
    n,a,b = 0,0,1
    while n< max:
        print(b)
        a,b = b ,a+b
        n = n+1
    return  'done'
#上面的函数和generator仅一步之遥。要把fib函数变成generator，只需要把print(b)改为yield b
#这就是定义generator的另一种方法。如果一个函数定义中包含yield关键字

def odd():
    print('step 1')
    yield 1
    print('step 2')
    yield(3)
    print('step 3')
    yield(5)

o = odd()
#最难理解的就是generator和函数的执行流程不一样。函数是顺序执行，遇到return语句或者最后一行函数语句就返回。而变成generator的函数，在每次调用next()的时候执行，遇到yield语句返回，再次执行时从上次返回的yield语句处继续执行。
next(0)





