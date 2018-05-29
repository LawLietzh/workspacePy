#coding:utf-8
'''
这里类，用来练习，pandas的DataFrame排序方法小结 


'''
import numpy as np
import pandas as pd
import nltk as a

#创建 dataframe
#np.random.randint(a, b, size=(c, d)),指定生成随机数范围 和生成的多维数组的大小，单个数的话，就是列表
data= [np.random.randint(1,10,4)]
print(data)
data= [np.random.randint(1,10,4)for i in range(5)] #后面加上for i in range(5)，就是生成5 个 长度为4 的列表
print(data)
df = pd.DataFrame(data= [np.random.randint(1,10,4)for i in range(5)],index=range(5),columns=list('ABCD'))
print(df)

#对index 进行排序  对索引列进行排序，默认是 0 ，1,2，排序后是 2 ，1，0
print(df.sort_index(axis=0,ascending=False))
#对columns进行排序
print(df.sort_index(axis=1,ascending=False))
#按单列进行排序
print(df.sort_values('A'))
#按单列进行排序
print(df.sort_values(['A','B']))

# 产生 8 7 6 5 4 3 2 1这八个数
for i in range(8, 0, -1):
    print(i)
'''
问题描述假设有两个字符，要求检查两个字符串的重叠部分并进行拼接。
例如abcdefg和fghik拼接得到abcdefghik，1234和23456拼接得到123456，而1234和678无法拼接。
'''
def checkAndMerge(s1,s2):
    m = min(len(s1),len(s2))
    for i in range(m,0,-1):
        #比较s1的最后的i个字符 是否与 s2的前I字符一样
        if s1[-i:] == s2[:i]:
            return  s1+s2[i:]

print(checkAndMerge('abcdefg', 'fghik'))


#继续DataFrame
#查看数据
#显示前三行
print(df.head(3))

#显示后三行
print(df.tail(3))
#DataFrame的index，columns以及values df.index ; df.columns ; df.values 即可
print(df.index)

#describe()函数 对于数据的快速统计汇总  a.describe()对每一列数据进行统计，包括计数，均值，std，各个分位数等。
print(df.describe())

#转置df.T

# 二，选择对象
#1，选择特定的列 和行的数据
#a['x'] 那么将会返回columns为x的列，注意这种方式一次只能返回一个列。a.x与a['x']意思一样。
print(df.A)
print(df['A'])
#取行数据，可以通过切片[]来选择
print(df[0:3])

#loc 是通过标签来选择数据  则会默认表示选取行为  index 1 这一行；
print(df.loc[1])
#表示选取所有的行以及columns为a b 的列；
print(df.loc[:,['A','B']])
#表示选取1 和2 这两行以及columns为a,b的列；
print(df.loc[[1,2],['A','B']])

#a.loc[1,'a']与a.loc[[1],['a']]作用是一样的，不过前者只显示对应的值，而后者会显示对应的行和列标签。
print(df.loc[1,'A'])

print(df.loc[[1],['A']])

#iloc则是直接通过位置来选择数据