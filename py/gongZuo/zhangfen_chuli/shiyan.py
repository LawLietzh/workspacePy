#coding:utf-8
import jieba
str = "17759919055顾客来电， 2013-04-13 购买的 阿里斯顿热水器AM50SH3.0M5，需要维修， 请分部核实后回复：17759919055"
seg_list = list(jieba.cut(str,cut_all = False))
query = (','.join(seg_list)).replace(',',' ')
print(query)
jieba.load_userdict("userwords.txt")

seg_list = list(jieba.cut(str.replace(" ",""),cut_all = False))
query = (','.join(seg_list)).replace(',',' ')
query = query.split(" ")
for i in query:
    print(i)
print(query)

list = ["1","2","3","4","5"]
for i in list:
    print(i)


