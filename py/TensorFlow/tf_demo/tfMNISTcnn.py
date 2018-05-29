#coding:utf-8
import tensorflow as tf
from tensorflow.examples.tutorials.mnist import input_data

'''
使用cnn实现，mnist手写体识别

'''

#载入数据
#                                  下载的数据存放位置， 标签采用 01
mnist = input_data.read_data_sets("MNIST_data",one_hot=True)
print(mnist)
#每个批次的大小
batch_size = 100
#计算一共有多少个批次
n_batch = mnist.train.num_examples #batch_size

#初始化权值
# shape 是形状
def weight_variable(shape):
    #生成一个截断的 正太分布，从中产生随机数，来初始化 0.1  为标准差
    initial = tf.truncated_normal(shape,stddev= 0.1)
    return  tf.Variable(initial)

#初始化偏置 固定值 0.1
def bias_variable(shape):
    initial = tf.constant(0.1,shape =shape)
    return tf.Variable(initial)

#卷积层
def conv2d(x,W):
    # x 输入，一个tensor ，是一个四维，批次，长，款，通道数
    #W，卷积核，也是一个rensor，长，宽，输入通道数，输出通道数
    #strides[0] strides[3] = 1 代表x方向，strides[1]，strides[2]代表步长
    #padding
    return tf.nn.conv2d(x,W,strides=[1,1,1,1],padding='SAME')

#池化层。
def max_pool_2x2(x):
   #ksize 池化窗口
   #strides 步长
    return tf.nn.max_pool(x,ksize=[1,2,2,1],strides=[1,2,2,1],padding='SAME')

#定义输入数据  placeholder  为占位符，相当于定义了变量
x = tf.placeholder(tf.float32,[None,784])
y = tf.placeholder(tf.float32,[None,10])

#改变x的格式为4D 的向量，[batch, height,width, channels]
#-1 代表样本数量不固定， 1 代表颜色通道
x_image = tf.reshape(x,[-1,28,28,1])

#初始化，第一个卷积层的权值和偏置
#采用5*5 的采样，32 个卷积核，1是通道，这个数量要和 x_image输入数据的通道数一样
W_conv1 = weight_variable([5,5,1,32])
b_conv1 = bias_variable([32])#每一个卷积核的偏置值，和卷积核的数量同步

#第一个卷积层的得到的结果
# 先进行卷积，然后激活函数
h_conv1 = tf.nn.relu(conv2d(x_image,W_conv1)+b_conv1)
#最好池化
h_poo11 = max_pool_2x2(h_conv1)

#初始化第二个卷积权值和偏置
#因为上一层的卷积核个数是32 ，因此有32个特征平面，所以有32个通道
#所以第二层卷积  的卷积核通道数是32，
#5*5 的卷积窗口，64个卷积核从 32 个平面抽取特征
W_conv2 = weight_variable([5,5,32,64])
b_conv2 = bias_variable([64])

#第二次卷积
#把上一层的输出，作为输入
h_conv2 = tf.nn.relu(conv2d(h_poo11,W_conv2)+b_conv2)
h_pool2 = max_pool_2x2(h_conv2)

'''
因为卷积是SAME卷积，因此第一个卷积后，还是28*28 ，
池化也是SAME池化，池化后也应该是28*28 ，但是步长是2，所以，池化后是 14*14 
同理，二层池化后是 7*7 

'''


#全连接层之前的数据，是 64个 7*7图片，把64个图片，组合成一张图片，
#初始化，第一个全连接层的权值
#上一层7*7*64个神经元，全连接层有1024个神经元
W_fc1 = weight_variable([7*7*64,1024])
b_fc1 = bias_variable([1024])
#把池化层2 的输出扁平化为1 维
#h_pool2 的shape 是[100,7,7,64] 要变成 7*7*64
h_pool2_flat = tf.reshape(h_pool2,[-1,7*7*64])
h_fc1 = tf.nn.relu(tf.matmul(h_pool2_flat,W_fc1)+b_fc1)

#dropout层
#keep_prob 用来表示神经元的输出概率，就是让一部分神经元工作，一部分不工作
keep_prob = tf.placeholder(tf.float32)
h_fc1_drop = tf.nn.dropout(h_fc1,keep_prob)

#初始化，第二个全连接层
#说明我们有10个分类
W_fc2 = weight_variable([1024,10])
b_fc2 = bias_variable([10])

#计算输出
prediction = tf.nn.softmax(tf.matmul(h_fc1_drop,W_fc2)+b_fc2)

#交叉熵代价函数
cross_entropy = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(labels=y,logits=prediction))
#使用AdamOptimizer进行优化
train_step = tf.train.AdamOptimizer(1e-4).minimize(cross_entropy)

#结果存放在一个布尔列表中
cross_prediction = tf.equal(tf.arg_max(prediction,1),tf.arg_max(y,1))
#求准确率
accuracy = tf.reduce_mean(tf.cast(cross_prediction,tf.float32))


#下面开始训练过程
with tf.Session() as sess:
    #初始化变量
    sess.run(tf.global_variables_initializer())
    batch_xs,batch_ys = mnist.train.next_batch(batch_size)
    print(batch_xs[0:3])
    #循环周期
    for epoch in range(21):
        #循环batch
        for batch in range(n_batch):
            batch_xs,batch_ys = mnist.train.next_batch(batch_size)
            sess.run(train_step,feed_dict={x:batch_xs,y:batch_ys,keep_prob:0.7})
        #测试的时候，keep_prob 是1
        acc = sess.run(accuracy,feed_dict={x:mnist.test.images,y:mnist.test.labels,keep_prob:1.0})
        print("Iter"+str(epoch)+",Testing Accuracy = "+ str(acc))






