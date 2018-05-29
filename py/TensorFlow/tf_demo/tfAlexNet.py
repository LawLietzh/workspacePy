#coding:utf-8
from datetime import datetime
import math
import time
import  tensorflow as tf

batch_size = 32
num_batch = 100
#定义一个函数  显示每一层结构的函数 print_actications ,展示每一个卷积层 或池化层 输出tensor ，接受一个tensor
def print_actications(t):
    print(t.op.name,'',t.get_shape().as_list())
#接下来 设计网络结构
def inference(images):
    parameters = []
    with tf.name_scope('conv1') as scope:
        kernel = tf.Variable(tf.truncated_normal([11,11,3,64],dtype=tf.float32,stddev=1e-1),name= 'Weights')
        conv = tf.nn.conv2d(images,kernel,[1,4,4,1],padding='SAME')

        biases = tf.Variable(tf.constant(0.0,shape=[64],dtype=tf.float32),trainable= True,name = 'biases')
        bias = tf.nn.bias_add(conv,biases)
        conv1 = tf.nn.relu(bias,name= scope)
        print_actications(conv1)
        parameters +=[kernel,biases]
        # lrn 层 和 pool 层
        lrn1 = tf.nn.lrn(conv1,4,bias = 1.0,alpha= 0.001/9,beta = 0.75,name = 'lrn1')
        pool1 = tf.nn.max_pool(lrn1,ksize=[1,3,3,1],strides=[1,2,2,1],padding='VALID',name='pool1')
        print_actications(pool1)

    with tf.name_scope('conv2') as scope:
        kernel = tf.Variable(tf.truncated_normal([5,5,64,192],dtype=tf.float32,stddev=1e-1),name= 'Weights')
        conv = tf.nn.conv2d(pool1,kernel,[1,1,1,1],padding='SAME')
        biases = tf.Variable(tf.constant(0.0,shape=[192],dtype=tf.float32),trainable= True,name = 'biases')
        bias = tf.nn.bias_add(conv,biases)
        conv2 = tf.nn.relu(bias,name= scope)
        print_actications(conv2)
        parameters +=[kernel,biases]
        # lrn 层 和 pool 层
        lrn2 = tf.nn.lrn(conv2,4,bias = 1.0,alpha= 0.001/9,beta = 0.75,name = 'lrn2')
        pool2 = tf.nn.max_pool(lrn2,ksize=[1,3,3,1],strides=[1,2,2,1],padding='VALID',name='pool2')
        print_actications(pool2)

    with tf.name_scope('conv3') as scope:
        kernel = tf.Variable(tf.truncated_normal([3,3,192,384],dtype=tf.float32,stddev=1e-1),name= 'Weights')
        conv = tf.nn.conv2d(pool2,kernel,[1,1,1,1],padding='SAME')
        biases = tf.Variable(tf.constant(0.0,shape=[384],dtype=tf.float32),trainable= True,name = 'biases')
        bias = tf.nn.bias_add(conv,biases)
        conv3 = tf.nn.relu(bias,name= scope)
        print_actications(conv3)
        parameters +=[kernel,biases]

    with tf.name_scope('conv4') as scope:
        kernel = tf.Variable(tf.truncated_normal([3,3,384,256],dtype=tf.float32,stddev=1e-1),name= 'Weights')
        conv = tf.nn.conv2d(conv3,kernel,[1,1,1,1],padding='SAME')
        biases = tf.Variable(tf.constant(0.0,shape=[256],dtype=tf.float32),trainable= True,name = 'biases')
        bias = tf.nn.bias_add(conv,biases)
        conv4 = tf.nn.relu(bias,name= scope)
        print_actications(conv4)
        parameters +=[kernel,biases]

    with tf.name_scope('conv5') as scope:
        kernel = tf.Variable(tf.truncated_normal([3,3,256,256],dtype=tf.float32,stddev=1e-1),name= 'Weights')
        conv = tf.nn.conv2d(conv4,kernel,[1,1,1,1],padding='SAME')
        biases = tf.Variable(tf.constant(0.0,shape=[256],dtype=tf.float32),trainable= True,name = 'biases')
        bias = tf.nn.bias_add(conv,biases)
        conv5 = tf.nn.relu(bias,name= scope)
        print_actications(conv5)
        parameters +=[kernel,biases]
        pool5 = tf.nn.max_pool(conv5,ksize=[1,3,3,1],strides=[1,2,2,1],padding='VALID',name='pool5')
        print_actications(pool5)
        return pool5,parameters

#接下来，实现 一个评估 alexNet 每轮计算时间的函数 time_tensorflow_run
#第一个是 tensorflow 的session，第二个 是要评估的 运算算子，第三个变量是测试的名称

def time_tensorflow_run(session,target,info_string):
    num_steps_burn_in = 10
    total_duration = 0.0
    total_duration_squared = 0.0

    for i in range(num_batch+ num_steps_burn_in):
        start_time = time.time()
        _ = session.run(target)
        duration = time.time() - start_time
        if i>=num_steps_burn_in:
            if not i%10:
                print('%s:step %d, duration = %.3f' % (datetime.now(),i-num_steps_burn_in,duration))
            total_duration += duration
            total_duration_squared += duration *duration

















