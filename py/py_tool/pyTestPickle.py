#coding:utf-8
#主要 介绍 python pickle 模块用法实例，Python的pickle模块实现了基本的数据序列 和反序列化，

import  pickle
'''
pickle.dump(obj,file,[,protocol])
将对象obj 保存到文件file 中去 


'''
shoplistfile = './model/shoplist.data'
shoplist = ['apple','mango','carrot']
f = open(shoplistfile,'wb')
pickle.dump(shoplist,f)
f.close()
del shoplist
f = open(shoplistfile,'rb')
storedlist = pickle.load(f)
print(storedlist)
