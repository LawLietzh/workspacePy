#coding:utf-8
'''
测试，svd 的应用 
'''


from numpy import  *
from numpy import  linalg as la
u,sigma ,v = linalg.svd([[1,1],[7,7]])
print(u)
print(sigma)
print(v)

myMat = [[1,1,1,0,0],
         [2,2,2,0,0],
         [1,1,1,0,0],
         [5,5,5,0,0],
         [1,1,0,2,2],
         [0,0,0,3,3],
         [0,0,0,1,1]
       ]
u,sigma ,v = linalg.svd(mat(myMat))
print("llllllll")
print(u)
print(u[:,:3])

#加载测试数据集
def loadExData():
    return mat([[],
                 [],
                [],
                [],
                [],])



#相似度函数
def eulidSim(inA ,inB):
    return 1.0/(1.0 + la.norm(inA - inB))
#
def pearsSim(inA ,inB):
    if len(inA)<3 : return  1.0

    return 0.5 + 0.5*corrcoef(inA,inB,rowvar=0)[0][1]
#余弦相似度
def cosSim(inA ,inB):
    num = float(inA.T*inB)
    demo = la.norm(inA)*la.norm(inB)
    return  0.5+ 0.5*(num/demo)

print("kankan  相似度 ")
#计算相似度
myMat = mat(myMat)
print(type(myMat))
print(myMat[:,0])
t1 = eulidSim(myMat[:,0],myMat[:,4])
print(t1)

t1 = eulidSim(myMat[:,0],myMat[:,0])
print(t1)


t1 = cosSim(myMat[:,0],myMat[:,4])
print(t1)

k = mat(eye(3)*[1,2,3])
print(k)

#求 前k个奇异值的平方和占总奇异值的平方和百分比，来确定k的值
def sigmaPct(sigma,percentage):
    sigma2 = sigma**2
    sumsgm2 = sum(sigma2)
    sumsgm3 = 0
    k = 0
    for i in sigma:
        sumsgm3 += i**2
        k +=1
        if sumsgm3 >= sumsgm2*percentage:
            return  k
#函数svdest（）de 参数包括，数据矩阵，用户编号，物品的奇异值占比，行对应的用户，列对应的物品，还有相似度计算的方法
'''
.T －－ 返回自身的转置
.H －－ 返回自身的共轭转置
.I －－ 返回自身的逆矩阵
.A －－ 返回自身数据的2维数组的一个视图（没有做任何的拷贝） 对于矩阵mat而言，.A是把它转化为array 数组类型
'''
def svdEst(dataMat,user,simMeas,item,percentage):
    n = shape(dataMat)[1]
    simTotal = 0.0
    ratSimTotal = 0.0
    u,sigma,vt = la.svd(dataMat)
    k = sigmaPct(sigma,percentage)
    #取选出来的前k个特征值，构建对角矩阵
    sigmaK = mat(eye(k)*sigma[:k])
    #u[:,:k] 每一行的 前 k 列
    #sigmaK.I 矩阵的逆
    # #根据k的值将原始数据转换到k维空间(低维),xformedItems表示物品(item)在k维空间转换后的值
    xformedItems = dataMat.T*u[:,:k]*sigmaK.I
    for j in range(n):
        userRating = dataMat[user,j]
        if userRating==0 or j == item:continue
        #计算物品item 与物品j 之间的相似度
        similarity = simMeas(xformedItems[item,:].T,xformedItems[j,:].T)
        #对所有相似度求和  （求相似度总和）
        simTotal += similarity
        #用 物品 item 和物品j 的相似度 乘以用户对物品 j 的评分 并求和
        ratSimTotal += similarity * userRating

    if simTotal == 0 : return  0
    else:return  ratSimTotal/simTotal  #得到物品item 的预测评分

#产生预测评分最高的N 个推荐结果，默认返回5 个
#参数包括：数据矩阵，用户编号，相似度衡量的方法，预测评分分方法，以及奇异值占比的阈值
#数据矩阵的行 对应用户，列对应物品，函数的作用是 基于item 的相似性对 用户未评分的物品进行预测评分
def recommend(dataMat,user,N=5,simMeas = cosSim,estMethod=svdEst,percentage=0.9):
    #建立一个用户未评分item 的列表
    unratedItems = nonzero(dataMat[user,:].A == 0)[1]
    print("unratedItemsunratedItems")
    print(dataMat[user,:].A)
    print(unratedItems)
    #如果都已经评论过分，则退出
    if len(unratedItems) == 0:return  'you rated everything'
    itemScores=[]
    #对于每个未评分的item，都计算其预测评分
    for item in unratedItems:
        estimatedScore = estMethod(dataMat,user,simMeas,item,percentage)
        itemScores.append(  (item,estimatedScore)  )
    #按照item的得分进行从大到小排序
    itemScores = sorted(itemScores,key=lambda  x:x[1],reverse= True)
    #返回前N 大评分值得 item名，及其预测评分值
    print("返回前N 大评分值得 item名，及其预测评分值")
    return itemScores[:N]

if __name__ == "__main__":
    testdata = myMat
    t = recommend(testdata,1,N = 3,percentage=0.8)
    print(t)
















