#coding:utf-8
import  tensorflow as tf
state = tf.Variable(0,name = 'conter')
one = tf.constant(1)
new_value = tf.add(state,one)
update = tf.assign(state,new_value)
init_op = tf.global_variables_initializer()

with tf.Session() as sess:
    sess.run(init_op)
    print('kkk:',sess.run(state))
    for _ in range(3):
        #sess.run(update)
        #两种输出方法，意思run，二是，变量的直接输出
        #print(sess.run(state))
        #print(update.eval())#如果用 eval（）可以代替 sess.run（）
        print(sess.run(update))
        print(state.eval())

#feed   可以先用占位符，然后在执行的时候，在传值
def demo_feed():
    input1 = tf.placeholder(tf.float32)
    input2 = tf.placeholder(tf.float32)
    #乘法
    output = tf.multiply(input1,input2)
    with tf.Session() as sess:
        result = sess.run([output],feed_dict= {input1:[7.0],input2:[8.0]} )
        print(result)

demo_feed()
