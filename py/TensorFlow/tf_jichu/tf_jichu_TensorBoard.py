#coding:utf-8
import  tensorflow as tf
a = tf.constant([5,3,2],name='a')
b = tf.reduce_prod(a,name='b')#这个函数的作用是计算指定维度的元素相乘的总和。
c = tf.reduce_sum(a,name='mul_c')#相乘
d = tf.add(a,b,name='add_d')
e = tf.add(c,d,name='add_e')

import  numpy as np
t0 = np.array(50,dtype=np.int32)

t1 = np.array([b"APP",b"peach",b"grap"])
random = tf.Variable(tf.truncated_normal([2,2],stddev=1.0))
#如果 要求Graph 对象中的一些Variable 对象只可手工修改，而不允许使用Optimizer  可使用 trainable = False    not_trainable = tf.Variable(0,trainable = False)
random1 = tf.Variable(5)
#assign 对Variable对象进行修改，采用 assign 方法
random_var = random.assign(random*3)
shape = tf.shape(t0,name='s')
init = tf.initialize_all_variables()
sess = tf.Session()
sess.run(init)
output = sess.run(random)
output_var = sess.run(random_var)
#  assign_add() 方法实现  自 增加 5
output_var_add = sess.run(random1.assign_add(5))
print(output)
print(output_var)
print(output_var_add)














