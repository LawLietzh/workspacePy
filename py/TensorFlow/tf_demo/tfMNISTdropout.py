#coding:utf-8
'''
这个方法用来，用tf 实现一个简单的 手写体识别，MNIST

'''
import  tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

#载入数据
#                                  下载的数据存放位置， 标签采用 01
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)

#每个批次的大小
batch_size = 80
#计算一共有多少个批次
n_batch = mnist.train.num_examples //batch_size

#定义输入数据
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])
keep_prob = tf.placeholder(tf.float32)

#创建一个简单的神经网络
#采用截段的正太分布，标准差为0.1  来初始化
W1 = tf.Variable(tf.truncated_normal([784,2000],stddev=0.1))
b1 = tf.Variable(tf.zeros([2000])+0.1)
L1 = tf.nn.tanh(tf.matmul(x,W1)+b1)
L1_drop = tf.nn.dropout(L1,keep_prob)


W2 = tf.Variable(tf.truncated_normal([2000,2000],stddev=0.1))
b2 = tf.Variable(tf.zeros([2000])+0.1)
L2 = tf.nn.tanh(tf.matmul(L1_drop,W2)+b2)
L2_drop = tf.nn.dropout(L2,keep_prob)

W3 = tf.Variable(tf.truncated_normal([2000,1000],stddev=0.1))
b3 = tf.Variable(tf.zeros([1000])+0.1)
#双曲真切激活函数
L3 = tf.nn.tanh(tf.matmul(L2_drop,W3)+b3)
L3_drop = tf.nn.dropout(L3,keep_prob)

W4 = tf.Variable(tf.truncated_normal([1000,10],stddev=0.1))
b4 = tf.Variable(tf.zeros([10])+0.1)
prediction = tf.nn.softmax(tf.matmul(L3_drop,W4)+b4)

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

init = tf.global_variables_initializer()
with tf.Session() as sess:
    sess.run(init)
    for epoch in range(31):
        for batch in range(n_batch):
            #每次输入100 个样本
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:0.7})



        test_acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels,keep_prob:1.0})
        train_acc = sess.run(accuracy,feed_dict={x:mnist.train.images,y:mnist.train.labels,keep_prob:1.0})
        print("Iter "+ str(epoch) + ", Test Accurary "+str(test_acc)+ ", Train Accurary "+str(train_acc))









