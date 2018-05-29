#coding:utf-8
import sklearn
import  numpy as np
import matplotlib.pyplot as plt
print(sklearn.__version__)
#定义x的范围
h = np.arange(-10,10,0.1)
def sigmoid(h):
    return 1.0 / (1.0 + np.exp(-h))

s_h = sigmoid(h)
#画图
plt.plot(h,s_h)
#在坐标轴上加一条竖直 的线，0.0位竖直线 在坐标轴上的位置
plt.axvline(0.0,color='K')
# 加水平间距通过坐标轴
plt.axhspan(0.0,1.0,facecolor = '1.0',alpha = 1.0,ls = 'dotted')
plt.axhline(y=0.5, ls='dotted', color='k') # 加水线通过坐标轴
#plt.yticks([0.0, 0.5, 1.0]) # 加y轴刻度
#plt.ylim(-0.1, 1.1) # 加y轴范围
#plt.xlabel('h')
#plt.ylabel('$S(h)$')
plt.show()


