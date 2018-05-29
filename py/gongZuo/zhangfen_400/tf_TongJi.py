#conding:utf-8
import xlrd
import  jieba
import re

#停用词 列表
stopwordSet = set()
pathstop = 'C://Users//zhangheng//Desktop//张芬数据分析//stopwords.txt'
with open(pathstop,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        stopwordSet.add(line)



path = 'C://Users//zhangheng//Desktop//张芬数据分析//400//17年7月至2月11日诉求数据.xlsx'
pathR = "C://Users//zhangheng//Desktop//张芬数据分析//400//sanjifenlei.txt"
pathBase = "C://Users//zhangheng//Desktop//张芬数据分析//400//"
set = set()
data = xlrd.open_workbook(path)
table = data.sheets()[0]
nrows = table.nrows
print(nrows)
ncols = table.ncols
with open(pathR,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = str(line.strip())
        array = line.split(" ")
        if(len(array) == 2):
            leixing = array[0]
            set.add(leixing)

for leixing in set:
    #print(leixing)
    date_dict = {}
    for i in range(1, nrows):
        brand = str(table.row_values(i)[5]).strip().replace(" ","")
        print(brand)

        array = brand.split("-")
        if(len(array) == 3 ):
            x = array[2]
            if(x == leixing):
                print("jinlaile ")
                question = str(table.row_values(i)[44]).strip().replace(" ","")
                print('question:    ',question)
                question  = re.sub("[0-9\!\%\[\]\,\。.]", "", question)
                if len(question) > 1:
                    seg_list = list(jieba.cut(question,cut_all = False))
                    query = (','.join(seg_list)).replace(',',' ')
                    #print(type(query))
                    array = query.split(" ")
                    for x in iter(array):
                        if(len(x)>1 and x not  in stopwordSet):

                            if x not in date_dict:
                                date_dict[x] = 1
                            else:
                                date_dict[x] += 1



                print('date_dict:  ',len(date_dict))
                date = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)
                #以类型名  命名，
                leixingS = str(leixing).replace("/","")
                pathW = pathBase+str(leixingS)+".txt"
                print(pathW)
                w = open(pathW,'w',encoding='utf-8')

                for i in date:
                    newline = str(i[0])+" "+str(i[1])
                    w.write(newline)
                    w.write("\n")
                    w.flush()
                w.close()








