#coding:utf-8
path = 'D:\李响\key_word\shiyan\sim\知识库1.txt'
pathW = 'D:\李响\key_word\shiyan\sim\知识库NEW.txt'
w = open(pathW,'w',encoding='utf-8')
t = 0
t1 = 0
t2 = 0
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        t = t+1
        line = line.strip()
        if('http' in line):
            t1 = t1 +1
            linenew = "仅PC端"
            w.write(linenew)
            w.write('\n')
        elif('http' not in line):
            t2 = t2 +1
            linenew = "PC和APP通用"
            w.write(linenew)
            w.write('\n')

print(t,"   ",t1,"  ",t2)

