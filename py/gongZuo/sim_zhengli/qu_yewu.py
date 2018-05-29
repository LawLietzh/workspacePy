#coding:utf-8

path_zl ='D://李响//key_word//live800quchong//kefu_20171205_QC_jiaSpan_Qulive800_Q_query_amswer.txt'
path_xianguan ='D://李响//key_word//shiyan//sim//SQ.txt'

buzai ='D://李响//key_word//shiyan//buzai1.txt'
zai ='D://李响//key_word//shiyan//zai1.txt'
pathw = open(buzai,'w',encoding='utf-8')
zai = open(zai,'w',encoding='utf-8')
ss = set()
with open(path_zl,'r',encoding='utf-8') as f:
    for line in f.readlines():
        lineArray = line.strip().split("	")
        if(lineArray[1] not in ss):
            ss.add(lineArray[1])


print(ss.__len__())

with open(path_xianguan,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(line not in ss):
            pathw.write(line)
            pathw.write('\n')
        elif(line in ss):
            zai.write(line)
            zai.write('\n')










