#conding：utf-8

#字母转数字
print(ord('A'))
#数字转字母
print(chr(66))

#python 中数据结构  list
#list 是一个 可变的 有序表
cl = ['m','n','c']
print(cl)
print(len(cl))
print(cl[2])
print(cl[-1])#输出倒数第几个数
#在末尾添加数据
cl.append('aaa')
#在指定位置 插入
cl.insert(1,'bbbb')
print(cl)
#删除末尾元素
cl.pop()
#删除指定位置的元素
cl.pop(1)

#元组tuple  tuple 一旦初始化就不能修改，

tu = ('c','v','a')
print(tu)
#定义tuple
tt = ()
#只有1个元素的tuple定义时必须加一个逗号,，来消除歧义
t = (1,)

#条件判断 elif  是 else if 的缩写
age = 20
if age>=18:
    print('your age is ',age)
elif age >= 6:
    print('s')


#循环
names = ['m','v','e','t']
for name in names:
    print(name)
#产生 0 到4  的整数
k = list(range(5))

#dict 和 set
#python 中dict相当于map  查找速度极快
d = {'m':95,'b':6,'t':8}
print(d['m'])
#如果key不存在，dict会报错，要必要key不存在的错误，有两种办法
#一是通过 in 判断 key是否存在
#二是通过d.get('m') ，key不存在会返回 None
print(d.get('m')) #返回 对应k的value值
#删除 数据
d.pop('t')
print(len(d))
#list 中的顺序 和 放入数据一样，dict 中的顺序和放入无关


#set 和dict 类似，但是不存储value ，key值不能重读 要创建一个set，要提供一个list 作为输入集合
#set 是无序的
s = set([1,23,4])
print(s)
#set的 添加和删除
s.add(5)
print(s)
s.remove(1)
print(s)

#sort 排序
a = [3,6,2]
print(a)
a.sort()
print(a)