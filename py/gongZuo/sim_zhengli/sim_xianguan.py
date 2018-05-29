#coding:utf-8
path = 'D://李响//key_word//shiyan//sim//sim_xianguan_xiugai.txt'
path_zl ='D://李响//key_word//shiyan//sim//sim_xianguan_zl.txt'

sim_zl = open(path_zl,'w',encoding='utf-8')
with open(path,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(len(line) != 0):
            line = line.replace("                           ","	")
            sim_zl.write(line)
            sim_zl.write('\n')







