#coding:utf-8
import codecs,sys
#python 2 中一般才会用codecs
#创建gb2312 编码器
look = codecs.lookup("gb2312")
#创建utf-8 编码器
look2 = codecs.lookup("utf-8")

a = "我爱北京"
print(len(a),a,type(a))

#把a 编码为内部的 unicode ，但为什么方法名为decode呢，我的理解是把gb2312的字符串解码为unicode

b = look.decode(a)
#  返回的b[0]是数据，b[1]是长度，这个时候的类型是unicode了
print(b[1], b[0], type(b[0]))






