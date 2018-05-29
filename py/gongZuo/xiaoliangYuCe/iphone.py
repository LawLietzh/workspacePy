#coding:utf-8
'''
这个程序 用来 读懂 销量预测的例子
'''
from pyspark.sql import HiveContext
from pyspark import SparkConf,SparkContext
import pandas as pd
import numpy as np
import matplotlib
from pandas import Series
from pandas import merge
from numpy import array

import matplotlib.pyplot as plt
sc = SparkContext()
sqlContext = HiveContext(sc)
#从表中读取 数据
basedata_hive = sqlContext.sql("select skuid, day, sale, price \
                                   from temp.sale_predict_base_hive where catdname3='手机'  \
                                  order by day")
#把spark类型 的数据转成 pandas的类型的数据
basedata_tmp = basedata_hive.toPandas()
#显示前几条
basedata_tmp.head()
#显示后几条
basedata_tmp.tail()
#统计day 的条数
basedata_tmp.day.count()

from datetime import datetime,timedelta
#把字符串类型的时间类型，转化为时间类型
f = lambda x: datetime.strptime(x,'%Y-%m-%d')
#把f 函数 作用在day这一列上
basedata_tmp['day'] = basedata_tmp['day'].apply(f)
basedata_tmp.head()

from pandas import DataFrame
#构造从2016年 8月三号 开始 ，间隔一天的 ，周期为516的 dataframe
#其实就是从 20168月3号，开始今后的516天 ，并且列用day 表示
timeAll = DataFrame(pd.date_range('8/3/2016', periods=516,freq='1d'))
timeAll.columns = ['day']
timeAll.tail()#显示后面的几个
#
#定义uid 列表
skuids=array(['1123340507','1123340508','1123340454','1123340500','1123340514','1123340499','1123340458',
              '1123340517','1123340293','1123340287','1123502777','1123340506','1123340530','1123240599',
              '1123340503','1123340529','1123200596','1123040399','1123040424','1123502433',
              '1123342800','1123502371','1130000690','1123340509','1123340513','1123240839','1123460046',
              '1123342799','1123232409','1123320140','1130000791','1130012654','1130000891',
              '1123200391','1123340078','1123230704','1122440050','1123502417','1123240758','1123461018',
              '1123240455','1123340295','1123460971','1123260397','1123501585','1123502434','1123510150',
              '1123502310','1123200483','1123340456','1123250191','1123230587',
              '1123040378','1123250177','1123340502','1123502307','1123461017','1123240843',
              '1123240757','1123341903','1123500073','1123340924','1123180506','1123342711','1123180509',
              '1123181305','1123240565','1123500072','1123300416','1123180508',
              '1123460045','1123240759','1123200389','1123240569','1123340519',
              '1123231338','1123200484','1123340023','1123040396','1123250176','1123500649','1123460704',
              '1123230588','1123342705','1123340528','1123500762','1130000827',
              '1123230971','1123510268'])
#创建 列为 ['day','sale', 'price','skuid'] 的dataframe
basedata = DataFrame(columns=['day','sale', 'price','skuid'])

for id in skuids:
    data_tmp = basedata_tmp.ix[basedata_tmp.skuid == id][['day','sale','price']]
    basedata_temp = merge(timeAll, data_tmp, how='left', left_on=['day'], right_on=['day'])
    basedata_temp['sale'] = basedata_temp['sale'].fillna(0)
    basedata_temp['price'] = basedata_temp['price'].fillna(method = 'ffill')
    basedata_temp['price'] = basedata_temp['price'].fillna(method = 'bfill')
    basedata_temp['skuid'] = id
    basedata = pd.concat([basedata,basedata_temp], axis=0)
basedata.head()
