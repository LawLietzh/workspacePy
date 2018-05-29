#coding:utf-8
'''
练习statsmodels 模块的使用 
'''
import statsmodels
import matplotlib
from statsmodels.tsa.seasonal import seasonal_decompose
import  numpy as np
from statsmodels.tsa.arima_model import ARIMA
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import  os
import numpy as np
import pandas as pd
import numpy as np
import matplotlib



matplotlib.use('Agg')
#读取文件 下的所以 数据列表
path = "E://数据资料//用户画像资料//工作//销量预测历史数据//test//"
'''
R01 彩电 
R03 空调
R05 冰箱 
R06 洗衣机
l = []
pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)

for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        line = line.strip()
        print(line)
        array = line.split('\t')
        str = array[2].strip()
        if str =='R01':
            l.append(array[0:2])

print(l.__len__())
arr = np.array(l)
'''
path1 = 'E://数据资料//用户画像资料//工作//test.csv'
l = []
pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    #print(child)
    pathdir.append(child)

for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        line = line.strip()
        #print(line)
        array = line.split('\t')
        str = array[2].strip()
        if str =='R01':
            l.append(array[0:2])

print(l.__len__())
arr = np.array(l)
basedate = pd.DataFrame(arr,columns=['day','sale'])
print(basedate)
basedate.index = pd.to_datetime(basedate.day)


print(basedate.tail())

from statsmodels.tsa.seasonal import seasonal_decompose
ts = basedate['sale']
#ts = ts.resample('w').sum()
ts = ts.fillna(0)
ts.describe()



print(ts['2015'])

#平稳性处理   a 对数变换， b ,平滑法
#a
ts_log = np.log(ts['sale'])

#b
diff_12 = ts_log.diff(12)
diff_12.dropna(inplace=True)
diff_12_1 = diff_12.diff(1)
diff_12_1.dropna(inplace=True)



'''
decomposition = seasonal_decompose(ts,freq=1, model="additive")
trend = decomposition.trend
seasonal = decomposition.seasonal
residual = decomposition.resid
print("444444444444")
print(trend[26:79])

'''
