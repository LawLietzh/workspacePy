#coding:utf-8
path = 'D://李响//key_word//shiyan//wuliu_zhongjibanben_kuochong.txt'
#path1 = 'D://李响//key_word//shiyan//二分类//wuliu_zhongjibanben.txt'
pathquchong = 'D://李响//key_word//shiyan//wuliu_zhongjibanben_kuochong_QC.txt'
w_quwuliu = open(pathquchong,'w',encoding='utf-8')
quchong = set()
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(line not in quchong):
            quchong.add(line)
            w_quwuliu.write(line)
            w_quwuliu.write('\n')

print(len(quchong))
'''
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(line not in quchong):
            w_quwuliu.write(line)
            w_quwuliu.write('\n')
            '''
w_quwuliu.close()
