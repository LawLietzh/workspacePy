#coding:utf-8
#path ='D://李响//key_word//live800quchong//kefu_20171205_QC_jiaSpan_Qulive800_Q_query_amswer.txt'
pathbuquan ='D://李响//key_word//live800quchong//zsk_quan.txt'


pathbuwriter ='D://李响//key_word//live800quchong//zsk_quan_xiugai.txt'
zai = open(pathbuwriter,'w',encoding='utf-8')
ss = set()

with open(pathbuquan,'r',encoding='utf-8') as f:
    for line in f.readlines():
        line = line.strip()
        linearr = line.split("\t")
        if(len(linearr) == 3):
            arr3 = linearr[2]
            if("第三方商家配送：自下单起72小时内发货（显示揽收信息），除预售商品、海外购商品、定制商品及大件家具商品按店铺公告或与店铺协商日期为准" in arr3):
                arr3 = arr3.replace("第三方商家配送：自下单起72小时内发货（显示揽收信息），除预售商品、海外购商品、定制商品及大件家具商品按店铺公告或与店铺协商日期为准","第三方商家配送：自下单起48小时内发货（显示揽收信息），除预售商品、海外购商品、定制商品及大件家具商品按店铺公告或与店铺协商日期为准")
                linex = linearr[0]+'\t'+linearr[1]+'\t'+arr3
                zai.write(linex)
                zai.write('\n')
            else:
                zai.write(line)
                zai.write('\n')

        elif(len(linearr) != 3):

            print(line)






print(ss.__len__())
