#coding:utf-8
import  pandas as pd
import  numpy as np

path ='C://Users//zhangheng//Desktop//lixiang//lixiang717.xlsx'
df = pd.read_excel(path)
#除表头    开始的 第五列数据（）
col_data = list(df.ix[:,5])
for line in col_data:
    print(str(line).replace('\n',''))


print('************************')


col_data = list(df.ix[5,:])
for line in col_data:
    print(str(line).replace('\n',''))

