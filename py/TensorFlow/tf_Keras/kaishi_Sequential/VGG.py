#coding:utf-8
import numpy as np
import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten
from keras.layers import Conv2D, MaxPooling2D
from keras.optimizers import SGD

x_train = np.random.random((100, 100, 100, 3))
y_train = keras.utils.to_categorical(np.random.randint(10, size=(100, 1)), num_classes=10)
x_test = np.random.random((20, 100, 100, 3))
y_test = keras.utils.to_categorical(np.random.randint(10, size=(20, 1)), num_classes=10)
#print(y_train[10:20])

model = Sequential()
#  32 卷积核 的数目，（3,3）卷积核的跨度 和长度   input_shape = (rows,cols,channels)  输入数据的长宽高 和通道
model.add(Conv2D(32,(3,3),activation = 'relu',input_shape=(100,100,3)))
model.add(Conv2D(32,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.25))

model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(Conv2D(64, (3, 3), activation='relu'))
model.add(MaxPooling2D(pool_size=(2, 2)))
model.add(Dropout(0.25))
#Flatten 层用来将输入 "压平" ，即把多维的输入一维话，常用在从卷积层到全连接层的过度，Flatten 不影响batch的大小
model.add(Flatten())
model.add(Dense(256, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(10, activation='softmax'))

sgd = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd)


#训练
model.fit(x_train, y_train, batch_size=32, epochs=10)
#测试
score = model.evaluate(x_test, y_test, batch_size=32)
print(score)