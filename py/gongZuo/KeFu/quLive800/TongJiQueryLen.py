#coding:utf-8
path = 'D://李响//key_word//live800quchong//zsk_quan_xiugai.txt'



le = 0
stt = ""
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        lineArray = line.strip().split("\t")
        classify = str(lineArray[1])
        classify = classify.replace(" ","")
        ss = len(classify)
        if(ss == 43):
            stt = classify

        if(ss>=le):
            le = ss
        print(classify,ss)

print(le)
print(stt)











