#coding:utf-8
path = 'D://李响//key_word//shiyan//wentiduiying1016_seg.txt'
pathQC = 'D://李响//key_word//shiyan//wuliu.txt'
w = open(pathQC,'w',encoding='utf-8')
#te = open(path,'w',encoding='utf-8')

se = set()
t = 0
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        line = line.split("\t")[1].strip()
        t = t+1
        if(line in se):
            continue;
        elif(      line not in se ):
            se.add(line)
            w.write(line)
            w.write("\n")


print(t)
print(len(se))
w.close()





