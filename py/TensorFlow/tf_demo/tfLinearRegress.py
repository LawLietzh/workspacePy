#coding:utf-8
'''
这个类，用于联系，tf 运行线性回归
'''

import tensorflow as tf
import numpy as np
import matplotlib.pyplot as plt

#使用numpy 生成200个随机点
#在-0.5 到 0.5 之间 均匀的产生 200个点 。并且把这些点，变成列，也就是每行一个数据，有两百行

#输入层 数据
x_data = np.linspace(-0.5,0.5,200)[:,np.newaxis]
#print(x_data)
#随机产生一些点，在0到0.02 之间，形状和x_data.shape()相同
noise = np.random.normal(0,0.02,x_data.shape)
#print(noise)
y_data = np.square(x_data) + noise

#定义两个placeholder  输入层 数据格式，就是一个点
x = tf.placeholder(tf.float32,[None,1])
y = tf.placeholder(tf.float32,[None,1])

#定义神经网络中间层
#输入层是一个点，就是x ，中间有10个节点，因此 【1.10】
Weights_L1 = tf.Variable(tf.random_normal([1,10]))
#偏置值，是对应的神经元，偏置的个数要神经元的个数一样
biases_L1 = tf.Variable(tf.zeros([1,10]))
print('b1:',biases_L1)
#这个得到是，输入和每个对应权重的乘积，加偏置
Wx_plus_b_L1 = tf.matmul(x,Weights_L1)+biases_L1
#通过激活函数
L1 = tf.nn.tanh(Wx_plus_b_L1)

#定义输出层


Weights_L2 = tf.Variable(tf.random_normal([10,1]))
#L2对应的是输出层的神经元，因此偏置的个数，是1 ，这就是L2 和L1 不同原因
biases_L2 = tf.Variable(tf.zeros([1,1]))
print('b2:',biases_L2)
Wx_plus_b_L2 = tf.matmul(L1,Weights_L2)+biases_L2

prediction = tf.nn.tanh(Wx_plus_b_L2)

#定义代价函数
loss = tf.reduce_mean(tf.square(y-prediction))
#定义训练方法
train_step = tf.train.GradientDescentOptimizer(0.1).minimize(loss)

#执行
with tf.Session() as sess:
    #变量初始化
    sess.run(tf.global_variables_initializer())
    #
    for _ in range(2000):
        print('b1:',biases_L1.eval())
        print('b2:',biases_L2.eval())
        sess.run(train_step,feed_dict={x:x_data,y:y_data})

    #获得预测值
    prediction_value = sess.run(prediction,feed_dict={x:x_data})
    #画图
    plt.figure()
    plt.scatter(x_data,y_data)
    plt.plot(x_data,prediction_value,'r-',lw=5)
    plt.show()





