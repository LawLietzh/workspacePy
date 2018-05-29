#coding：utf-8
import numpy
pathZ = 'D://李响//key_word//shiyan//model//fast//zhengli_lable.txt'
pathF = 'D://李响//key_word//shiyan//model//fast//fuli_lable.txt'
pathTrain  = 'D://李响//key_word//shiyan//model//fast//train.txt'
pathTest  = 'D://李响//key_word//shiyan//model//fast//test.txt'
wTrain = open(pathTrain,'w',encoding='utf-8')
wTest = open(pathTest,'w',encoding='utf-8')
#读取wuliuCUN

lz = list()
lf = list()
with open(pathF,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        lf.append(line)

with open(pathZ,"r",encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        lz.append(line)

numpy.random.shuffle(lz)
numpy.random.shuffle(lf)

print(len(lz))
print(len(lf))
tz = int(len(lz)*0.8)

tf = int(len(lf)*0.1)
tf1 = int(len(lf)*0.12)
print('*********')
print(tz)
print(tf)
print(tf1)
ltrain = list()
for i in range(7):
    ltrain.extend(lz[0:tz])
ltrain.extend(lf[0:tf])
ltest = list()
#ltest.extend(lz[tz:])
ltest.extend(lz)
ltest.extend(lf[tf:tf1])
numpy.random.shuffle(ltrain)
numpy.random.shuffle(ltest)

for line in ltrain:
    wTrain.write(line)
    wTrain.write('\n')

for line in ltest:
    wTest.write(line)
    wTest.write('\n')
