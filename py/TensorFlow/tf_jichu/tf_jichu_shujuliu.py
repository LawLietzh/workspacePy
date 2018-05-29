#coding:utf-8
import tensorflow as tf
a = tf.constant(5,name='a')
b = tf.constant(3,name='b')
c = tf.multiply(a,b,name='mul_c')#相乘
d = tf.add(a,b,name='add_d')
e = tf.add(c,d,name='add_e')

sess = tf.Session()
#sess.run(e)
print(sess.run(e))

