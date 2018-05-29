#coding:utf-8
'''
 查看 问句中有多少 带时候的 问题 

'''

path = 'D://李响//key_word//live800quchong//timeGUI.txt'

path1 = 'D://李响//key_word//live800quchong//timeGUIWen.txt'

w = open(path1,'w',encoding='utf-8')

with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if('时候' in line and  '到'  in line and  '今天'  not in line and  '现在'  not in line and  '发货'  not in line) :
            w.write(line)
            w.write('\n')



w.close()
'''
examples = list(open("ff.txt", "r",encoding='utf-8').readlines())
w = [s.strip() for s in examples]

#写文件
with open('xie.txt','w',encoding='utf-8') as f:
    f.write('Hello ,world!')
'''



