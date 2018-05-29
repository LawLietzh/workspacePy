#coding:utf-8
path = 'D://李响//key_word//shiyan//wuliu.txt'
pathQC = 'D://李响//key_word//shiyan//wuliuCUN.txt'
w = open(pathQC,'w',encoding='utf-8')
#te = open(path,'w',encoding='utf-8')

se = set()
t = 0
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        t = t+1
        if(line in se):
            continue;
        elif(  "物流" in line  and   line not in se ):
            se.add(line)
            w.write(line)
            w.write("\n")


print(t)
print(len(se))
w.close()





