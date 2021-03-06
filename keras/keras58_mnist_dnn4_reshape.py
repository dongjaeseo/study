# 인공지능계의 hello world라 불리는 mnist
# # 실습!! 완성하시오!!
# 지표는 acc

import numpy as np
import matplotlib.pyplot as plt

from tensorflow.keras.datasets import mnist

(x_train,y_train),(x_test,y_test) = mnist.load_data()
x_pred = x_test[:10]

from sklearn.model_selection import train_test_split
x_train,x_val,y_train,y_val = train_test_split(x_train,y_train,train_size = 0.8, shuffle = True)

x_train = x_train.reshape(x_train.shape[0],x_train.shape[1],x_train.shape[2],1).astype('float32')/255.
x_test = x_test.reshape(x_test.shape[0],x_test.shape[1],x_test.shape[2],1)/255.
x_pred = x_pred.reshape(x_pred.shape[0],x_pred.shape[1],x_pred.shape[2],1)/255.
x_val = x_val.reshape(x_val.shape[0],x_val.shape[1],x_val.shape[2],1)/255.
# (x_test.reshape(x_test.shape[0],x_test.shape[1],x_test.shape[2],1))

y_train = x_train
y_test = x_test
y_val = x_val

print(y_train.shape)
print(y_test.shape)


# # OneHotEncoding
# from tensorflow.keras.utils import to_categorical
# y_train = to_categorical(y_train)
# y_test = to_categorical(y_test)
# y_val = to_categorical(y_val)


#2. 모델링
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Conv2D, MaxPooling2D, Flatten, Dropout
from tensorflow.keras.layers import Reshape

model = Sequential()
# model.add(Conv2D(filters = 80, kernel_size = (2,2), padding = 'same', strides = 1, input_shape = (28,28,1)))
# model.add(MaxPooling2D(pool_size=2))
# model.add(Dropout(0.5))
# model.add(Conv2D(1,2))
# model.add(Conv2D(1,2))
# model.add(Flatten())
model.add(Dense(64,input_shape = (28,28,1)))
model.add(Flatten())
model.add(Dense(64))
model.add(Dense(784,activation = 'relu'))
model.add(Reshape((28,28,1)))
model.add(Dense(1))
model.summary()

#3. 컴파일 훈련
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
modelpath = '../Data/modelcheckpoint/k57_mnist_{epoch:02d}-{val_loss:.4f}.hdf5'
es = EarlyStopping(monitor = 'val_loss', patience = 10, mode = 'auto')
cp = ModelCheckpoint(filepath=modelpath, monitor = 'val_loss', save_best_only=True, mode = 'auto')
reduce_lr = ReduceLROnPlateau(monitor='val_loss', patience = 5, factor =0.5, verbose = 1)

model.compile(loss = 'mse', optimizer = 'adam', metrics = ['acc'])
hist = model.fit(x_train,y_train, epochs = 1000, batch_size = 16 ,validation_data=(x_val,y_val), verbose = 1, callbacks = [es,cp,reduce_lr])

#4. 평가 예측
loss = model.evaluate(x_test,y_test,batch_size = 16)
print('loss : ', loss[0])
print('acc : ', loss[1])

y_pred = model.predict(x_test)
print(y_pred[0])
print(y_pred.shape)

