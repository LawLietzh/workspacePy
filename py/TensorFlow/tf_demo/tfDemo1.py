#coding:utf-8
'''

这是一个简单的 入门前小栗子 

'''
import  tensorflow as tf
import  numpy as np

#使用numpy 生成100个 随机点(在 0 -1 之间)
x_data = np.random.rand(100)
print(type(x_data))
y_data = x_data*0.1 +0.2

#构造一个线性模型
b = tf.Variable(0.)
k = tf.Variable(0.)
y = k*x_data + b
#二次代价函数
#误差的【平方，求平均值
loss = tf.reduce_mean(tf.square(y_data-y))

#定义一个梯度下降法 ，进行训练的优化器

optimizer = tf.train.GradientDescentOptimizer(0.2)

#训练的目的，最小化代价函数
train = optimizer.minimize(loss)
#变量初始化
init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    #迭代训练
    for step in range(201):
        sess.run(train)
        if step%20 == 0:
            print(step,sess.run([k,b]))

