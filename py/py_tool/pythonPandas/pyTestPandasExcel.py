#coding:utf-8
'''
pandas 处理excel 数据

'''
import numpy as np
import  pandas as pd
path = "C:/Users/zhangheng/Desktop/lixiang/lixiang912/9.12机器人问答.xlsx"
path1 = "E://数据资料//用户画像资料//工作//test.csv"
df = pd.read_excel(path)
print(df.loc[0:3])

#根据列 索引   删除某一列   得到新的dataframe
df1 = df.drop('序号',axis=1)
print(df1.loc[0:3])

#根据列 索引   删除某一列    也可以直接在原DataFrame上原地删除：
df.drop('序号',axis=1,inplace=True)
print(df.loc[0:3])
print("dddddd")
#把表中空值变为1
df1 = df.replace({np.nan:0})
print(df1.loc[0:3])

