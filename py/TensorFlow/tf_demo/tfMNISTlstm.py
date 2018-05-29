#coding:utf-8
'''
lstm的tensorflow实现
rnn 的网络结构
'''
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data
from tensorflow.python.ops import  rnn,rnn_cell

#载入数据
#                                 下载的数据存放位置， 标签采用 01
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)
print(type(mnist))
print(mnist[0:1])
#输入图片是 28*28
n_input = 28  #输入一行，一行有28个数据
max_time = 28 # 一共28 行
lstm_size = 100  #隐层单元
n_classes = 10  #10个分类
batch_size = 50 #每个批次50个样本
#计算一共有多少个批次
n_batch = mnist.train.num_examples //batch_size

#定义输入数据
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

#初始化权值
weights = tf.Variable(tf.truncated_normal([lstm_size,n_classes],stddev= 0.1))
#初始化偏置值
biases = tf.Variable(tf.constant(0.1,shape=[n_classes]))

#定义初始权值
def RNN(X,weight,biases):
    #input = [batch_size,max_time,n_input]
    inputs = tf.reshape(X,[-1,max_time,n_input])
    #定义LSTM基本cell
    #新版本要这么写，下面一行是老版本的写法，有错误
    lstm_cell = tf.contrib.rnn.BasicLSTMCell(lstm_size)
    #lstm_cell = tf.python.ops.rnn_cell.BasicLSTMCell(lstm_size)

    #final_state[state,batch_size,cell.state_size]
    #            (0,1 )  50           100
    #final_state[0] 是cell state  （中间信号）
    #final_state[1] 是 hihhen——state  （时间序列最后的输出信号）

#output: the RNN output 'tensor'
    #if time_major == False(default) ,this will be a 'tensor' shaped
    #[batch_size ,max_time,cell.output_size]    记录的每次时间序列的输出信号
    #if time_major == True(default) ,this will be a 'tensor' shaped
    #[max_time,batch_size,cell.output_size]
    output,final_state = tf.nn.dynamic_rnn(lstm_cell,inputs,dtype=tf.float32)
    results = tf.nn.softmax(tf.matmul(final_state[1],weight)+biases)
    return results

#计算RNN的返回结果
prediction = RNN(x,weights,biases)
#损失函数
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=y))
#使用AdamOptimizer进行优化
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)
#结果存放在一个布尔列表中
cross_prediction = tf.equal(tf.arg_max(prediction,1),tf.arg_max(y,1))
#求准确率
accuracy = tf.reduce_mean(tf.cast(cross_prediction,tf.float32))


#初始化变量
init = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init)
    for epoch in range(6):
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys})

        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels})
        print("Iter"+str(epoch)+",Testing Accuracy = "+ str(acc))


