#coding:utf-8

# coding: utf-8
import os
#spark-submit --master local 执行标识
from pyspark.sql import HiveContext
from pyspark import SparkConf,SparkContext
import pandas as pd
import numpy as np
import sklearn
from sklearn.preprocessing import MinMaxScaler
import time

sc = SparkContext()
sqlContext = HiveContext(sc)
data = [("Alice", 21), ("Bob", 24)]
people = sqlContext.createDataFrame(data, ["name", "age"])

people.show(1)











