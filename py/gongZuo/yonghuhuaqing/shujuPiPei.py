#coding:utf-8
'''
会员等级模型
用户忠诚度模型
二者融合

'''
#读取数据
pathDengji = 'E://数据资料//数据集合//uidRank.txt'
pathZhongcheng = 'E://数据资料//数据集合//uidRank.txt'

#读取会员等级
dengji = {}
with open(pathDengji,'r',encoding='utf-8') as f:
    for line in f.readlines():
        strArray = line.strip().split('\t')
        dengji[strArray[0]] = st[1]

print(dengji.__len__())

#读取 用户忠诚度
zhongchengdu = {}
with open(pathZhongcheng,'r',encoding='utf-8') as f:
    for line in f.readlines():
        strArray = line.strip().split('\t')
        zhongchengdu[strArray[0]] = strArray[1]
print(zhongchengdu.__len__())
