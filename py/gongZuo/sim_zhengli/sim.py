#coding:utf-8
pathsim = 'D://李响//key_word//shiyan//sim//query_sim3.txt'
pathsim_qu = 'D://李响//key_word//shiyan//sim//sim_qu.txt'
pathsim_xiangguan = 'D://李响//key_word//shiyan//sim//sim_xianguan.txt'
pathSH = 'D://李响//key_word//shiyan//sim//SH.txt'
pathSQ = 'D://李响//key_word//shiyan//sim//SQ.txt'


sim_qu = open(pathsim_qu,'w',encoding='utf-8')
sim_xiangguan = open(pathsim_xiangguan,'w',encoding='utf-8')

xg = set()
#读取 SQ  SH
with open(pathSH,'r',encoding='utf-8') as f:
    for line in f.readlines():
        xg.add(line.strip())

with open(pathSQ,'r',encoding='utf-8') as f:
    for line in f.readlines():
        xg.add(line.strip())

muju = set()
#找到 xg   查找 原始语句
muju1 = set()
with open(pathsim,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        lineArray = line.split("	")
        if(lineArray[0] in xg):
            muju.add(lineArray[1])
        elif(lineArray[0] not in xg):
            muju1.add(line)

print(xg.__len__())
print(muju.__len__())
print(muju1.__len__())

t = 0
sorted(muju)
lie = set()
with open(pathsim,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        lineArray = line.split("	")
        if(lineArray[1] in muju):
            t = t +1
            lie.add(lineArray[0]+"                           "+lineArray[1])
            sim_xiangguan.write(lineArray[0]+"                           "+lineArray[1])
            sim_xiangguan.write('\n\r')


print(t)



