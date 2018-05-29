#coding:utf-8
import numpy as np
from keras.models import Sequential
from keras.layers import Dense, Dropout

x_train = np.random.random((1000, 20))# 产生 1000 行 20 列的 0 到1 之间的浮点数
y_train = np.random.randint(2, size=(1000, 1))
#print(y_train)
x_test = np.random.random((100, 20))
y_test = np.random.randint(2, size=(100, 1))

model = Sequential()
#Dense  全连接层
# 64 :大于0 的整数，代表该层的输出维度    input_dim=20  输入数据的维度
model.add(Dense(64,input_dim=20,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64,input_dim=20,activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy',
              optimizer='rmsprop',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          epochs=20,
          batch_size=128)
#本函数，按batch 计算在某些输入数据上，模型的误差
score = model.evaluate(x_test, y_test, batch_size=128)
print(score)
print(model.get_config())









