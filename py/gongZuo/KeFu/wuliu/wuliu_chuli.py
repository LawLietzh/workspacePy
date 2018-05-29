#coding:utf-8
'''
最后一次处理 物流问题 
'''
path = 'D://李响//key_word//shiyan//二分类//wuliu_zhongjibanben.txt'
pathSQ = 'D://李响//key_word//shiyan//二分类//wuliu_SQ.txt'
pathQC = 'D://李响//key_word//shiyan//二分类//wuliu_SQ_QC.txt'

wuliu_SQ_QC = open(pathQC,'w',encoding='utf-8')
quchong = set()
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(line not in quchong):
            quchong.add(line)


quchong_SQ = set()
with open(pathSQ,"r",encoding='utf-8') as f:
    for line1 in f.readlines():
        line1 = line1.strip()
        if(line1 not in quchong_SQ):
            quchong_SQ.add(line1)
            wuliu_SQ_QC.write(line1)
            wuliu_SQ_QC.write('\n')

'''
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(line not in quchong):
            w_quwuliu.write(line)
            w_quwuliu.write('\n')
            '''
#w_quwuliu.close()

print(len(quchong))
print(len(quchong_SQ))
for ss in quchong:
    if ss in quchong_SQ:
        print(ss)






