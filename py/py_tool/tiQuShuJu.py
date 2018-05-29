#cond:utf-8
#这个方法用于，提取 1000万数据，去掉后面的词频，并进行分词，然后存储

import  jieba
pathD = 'C://Users/zhangheng/Desktop/预料标注/question16.txt'
pathX = 'C://Users/zhangheng/Desktop/预料标注/question16TiQu.txt'
r = []
d = open(pathX,'w',encoding='utf-8')
with open(pathD, "r", encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip().split('\t')[0]
        print(line)
        seg_list = list(jieba.cut(line,cut_all = True))
        line = (','.join(seg_list)).replace(',',' ')
        d.write(line)
        d.write('\n')

d.close()
