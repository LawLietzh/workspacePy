#coding：utf-8
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):

    def run(self):
        print('Dog is running...')

class Cat(object):

    def run(self):
        print('Cat is running...')

cat = Cat()
dog = Dog()
cat.run()
dog.run()

#使用type() 函数 来判断对象类型
type(123)
#class的继承关系来说，使用type()就很不方便。我们要判断class的类型，可以使用isinstance()
'''
try:
    print('try')
except ZeroDivisionError as e:
    print('except',e)
finally:
    print('finally')
'''
#python lpgging 代替print
#logging
import  logging
logging.basicConfig(level= logging.INFO)
s = '1'
n = int(s)
logging.info('n = %d' %n)
print(10/n)
#logging 的好处，它允许你指定 记录信息的级别，
#有debug info ，warning,error 等几个级别


#操作文件和目录
import  os
#如果是posix，说明系统是Linux、Unix或Mac OS X，如果是nt，就是Windows系统
print(os.name)
#要获取详细的系统信息，可以调用uname()函数：
#print(os.uname())   但是在windows 上不提供

#操作文件  和目录
#操作文件和目录的函数一部分放在os模块中，一部分放在os.path模块中，这一点要注意一下

#查看 当前目录的绝对路径
print(os.path.abspath('.'))

#在某个路径下，创建一个新目录 ，首先把新目录的完整路径表示出来
print(os.path.join('D://workspacePy/py/py_lianxi','testdir1'))
#创建目录，要先表示出来
#os.mkdir('D://workspacePy/py/py_lianxi/testdir1')
#os.rmdir('D://workspacePy/py/py_lianxi/testdir1')
#把两个路径 合成一个的时候，不要直接拼字符串，而是要通过os.path.join()函数
#要拆分路径时，也不要直接去拆字符串，而要通过os.path.split()函数，这样可以把一个路径拆分为两部分，后一部分总是最后级别的目录或文件名：
print(os.path.split('/Users/michael/testdir/file.txt'))
#对文件重命名
#os.rename('','')
#删除文件
#os.remove()


#列出当前目录下的所有目录，只需要一行代码：
l = [x for x in os.listdir('.') if os.path.isdir(x)]

print('dirs:  ',l)

#要列出所有的.py文件，也只需一行代码

l = [x for x in os.listdir('.') if os.path.isfile(x) and os.path.splitext(x)[1]=='.py']
print(l)


#序列化
import pickle
#我们 尝试，把一个对象序列化，并写入文件

d = dict(name='Bob', age=20, score=88)
#pickle.dumps()方法把任意对象序列化成一个bytes，然后，就可以把这个bytes写入文件。或者用另一个方法pickle.dump()直接把对象序列化后写入
pickle.dumps(d)

#或者 直接写到文件中
f = open('d://dump.txt','wb')
pickle.dump(d, f)
f.close()

#读取 序列化
f = open('d://dump.txt','rb')
d = pickle.load(f)
f.close()
print(d)

#如果我们要在不同的语言之间传递对象，就必须要对象序列化为标准格式，比如xml，更好的方法是，序列化为 JSON ，
#因为json表示出来 就是是一个字符串,可以被所有语言读取，也可以方便地存储到磁盘，或者通过网络传输

#把Python对象变成一个JSON：
import  json
d = dict(name='AAAA', age=20, score=88)
#json之后 变成了字符串  dump()方法可以直接把JSON写入一个file-like Object。

a = json.dumps(d)
print(type(a))

print(json.loads(a))

#json序列化 class
class Student(object):
    def __init__(self,name,age,score):
        self.name = name
        self.score = score
        self.age = age

s = Student('Bob',20,88)
#要用json 序列化 类，就要为  类 ，专门写一个转换函数 ，再把函数传进去

def student2dic(std):
    return {
        'name': std.name,
        'age': std.age,
        'score': std.score
    }

#这样，Student实例首先被student2dict()函数转换成dict，然后再被顺利序列化为JSON：
#print(json.dumps(s, default=student2dic))
#下次如果遇到一个Teacher类的实例，照样无法序列化为JSON。我们可以偷个懒，把任意class的实例变为dict：
print(json.dumps(s, default=lambda  obj: obj.__dict__))

#如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，

def dict2student(d):
    return  Student(d['name'],d['age'], d['score'])
#序列化之后的，数据
json_str = '{"age": 20, "score": 88, "name": "Bob"}'
#反序列话
print(json.loads(json_str, object_hook=dict2student))

