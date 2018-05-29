#coding:utf-8
'''

这个类，主要用来去掉那些，问题相同，但是答案不同的问题，

'''
path = 'D://李响//key_word//live800quchong//kefu_20171205_QC_jiaSpan_Qulive800.txt'
pathwriter = 'D://李响//key_word//live800quchong//kefu_20171205_QC_jiaSpan_Qulive800_Q_query_amswer.txt'
pathwriter_query_amswer = 'D://李响//key_word//live800quchong//query_amswer.txt'

w_pathwriter = open(pathwriter,'w',encoding='utf-8')
w_pathwriter_query_amswer = open(pathwriter_query_amswer,'w',encoding='utf-8')

set_query = set()
set_query_C = set()
set_answer = set()
setline = set()

with open(path,"r",encoding='utf-8') as f:
    for line in f.readlines():
        lineArray = line.strip().split("\t")
        classify = lineArray[0]
        question = lineArray[1]
        if(question not in set_query):
            set_query.add(question)
            setline.add(line)
        elif(question in set_query):
            set_query_C.add(question)
            set_answer.add(line)

print(len(setline))
print(len(set_answer))
t = 0
for line in setline:
    lineArray = line.strip().split("\t")
    question = lineArray[1]
    if question in set_query_C:
        print(question)
        set_answer.add(line)
    elif question not in set_query_C:
        t = t+1
        w_pathwriter.write(line)
w_pathwriter.flush()
w_pathwriter.close()

sorted(set_answer)
for line in set_answer:
    w_pathwriter_query_amswer.write(line)

w_pathwriter_query_amswer.flush()
w_pathwriter_query_amswer.close()

print(t)




























