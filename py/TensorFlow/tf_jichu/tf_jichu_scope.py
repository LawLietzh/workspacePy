#coding:utf-8
'''
练习 名称作用域  name scope  
本质上，名称作用域 允许 将 op 划分到一些较大的，有名称的语句块中，
当以

'''
import tensorflow as tf
with tf.name_scope("A") as scope:
    a = tf.add(1,2,name="A_add")

with tf.name_scope("B") as scope:
    b = tf.multiply(1,2,name="B_mul")
e = tf.add(a,b,name="output")

with tf.Session() as sess:
    t1 = sess.run(a)
    t2  = sess.run(b)
    t3 = sess.run(e)
    print(t1)
    print(t2)
    print(t3)


















