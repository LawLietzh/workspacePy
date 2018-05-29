import xlrd
import xlwt
'''
path = 'E://数据资料//数据分析//诉求工单（4月-11月）.xlsx'
data = xlrd.open_workbook(path)
table = data.sheets()[0]
nrows = table.nrows
ncols = table.ncols
date_dict = {}
for i in range(1, nrows):
    date = table.row_values(i)[5].strip().split("-")[0]
    if u"门店客诉" in date:
        brand = table.row_values(i)[57]

        if brand not in date_dict:
            date_dict[brand] = 1
        else:
            date_dict[brand] += 1
'''
class kesu:
    def __init__(self):
        pass

    #门店客诉集中类型
    def mendiankesuJIZHONLEIXING(self):
        print('E://数据资料//数据分析//诉求工单（4月-11月）.xlsx')
        path = 'E://数据资料//数据分析//诉求工单（4月-11月）.xlsx'
        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        date_dict = {}
        for i in range(1, nrows):
            #brand = table.row_values(i)[5].strip().split("-")[2]
            brand = table.row_values(i)[54]
            #if u"门店客诉" in date:
             #   brand = table.row_values(i)[5].strip().split("-")[2]

            if brand not in date_dict:
                date_dict[brand] = 1
            else:
                date_dict[brand] += 1

        date_dict = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)

        for time in date_dict:
            print(time[0])
        for time in date_dict:
            print(time[1])
    #门店客诉集中品类
    def mendiankesuJIZHONPINLEI(self):

        path = 'E://数据资料//数据分析//诉求工单（4月-11月）.xlsx'
        data = xlrd.open_workbook(path)
        table = data.sheets()[0]
        nrows = table.nrows
        ncols = table.ncols
        date_dict = {}
        for i in range(1, nrows):
            date = table.row_values(i)[5].strip().split("-")[-1].encode('utf-8')
            print(date)
            if u"送货不及时" in date:
                brand = table.row_values(i)[15].strip()
                print(brand)
                if brand not in date_dict:
                    date_dict[brand] = 1
                else:
                    date_dict[brand] += 1

        date_dict = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)

        for time in date_dict:
            print(time[0])
        for time in date_dict:
            print(time[1])
#门店客诉集中类型
if __name__ == "__main__":

    path = 'E://数据资料//数据分析//诉求工单（4月-11月）.xlsx'
    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    date_dict = {}
    for i in range(1, nrows):
        date = table.row_values(i)[5].strip().split("-")[-1]

        if u"送货不及时" in date:
            brand = table.row_values(i)[17].strip()

            if brand not in date_dict:
                date_dict[brand] = 1
            else:
                date_dict[brand] += 1
    date_dict = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)

    for time in date_dict:
        print(time[0])
    print("**************")
    for time in date_dict:
        print(time[1])























    '''
    #kesu().mendiankesuJIZHONPINLEI()
    path = 'E://数据资料//数据分析//来话小结（4月-11.26）.xlsx'
    L = ['安装','屏碎','维修','换货','订单','发票','送货','退货']

    data = xlrd.open_workbook(path)
    table = data.sheets()[0]
    nrows = table.nrows
    ncols = table.ncols
    date_dict = {}
    t = 0
    for i in range(1, nrows):
        date = str(table.row_values(i)[11]).strip()
        for key in L:
            if key in date:
                date = key
                break
        if(date=='1.0'):
            date= '1'
        date = date.replace('\n','').replace('\r\n','').replace('\r','').replace('	','').replace('\t','')
        t = t+1
        if date not in date_dict:
            date_dict[date] = 1
        else:
            date_dict[date] += 1

    date_dict = sorted(date_dict.items(),key=lambda item:item[1],reverse=True)

    #for time in date_dict:
        #if(time[1]>5):
         # print(time[0])
    for time in date_dict:
        if (time[1]>5):
            print ("%.2f%%" % (time[1] / float(t) * 100))
        #print(time[1])
        #print('%.4f%%' % float(time[1]/t)*100)
        #print ("%.2f%%" % (time[1] / float(t) * 100))
    for time in date_dict:
        if (time[1]>5):
            print(time[1])
'''

