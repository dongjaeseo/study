import numpy as np

#1. 데이터
from sklearn.datasets import load_diabetes
dataset = load_diabetes()

x = dataset.data
y = dataset.target
# print(x.shape,y.shape) (442, 10) (442,)

from sklearn.model_selection import train_test_split as tts
x_train, x_test, y_train, y_test = tts(x,y,train_size = 0.8, shuffle = True, random_state = 1)
x_train,x_val,y_train,y_val = tts(x_train,y_train,train_size = 0.8, shuffle = True, random_state = 1)

from sklearn.preprocessing import MinMaxScaler
scale = MinMaxScaler()
scale.fit(x_train)
x_train = scale.transform(x_train)
x_test = scale.transform(x_test)
x_val = scale.transform(x_val)

x_train = x_train.reshape(x_train.shape[0],2,5,1)
x_test = x_test.reshape(x_test.shape[0],2,5,1)
x_val = x_val.reshape(x_val.shape[0],2,5,1)

#2. 모델링
from tensorflow.keras.models import Model
from tensorflow.keras.layers import Dense, Conv2D, Input, MaxPooling2D, Dropout, Flatten

input = Input(shape = (2,5,1))
d = Conv2D(100, (2,3), activation ='relu', padding = 'same')(input)
d = Dropout(0.3)(d)
d = Conv2D(20, 2)(d)
d = Dropout(0.2)(d)
d = Flatten()(d)
d = Dense(10)(d)
d = Dense(1)(d)

model = Model(inputs = input, outputs = d)
# model.summary()

#3. 컴파일 훈련
from tensorflow.keras.callbacks import EarlyStopping
es = EarlyStopping(monitor = 'loss', patience = 20, mode = 'auto')
model.compile(loss = 'mse', optimizer = 'adam', metrics = ['mae'])
model.fit(x_train,y_train,epochs = 1000, validation_data=(x_val,y_val), callbacks = [es], batch_size = 1)

#4. 평가 예측
loss = model.evaluate(x_test,y_test,batch_size = 1)
print('loss : ', loss[0])
print('mae : ', loss[1])

from sklearn.metrics import r2_score
y_pred = model.predict(x_test)
print("R2", r2_score(y_pred,y_test))

# loss :  3107.17236328125
# mae :  42.03068923950195
# R2 -0.43297496866083907