#coding:utf-8
import  pandas as pd
import  numpy as np
from pyspark.sql import HiveContext
from pyspark import SparkConf,SparkContext
from pyspark.sql import SparkSession

#初始化pandas DataFrame
df = pd.DataFrame([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]], columns=['c1', 'c2', 'c3'])
#
#可以把pandas的数据格式转化为 numpy的array格式的数据
dd = np.array(df)
print(dd)
cc = pd.DataFrame(dd)
print("cccccccccccccccccccccccccccccc")
print(type(cc))
#pandas 用loc来获取某一行数据， 但是 还是显示标号，用tolist转一家就是好了 就是list了
print(df.loc[0].tolist())
print(type(df.loc[0].tolist()))

df.loc[3:6] # 使用了切片，注意：由于这里使用loc[]函数，所以返回的是行标号为3，4，5，6的数据，与python的切片不同的是这里会返回最后的标号代表的数据，但也可以使用python的切片方法：food_info[3:7]

df.loc[[2,5,10]] # 返回行标号为2，5，10三行数据
#练习 返回文件的最后五行，
#方法一
length = df.shape[0]
last_row = df.loc[length-2:length-1]
print(last_row)
#方法2
num_rows = df.shape[0]
last_rows = df.loc[num_rows-2:num_rows]
print(last_rows)
#返回列名称为NDB_No的那一列的数据
xxx = df['c1']
print(xxx)
# 返回两列数据
print(df[['c1','c2']])

#简单运算 对datafram的某一列数据进行算的运算，其实就是对 该列中所以元素进行 逐一运算

chengfa = df['c1']*df['c2']
print(chengfa)

#在








