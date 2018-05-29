#coding:utf-8
'''
这个方法用来，用tf 实现一个简单的 手写体识别，MNIST

'''
import  tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#载入数据
#          下载的数据存放位置， 标签采用 01
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

#每个批次的大小
batch_size = 80
#计算一共有多少个批次
n_batch = mnist.train.num_examples //batch_size

#定义输入数据
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

#创建一个简单的神经网络    初始化权重
W = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))
prediction = tf.nn.softmax(tf.matmul(x,W)+b)

#二次代价函数
#loss = tf.reduce_mean(tf.square(y-prediction))
#采用交叉熵代价函数
loss = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
#梯度下降
train_step = tf.train.GradientDescentOptimizer(0.2).minimize(loss)

#结果存放在一个布尔型列表中
#argmax返回一维张量中最大的值所在的位置
correct_prediction = tf.equal(tf.arg_max(y,1),tf.arg_max(prediction,1))

#求准确率
#               平均         类型转换
accuracy = tf.reduce_mean(tf.cast(correct_prediction,tf.float32))

# 声明 保存模型
saver = tf.train.Saver()

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(21):
        for batch in range(n_batch):
            #每次输入100 个样本
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})



        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("Iter "+ str(epoch) + ", Test Accurary "+str(acc))
#保存模型
    saver.save(sess,'net/my_net.ckpt')
    #载入模型
    #saver.restore(sess,'net/my_net.ckpt')







