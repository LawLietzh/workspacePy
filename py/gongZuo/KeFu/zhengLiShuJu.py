#conding:utf-8
import  jieba
'''
智能客服中，判断语料的正负向，先去重，在分词，然后，类别标记

'''
#读取非 utf-8 编码，open('/Users/michael/gbk.txt', 'r', encoding='gbk')
#原文件
#path = 'E://数据资料//数据集合//情感词挖掘//ZhengXcontent.txt'
path = 'E://数据资料//数据集合//情感词挖掘//FuXcontent.txt'
#去重完的文件
#path1 = 'E://数据资料//数据集合//情感词挖掘//ZhengXcontent_quchong.txt'
path1 = 'E://数据资料//数据集合//情感词挖掘//FuXcontent_quchong.txt'
r = set()
w = open(path1,'w',encoding='utf-8')
t = 0
with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        t = t+1
        r.add(line)
print(t)
print(len(r))

for i in r:
    line = str(i).strip()
    line = line.strip()
    if len(line)>1:
        seg_list = list(jieba.cut(line,cut_all = True))
        query = (','.join(seg_list)).replace(',',' ')
        #print(query)
        w.write(query+" #负向")
        w.write('\n')

w.close()
'''
examples = list(open("ff.txt", "r",encoding='utf-8').readlines())
w = [s.strip() for s in examples]

#写文件
with open('xie.txt','w',encoding='utf-8') as f:
    f.write('Hello ,world!')
'''