#coding：utf-8


path = 'D://李响//key_word//shiyan//model//fast//fuli.txt'
pathW = 'D://李响//key_word//shiyan//model//fast//fuli_lable.txt'

w = open(pathW,'w',encoding='utf-8')





#读取wuliuCUN
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        w.write(line+" "+'#'+u'负')
        w.write('\n')




