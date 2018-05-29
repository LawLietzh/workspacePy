#coding:utf-8
'''
统计舆情权重，参看 设的阈值，下，有多少满足需求的样本
'''

path = "E:/数据资料/save2.txt"
pathW = "E:/数据资料/save2X.txt"
w = open(pathW,"w",encoding='UTF-8')



with open(path,"r",encoding='GBK') as f:
    for line in f.readlines():
        strArray = line.strip().split('\t')
        #print(strArray[5])
        core = ""
        if strArray[5] == "负面" :
            core = "\t"+"0"+"\t"+"0.4,0.6"
        elif strArray[5] == "中性" :
            core = "\t"+"1"+"\t"+"0.55,0.45"
        elif strArray[5] == "正面" :
            core = "\t"+"1"+"\t"+"0.6,0.4"
        line = line.strip() + core
        print(line)
        w.write(line)
        w.write("\n")
        w.flush()

w.close()



















