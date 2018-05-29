#coding:utf-8
path = 'E://数据资料//数据分析//智能客服语料整理//es20171204.txt'
#path1 = 'D://李响//key_word//shiyan//二分类//wuliu_zhongjibanben.txt'
pathzhengli = 'E://数据资料//数据分析//智能客服语料整理//es_text.txt'
w_quwuliu = open(pathzhengli,'w',encoding='utf-8')
quchong = set()
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip().replace("{","").replace("}","")
        lineArray  = line.split(",")
        for arr in lineArray:
            arrass = arr.split()








        if(line not in quchong):
            quchong.add(line)
            w_quwuliu.write(line)
            w_quwuliu.write('\n')


'''
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        if(line not in quchong):
            w_quwuliu.write(line)
            w_quwuliu.write('\n')
            '''
w_quwuliu.close()