#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'a test modul'
__author__ = 'zhangheng'
#任何模块代码的第一个字符串都被视为模块的文档注释；
#以上就是Python模块的标准文件模板

import sys
def test():
    #命令行参数List，第一个元素是程序本身路径
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# if __name__ == '__main__':
#     test()
#和普通的函数相比，在类中定义的函数只有一点不同，就是第一个参数永远是实例变量self，并且，调用时，不用传递该参数
class Student(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score
    def print_score(self):
        print('%s:%s' % (self.name,self.score))

bart = Student('A',89)
lisa = Student('B',87)
bart.print_score()
lisa.print_score()
#如果要让内部属性不被外部访问，可以把属性的名称前加上两个下划线__
class Student1(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        return self.__name

    def get_score(self):
        return self.__score

    def set_score(self, score):
        self.__score = score














