#coding:utf-8
from pyspark import SparkConf

'''
会员流失模型 
打算采用，LR 和 SVM 来看看效果

今天 重新看看 ，这两个模型

'''
import os
import  numpy as np
#读取数据
path = 'E://数据资料//数据集合//test//'
pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)

#先整理数据 给每一个数据加上 label标签
train = []
lab = []
t0 = 0
t1 = 0
for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        line = line.strip()
        str = line.split('\t')
        arr = []

        arr.append(float(str[1].strip()))
        arr.append(float(str[2].strip()))
        #arr.append(float(str[3].strip()))
        train.append(arr)
        #流失的用 0 代表，没有流失的用1
        if float(str[3].strip())>=200 :
            lab.append(0)
            t0= t0 +1
        elif float(str[3].strip())<200:
            lab.append(1)
            t1= t1 +1

print("看看lab 下有多少 0  和  1  ")
print("000000:   ",t0,"         111111111111111:    ",t1)


train = np.array(train)
quanbu = np.array(train)
lab  = np.array(lab)
labq  = np.array(lab)
if len(train)!= len(lab):
    print("长度不相同，什么鬼：")
#np.random.seed(22)
#shuffle_indices = np.random.permutation(np.arange(len(train)))

#train = train[shuffle_indices]
#lab  = lab[shuffle_indices]
print("kan kan shu ju :")
print(train[0:3])
print(lab[0:3])

leng = int(len(train)*0.7)

print(leng)
#模型
#取样本的30%作为测试
X_train = train[:leng]
X_test = train[leng:]
y_train = lab[:leng]
y_test = lab[leng:]
#为了追求机器学习和最优化算法的最佳性能，我们将特征缩放
from sklearn.preprocessing import StandardScaler

sc = StandardScaler()
#估算每个特征的平均值和标准差
sc.fit(X_train)
#查看特征的平均值
print(sc.mean_)
#查看特征的标准差
print(sc.scale_)
#注意：这里我们要用同样的参数来标准化测试集，使得测试集和训练集之间有可比性
X_train_std = sc.transform(X_train)
X_test_std = sc.transform(X_test)




#调用 逻辑回归模型
from sklearn.linear_model import LogisticRegression
lr = LogisticRegression(C=1000.0, random_state=0)
lr.fit(X_train_std, y_train)
print('lkkkkkk')
# 查看第一个测试样本属于各个类别的概率
print((X_test_std[5,:]))
print(   (X_test_std[5,:]).reshape((1,-1))   )
t = lr.predict_proba((X_test_std[0,:]).reshape((1,-1)))
print(t)


#计算模型在测试集上的准确性，
#  测试，      测试集样本，测试集标签
t = lr.score(X_train_std,y_train,sample_weight=None)
print(t)

#print(t)
#统计结果
from sklearn.metrics import f1_score, classification_report
y_pred = lr.predict(X_train_std)
print(classification_report(y_train, y_pred))


#t = lr.predict_proba(    (X_test_std[5,:]).reshape((1,-1))      )
#print(t)




'''
科学计数发 e ，转化为 float类型的数据
y='{:.5f}'.format(x) # 5f表示保留5位小数点的float型
'''
'''
t = t[0]
print(t)
#存储 格式化的数据
x= []
for i in t:
    j = '{:.5f}'.format(i)
    x.append(j)
    print(j)

'''