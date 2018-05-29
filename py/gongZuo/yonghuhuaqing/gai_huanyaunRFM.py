#coding:utf-8
'''
会员价值等级模型判定

'''
import  os
import numpy as np
#读取数据
shuju = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12,],[13,14,15,16]])
print(shuju)
q = [0.5,0.3,0.2]
for pa in shuju:
    print(pa[0])


for pa in shuju:
    print(pa)

    if pa.__len__() == 4:
        uid  = pa[0]
        uidM = float(pa[1])
        uidF =float(pa[2])
        uidR = float(pa[3])
        rank = []

        #下面开始 判断金额
        if uidM<=1000:
            rank.append(1)
        elif uidM>1000 and uidM<=5000:
             rank.append(2)
        elif uidM>5000:
             rank.append(3)

        #下面开始 判断次数
        if uidF<2:
            rank.append(1)
        elif uidF>=2 and uidF<=5:
            rank.append(2)
        elif uidF>5:
            rank.append(3)

        #下面开始 判断天数
        if uidR<100:
            rank.append(3)
        elif uidR>=100 and uidR<=200:
            rank.append(2)
        elif uidR>200:
            rank.append(1)
        print(rank)

        #计算得分
        if rank.__len__()!=3:
             print('rank is not 3:',rank,pa)
        score = np.matmul(rank,q)

        print(score)

    elif pa.__len__() != 4:
        print(pa)
        print('the len of line is not 4')




