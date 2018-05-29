#coding:utf-8
path = 'D://李响//key_word//shiyan//wuliu_zhongjibanben_kuochong_QC.txt'
pathZong = 'D://李响//key_word//live800quchong//kefu_20171205_QC_jiaSpan_Qulive800_Q_query_amswer.txt'
pathQwuliu = 'D://李响//key_word//live800quchong//erfenlei.txt'
#pathSim_qu = 'D://李响//key_word//shiyan//query_sim3_quwuliu.txt'
w = open(pathQwuliu,'w',encoding='utf-8')

#te = open(path,'w',encoding='utf-8')

L = set()

#读取wuliuCUN
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        L.add(line)
print(len(L))

with open(pathZong,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(line not in L):
            w.write(line)
            w.write('\n')
