#coding:utf-8

'''
整合会员价值等级模型
和用户忠诚度计算

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



def dengJi(line):
    #line = str(line)
    #print(line)
    #print(type(line))
    q = [0.5,0.3,0.2]
    strArray = line.strip().split('\t')
    score = 0
    if strArray.__len__() == 4:
        uid  = strArray[0].strip()
        uidM = float(strArray[1].strip())
        uidF =float(strArray[2].strip())
        uidR = float(strArray[3].strip())
        rank = []

        #下面开始 判断金额
        if uidM<=1000:
            rank.append(1)
        elif uidM>1000 and uidM<=3000:
            rank.append(2)
        elif uidM>3000:
            rank.append(3)

        #下面开始 判断次数
        if uidF<2:
            rank.append(1)
        elif uidF >= 2 and uidF <=8 :
            rank.append(2)
        elif uidF > 8:
            rank.append(3)

        #下面开始 判断天数
        if uidR<80:
            rank.append(3)
        elif uidR>=80 and uidR<=160:
            rank.append(2)
        elif uidR>160:
            rank.append(1)
        #print(rank)

        #计算得分
        if rank.__len__()!=3:
            print('rank is not 3:',rank,line)
        score = np.matmul(rank,q)
    elif strArray.__len__() != 4:
        print(line)
        print('the len of line is not 4')



    return  score



#忠诚度
def get_customer_loyalty(line):

    strArray = line.strip().split('\t')
    if strArray.__len__() == 4:

        amount = float(strArray[1].strip())
        nums =float(strArray[2].strip())
        days = float(strArray[3].strip())

        #下面开始 判断金额
        if amount <= 5000:
            amount_weight = 2
        if 5000 < amount <= 10000:
            amount_weight = 3
        if amount > 10000:
            amount_weight = 5

        #下面开始 判断次数
        if nums <= 1:
            nums_weight = 4
        if 1 < nums <= 3:
            nums_weight = 3
        if 3 < nums <= 50:
            nums_weight = 2
        if nums > 50:
            nums_weight = 1

        #下面开始 判断天数
        if days <= 10:
            days_weight = 4
        if 10 < days <= 100:
            days_weight = 3

        if 100 < days <= 200:
            days_weight = 2

        if days > 200:
            days_weight = 1
        #print(rank)

        #计算得分
        customer_loyalty = float(0.2 * amount_weight + 0.5 * nums_weight + 0.3 * days_weight)

    elif strArray.__len__() != 4:
        print(line)
        print('the len of line is not 4')
    return customer_loyalty




for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        strArray = line.strip().split('\t')
        #获得会员价值分数
        score = dengJi(line)
        #获得忠诚度 分数
        customer_loyalty = get_customer_loyalty(line)

        uid = strArray[0].strip()
        print(score)
        print(uid+'\t'+str(score)+'\t'+str(customer_loyalty))
        #w.write(uid+'\t'+str(score)+'\t'+customer_loyalty)
        #w.write('\n')


        #w.flush()


#w.close()


