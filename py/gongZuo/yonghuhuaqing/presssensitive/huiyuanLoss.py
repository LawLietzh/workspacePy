#coding:utf-8


'''
会员流失模型 
打算采用，LR 和 SVM 来看看效果

今天 重新看看 ，这两个模型

'''
import os
import  numpy as np
#用joblib 进行模型的持久化的操作
from sklearn.externals import  joblib




#读取数据
path = 'E://数据资料//数据集合//loss//test//'
pathDir = os.listdir(path)
pathdir = []
for allDir in pathDir:
    #  '%s%s' %  的作用就是 是的拼接的时候
    child = os.path.join('%s%s' % (path,allDir))
    print(child)
    pathdir.append(child)

#先整理数据 给每一个数据加上 label标签
train  =  []
uid =   []
lab =   []
for pa in pathdir:
    f = open(pa,'r',encoding='utf-8')
    for line in f.readlines():
        line = line.strip()
        str = line.split('')
        #print('wo kan kan  leixing :',type(str))

        if str.__len__()==9:
            train.append(str)
        else:
            print("列表数据 有 错误数据")
            print(pa,"      ",line)

'''
#uid                       string,   用户uid  0 
#kdj                       string,   客单价  1
#last_tre_num              string,   最近三个月购买次数 2
#last_first_buy_interval   string,   最后一次购买距离第一次购买天数 3
#last_buy_damount          string,   最后一次购买金额 4
#last_buy_num              string,    最后一次购买数量 5 
#last_buy_interval         string,     最后一次购买距今天数 6 
#last_buy_ishuan           string,     最后一次购买是否换货 7
#last_buy_istui            string      最后一次购买是否退货  8

'''
train = np.array(train)
print("train")
print(train.shape)
train = np.array(train)
#现在已经拿到了数据矩阵，现在开始处理，获得 uid，lab  和样本数据

#获得uid   就是train 矩阵的第0 列
uid = (train[:,0]).reshape(-1,1)
#获得 lab
lab = (train[:,6])
#lab 处理 获得 真实的lab
#流失的标签 为1 ，没有流失的为 0 ,用200天作为阈值来判断是否流失
for i in range(len(lab)):
    if lab[i]>=200:
        lab[i] = 1
    elif lab[i] < 200:
        lab[i] = 0
print(lab[0:10])


#((basedata_tmp.T)[1:3]).T
#获得第一列 到第 5例
yangben1 = ((train.T)[1:6]).T
#获得第7 列到 第8 列
yangben2 = ((train.T)[7:9]).T
yangben = np.hstack((yangben1,yangben2))


#np.random.seed(22)
#shuffle_indices = np.random.permutation(np.arange(len(train)))

#train = train[shuffle_indices]
#lab  = lab[shuffle_indices]


leng = int(len(train)*0.7)

print (leng)
#模型
#取样本的30%作为测试
X_train = yangben[:leng]
X_test = yangben[leng:]
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
#保存模型
joblib.dump(lr,"./model/hyloss_model.m")
# 加载模型
lr = joblib.load("./model/hyloss_model.m")
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