#coding:utf-8

path_zl ='D://李响//key_word//shiyan//sim//sim_xianguanX.txt'
path_qu ='D://李响//key_word//shiyan//sim//sim_xianguan_qu.txt'
pathw = open(path_qu,'w',encoding='utf-8')
ss = set()
with open(path_zl,'r',encoding='utf-8') as f:
    for line in f.readlines():
        lineArray = line.split("	")
        if(lineArray[0] not in ss):
            ss.add(lineArray[0])
            pathw.write(lineArray[0])
            pathw.write('\n')

print(ss.__len__())












