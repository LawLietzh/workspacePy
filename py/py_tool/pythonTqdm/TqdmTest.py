#coding:utf-8
'''
Tqdm 是一个快速，可扩展的python进度条，可以在python长循环中添加一个进度提示信息，用户只需要封装
任意迭代器 tqdm(iterator)

'''
import  time
from tqdm import tqdm
for i in tqdm(range(10000)):
    #time.sleep(0.01)
    print(i)






















