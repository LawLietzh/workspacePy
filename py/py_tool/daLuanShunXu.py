#coding:utf-8
import numpy as np
r = []
#读取非 utf-8 编码，open('/Users/michael/gbk.txt', 'r', encoding='gbk')
pathX = 'C://Users//zhangheng//Desktop//预料标注//SUIji.txt'
pathD = 'C://Users//zhangheng//Desktop//预料标注//train4_wenti_ChouQu.txt'
t = 0

with open(pathD,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        r.append(line)

np.random.seed(10)
shuffle_indices = np.random.permutation(np.arange(len(r)))
x_text = np.array(r)
x_text = x_text[shuffle_indices]
with open(pathX,'w',encoding='utf-8') as x :
    for line in x_text:
        x.write(line)
        x.write('\n')
