##coding:utf-8
#读文件：
r = []
#读取非 utf-8 编码，open('/Users/michael/gbk.txt', 'r', encoding='gbk')
with open('ff.txt',"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        r.append(line)
print(r[0:4])

examples = list(open("ff.txt", "r",encoding='utf-8').readlines())
w = [s.strip() for s in examples]

#写文件
with open('xie.txt','w',encoding='utf-8') as f:
    f.write('Hello ,world!')

