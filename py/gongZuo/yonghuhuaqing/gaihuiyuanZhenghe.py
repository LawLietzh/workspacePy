#coding:utf-8

'''
整合会员价值等级模型
和用户忠诚度计算

'''
import  os
import numpy as np

ss = np.array([['天','下'],['五','零']])
print(ss)

shuju = np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12,],[13,14,15,16]])
print(shuju)



def dengJi(line):
    q = [0.5,0.3,0.2]
    score = 0
    if line.__len__() == 4:
        uidM = float(line[1])
        uidF =float(line[2])
        uidR = float(line[3])
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
    elif line.__len__() != 4:
        print(line)
        print('the len of line is not 4')



    return  score



#忠诚度
def get_customer_loyalty(line):


    if line.__len__() == 4:

        amount = float(line[1])
        nums =float(line[2])
        days = float(line[3])

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

    elif line.__len__() != 4:
        print(line)
        print('the len of line is not 4')
    return customer_loyalty


xinshuju = []

for pa in shuju:
    line = []
    #获得会员价值分数
    score = dengJi(pa)
    #获得忠诚度 分数
    customer_loyalty = get_customer_loyalty(pa)
    uid = pa[0]
    #print(uid)
   # print(score)
   # print(customer_loyalty)
    line.append(uid)
    if float(score)>=float(2):

        line.append('高')
    elif  float(score) >= float(1) and float(score)<float(2):
        line.append('中')
    elif float(score) < float(1):
        line.append('低')
    line.append(customer_loyalty)
    print(line)
    xinshuju.append(line)


xinshuju = np.array(xinshuju)

print("dddd",xinshuju)

hebing =[[1,2,3]]
scoreY=[1, 2]
for line in hebing:
    if float(line[1])>=float(scoreY[0]):
        line[1]= '高'
    elif float(line[1])>= float(scoreY[1]):
        line[1]= '中'
    elif float(line[1])<float(scoreY[1]):
        line[1] = '低'
    #
    # if float(line[2])>=float(customer_loyaltyY[0]):
    #     line[2]= '高'
    # elif float(line[2])>= float(customer_loyaltyY[1]) and float(line[2])<float(customer_loyaltyY[0]):
    #     line[2]= '中'
    # elif float(line[2])<float(customer_loyaltyY[1]):
    #     line[2] = '低'