#coding:utf-8
from pandas import DataFrame
import pandas as pd
timeAll = DataFrame(pd.date_range('8/3/2016', periods=252,freq='1d'))
print(timeAll.head())


timeAll.columns = ['day']
print(timeAll.tail())

basedata = DataFrame(columns=['day','sale', 'price','skuid'])
print(basedata)
#随机划分 训练集 和测试集
from sklearn.cross_validation import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X_trans, y, random_state=1, test_size = 0.4, train_size = 0.6)


