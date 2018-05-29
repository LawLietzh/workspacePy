#coding:utf-8
from matplotlib import pyplot
'''
主要记录几个数据展示的例子 
'''

#绘制柱状图
def drawBar(grades):
    xticks = ['A', 'B', 'C', 'D', 'E']
    gradeGroup = {}
    for grade in grades:
        gradeGroup[grade] = gradeGroup.get(grade, 0) + 1
    #创建柱状图
    #第一个参数为柱的横坐标
    #第二个参数为柱的高度
    #参数align为柱的对齐方式，以第一个参数为参考标准
    pyplot.bar(range(5), [gradeGroup.get(xtick, 0) for xtick in xticks], align='center')
    #设置柱的文字说明
    #第一个参数为文字说明的横坐标
    #第二个参数为文字说明的内容
    pyplot.xticks(range(5), xticks)
    #设置横坐标的文字说明
    pyplot.xlabel('Grade')
    #设置纵坐标的文字说明
    pyplot.ylabel('Frequency')
    #设置标题
    pyplot.title('Grades Of Male Students')
    #绘图
    pyplot.show()

grades = ['A','A','A','B','B','C','C','C','D','D','D']
drawBar(grades)

#绘制扇形图
def drawPie(grades):
    labels = ['A', 'B', 'C', 'D', 'E']
    gradeGroup = {}
    for grade in grades:
        gradeGroup[grade] = gradeGroup.get(grade, 0) + 1
        #创建饼形图
        #第一个参数为扇形的面积
        #labels参数为扇形的说明文字
        #autopct参数为扇形占比的显示格式
    pyplot.pie([gradeGroup.get(label, 0) for label in labels], labels=labels, autopct='%1.1f%%')
    pyplot.title('Grades Of Male Students')
    pyplot.show()
#drawPie(grades)

#绘制直方图
def drawHist(heights):
    #创建直方图
    #第一个参数为待绘制的定量数据，不同于定性数据，这里并没有事先进行频数统计
    #第二个参数为划分的区间个数
    pyplot.hist(heights, 1000)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Frequency')
    pyplot.title('Heights Of Male Students')
    pyplot.show()

heights = [1,2,3,4,5,6,7,1,1,1,3,3,4,4,4,7,7]
drawHist(heights)



#绘制 累积曲线 （可以反映正太分布 情况）
#累积曲线对应数据的分布函数，由于身高变量是属于服从正态分布的，从绘制出来的累积曲线图上也可以直观地看出来：
def drawCumulativeHist(heights):
    #创建累积曲线
    #第一个参数为待绘制的定量数据
    #第二个参数为划分的区间个数
    #normed参数为是否无量纲化
    #histtype参数为'step'，绘制阶梯状的曲线
    #cumulative参数为是否累积
    pyplot.hist(heights, 20, normed=True, histtype='step', cumulative=True)
    pyplot.xlabel('Heights')
    pyplot.ylabel('Frequency')
    pyplot.title('Heights Of Male Students')
    pyplot.show()

#drawCumulativeHist(heights)
#for i in l:
#    print(i,"   ")
#drawHist(heights)

import scipy.stats as stats
#判断一推数据 是否符合正太分布， 返回值有两个（w ，p_value）如何p_value》0.05 则 基本符合
#print(stats.shapiro(l))

