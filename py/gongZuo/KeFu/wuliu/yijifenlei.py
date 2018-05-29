#coding:utf-8
path = 'C://Users//zhangheng//Desktop//一级分类.txt'
path1 = 'C://Users//zhangheng//Desktop//一级分类_quchong.txt'


w =  open(path1,'w',encoding='utf-8')
set = set()
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        if(line not in set):
            set.add(line)
            w.write(line)


