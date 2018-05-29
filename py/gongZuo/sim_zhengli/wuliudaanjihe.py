#coding:utf-8
path_zl ='D://李响//key_word//shiyan//sim//物流答案集合.txt'


zai ='D://李响//key_word//shiyan//物流答案集合_qs.txt'

zai = open(zai,'w',encoding='utf-8')
ss = set()

with open(path_zl,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if('#' not in line):

            if(line not in ss):
                ss.add(line)
                zai.write(line)
                zai.write('\n')

print(ss.__len__())
