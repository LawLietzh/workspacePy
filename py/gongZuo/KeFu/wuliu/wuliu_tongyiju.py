#coding:utf-8
'''
根据 人工抽取的  询问订单的query， 和之前扩充的 同义句，来找出 订单query  同义句

'''
path = 'D://李响//key_word//shiyan//二分类//wuliu_SQ_QC.txt'
pathSim = 'D://李响//key_word//shiyan//query_sim3.txt'
pathQC = 'D://李响//key_word//shiyan//二分类//wuliuSQ_QC_kuochong.txt'
#pathSim_qu = 'D://李响//key_word//shiyan//query_sim3_quwuliu.txt'
w = open(pathQC,'w',encoding='utf-8')
#w_quwuliu = open(pathSim_qu,'w',encoding='utf-8')
#te = open(path,'w',encoding='utf-8')

L = set()

#读取wuliuCUN
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        L.add(line)
print(len(L))


L1 = set()

#读取sim 列表
with open(pathSim,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        L1.add(line)

print(len(L1))



set = set()
for line in L:
    for lineSim in L1:
        lineArray = lineSim.strip().split("\t")
        lineSim1 = lineArray[1]
        if(lineSim1 == line):
            set.add(lineArray[0])
            w.write(lineArray[0])
            w.write('\n')
print(len(set))

w.close()




















