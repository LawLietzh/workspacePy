#coding:utf-8
import pandas as pd
import numpy as np
from  openpyxl import  *
import matplotlib.pyplot as plt
'''
这个方法用来，测试 ，练习pandas

'''
#1。可以通过传递一个list对象来创建一个Series，pandas会默认创建整型索引：
#Series 就是给list 编号
s = pd.Series([1,3,5,np.nan,6,8])
print(s)
#通过传递一个 numpy array ，时间索引以及列标签 来创建一个DataFrame
#根据传入的如期和 ，遍历日期
dates = pd.date_range('20130101', periods=6)




#np.random.rand(6,4) 随机产生 （6,4）的数组
df = pd.DataFrame(np.random.rand(6,4),index=dates,columns=list('ABCD'))
df = np.array(df)
print(df)
print(type(df))
df = pd.DataFrame(df)
print(type(df))
print("aaaaaaa")
print(df)
for index ,row in df.iterrows():
    print(index,"     ",row)


#显示头部的行
print(df.head())
#显示尾部的行
print(df.tail(3))
#显示 索引 ，列 和底层的numpy数据
print(df.index)
print(df.columns)
print(df.values)
#describe(）函数，对数据快速统计
print(df.describe())
#对数据进行转置
print(df.T)



'''
重点来了，写入 Excel 文件 
'''
#写入Excel 文件  写进去了，但是索引乱码
df.to_excel('C://Users//zhangheng//Desktop//zxl//foo.xlsx',sheet_name='Sheet1')

#从Excel中读取数据
print('读数据****')
'''
x = pd.read_excel('C://Users//zhangheng//Desktop//zxl//lixiang717.xlsx','Sheet1',index_col=None,na_values=['NA'])
f = open('C://Users//zhangheng//Desktop//zxl//lixiang717.txt','w',encoding='utf-8')
f.write(str(x))
f.close()
'''

df = pd.read_excel("C://Users//zhangheng//Desktop//zxl//lixiang717.xlsx")
print(df.dtypes)
#获取除 表头外 开始的第五列数据
col_data = list(df.ix[:,5])

print(col_data)
#获取除 表头外 开始的第五行数据
col_data = list(df.ix[5, :])

print(col_data)

xls_file = pd.ExcelFile("C://Users//zhangheng//Desktop//zxl//lixiang717.xlsx")
print(xls_file.sheet_names)
table1=xls_file.parse('Sheet1')
print(table1)