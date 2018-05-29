#coding:utf-8
'''
会员价值等级模型判定

'''
import  os
import numpy as np
#读取数据
path = 'E://数据资料//数据集合//test//'
pathW =  'E://数据资料//数据集合//uidRank.txt'
#写数据
w = open(pathW,'w',encoding='utf-8')
pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)

# 会员id  uid
#  金额  阈值设为 大于 5000   uidM =
#次数   uid 设为 大于等于3   uidF = []
#  天数 为 100   uidR = []

q = [0.5,0.3,0.2]

for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        strArray = line.strip().split('\t')
        if strArray.__len__() == 4:
            uid  = strArray[0].strip()
            uidM = float(strArray[1].strip())
            uidF =float(strArray[2].strip())
            uidR = float(strArray[3].strip())
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
                print('rank is not 3:',rank,line)
            score = np.matmul(rank,q)

            print(score)
            w.write(uid+'\t'+str(score))
            w.write('\n')
            #f.write(uid+'\t'+score)
            #f.write(uid+'\t'+score)
            w.flush()
        elif strArray.__len__() != 4:
            print(line)
            print('the len of line is not 4')




