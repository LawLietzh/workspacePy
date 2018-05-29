#coding:utf-8
'''

序惯模型，是多个网络层 的线性堆叠，也就是 ‘一条路周到黑’
可以通过向Sequential 模型 传递一个layer 的list 来 构造该模型 

'''
from keras.models import Sequential
from  keras.layers import  Dense,Activation


#model = Sequential([Dense(32,units=784),Activation('relu'),Dense(10),Activation('softmax'),])
#也可以 通过.add（） 方法一个个的将layer 加入模型中
'''
model = Sequential()
model.add(Dense(32, input_shape=(784,)))
model.add(Activation('relu'))
'''

model = Sequential()
model.add(Dense(32, activation='relu', input_dim=100))
model.add(Dense(1, activation='sigmoid'))
#在训练模型之前，我们需要通过compile 来学习过程 进行配置，
'''
优化器 optimizer ，该参数可指定为已 预定义的优化器  
损失函数loss ： 该参数为模型试图最小化的目标函数 
指标列表metrics ： 对分类问题，我们一般 将该列表设置 

'''
model.compile(optimizer='rmsprop',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Generate dummy data
import numpy as np
data = np.random.random((1000, 100))
labels = np.random.randint(2, size=(1000, 1))

# Train the model, iterating on the data in batches of 32 samples
model.fit(data, labels, epochs=10, batch_size=32)













