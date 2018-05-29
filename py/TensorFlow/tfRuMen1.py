#coding:utf-8
'''
用来熟悉 tensorflow 的基本知识 
使用图 graph 来表示计算
在会话中执行图 session
使用张量 tensor 来代表数据
使用变量 variable
使用feeds 和 取回 fetches 将数据传入 或传出任何操作


 使用图（graphs）来表示计算任务
 在被称之为会话（Session）的上下文（context）中执行图
 使用tensor表示数据
 通过变量（Variable）维护状态
 使用feed和fetch可以为任意的操作赋值或者从其中获取数据
Tensorflow是一个编程系统，使用图（graphs）来表示计算任务，图（graphs）中的节点称之为op
（operation），一个op获得0个或多个Tensor，执行计算，产生0个或多个Tensor。Tensor 看作是
一个 n 维的数组或列表。图必须在会话（Session）里被启动

'''

import tensorflow as tf
#构建图  又变量的话，需要激活
matrix1 = tf.constant([[3.0,3.0]])

matrix2 = tf.constant([[2.0,2.0]])

x = tf.Variable([1.0,2.0])
jihou = tf.global_variables_initializer()

product = tf.add(matrix1 , matrix2)
product1 = tf.add(x,matrix1)
#执行
with tf.Session() as sess:
    sess.run(jihou)
    result = sess.run(product)
    result1 = sess.run(product1)
    print(result)
    print(result1)













