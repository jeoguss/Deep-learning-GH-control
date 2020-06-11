# -*- coding: utf-8 -*-
"""
Created on Wed Jun 26 17:35:33 2019

@author: user
"""

# -*- coding: utf-8 -*-
"""
Created on Mon Mar 18 22:17:39 2019

@author: jeogus
"""


import keras
from keras.models import Sequential
from keras.layers import Dense, Dropout, Flatten, Conv2D, MaxPooling2D
from keras.utils import to_categorical
from keras.layers import LSTM


y_train=Y_data2csv[:,1]
X_train = X_train.reshape(X_train.shape[0], 9, 30, 1)

X_test = X_train[4000:6000]
y_test = y_train[4000:6000]

y_train_hot = to_categorical(y_train)
y_test_hot = to_categorical(y_test)





model = Sequential()
model.add(Conv2D(24, (1, 2), activation='relu', input_shape=(9, 30, 1)))
model.add(Conv2D(24, (1, 2), activation='relu'))
model.add(MaxPooling2D(pool_size=(1, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(24, (1, 2), activation='relu', input_shape=(9, 30, 1)))
model.add(Conv2D(24, (1, 2), activation='relu'))
model.add(MaxPooling2D(pool_size=(1, 2)))
model.add(Dropout(0.25))

model.add(Conv2D(12, kernel_size=(2, 2), activation='relu' ))
model.add(Conv2D(12, kernel_size=(2, 2), activation='relu' ))
model.add(Dropout(0.25))

model.add(Conv2D(6, kernel_size=(2, 2), activation='relu' ))
model.add(Conv2D(6, kernel_size=(2, 2), activation='relu' ))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(24))
model.add(Dense(5))
model.compile(loss=keras.losses.categorical_crossentropy,
              optimizer=keras.optimizers.Adadelta(),
              metrics=['accuracy'])
print (model.summary())
history= model.fit(X_train, y_train_hot, batch_size=100, epochs=100, verbose=1,validation_data=(X_test, y_test_hot))

print(history.history.keys())


# "Loss"
y_prob=np.zeros(2000)
for x in range(0,1999):
    a=X_test[x].reshape(1,9,30,1)
    y_prob[x]= model.predict_classes(a)
    
