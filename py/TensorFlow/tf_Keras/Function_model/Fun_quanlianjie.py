#coding：utf-8
'''
Keras 函数式 模型接口是用户定义多输出模型，非循环有向模型，或具有共享层的模型等复杂模型的途径，
一句话，只要你的模型不是类似VGG 一样 一条路走到黑的模型，或者你的模型需要多于一个的输出，那么你总应该选择函数式模型
Sequential 只是它的一种特殊情况
'''
# 接下来 用函数式 编程的模式，实现第一个简单的模型，全连接网络
#Sequential 当然是实现全连接最好的方式，但是我们从简单的全连接网络开始，有助于 我们学习这部分内容

'''
在开始前，有几个概念 
层对象 接受张量 为参数，返回一个张量 
输入时张量，输出也是张量的一个框架就是模型，通过Model 定义 
这样的模型 可以被像keras 的 sequential 一样被训练


'''
from keras.layers import Input, Dense
from keras.models import Model

inputs = Input(shape=(784,))
x = Dense(64,activation='relu')(inputs)
x = Dense(64, activation='relu')(x)
predictions = Dense(10, activation='softmax')(x)

#
model = Model(inputs = inputs,outputs= predictions)

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])
#model.fit(data, labels)  开始训练

'''
所有的模型都是可调用的，就想层一样
注意当你调用一个模型时，你不仅仅重用了它的结构，也重用了它的权重。


多输入和多输出模型
     使用函数式模型的一个典型场景是搭建多输入、多输出的模型。
     
     
'''




