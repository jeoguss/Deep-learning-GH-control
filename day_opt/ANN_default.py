#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 18:24:23 2019

@author: jeogus
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  2 11:24:30 2019

@author: jeogus
"""

from keras.models import Sequential
from keras.layers import Dense
import numpy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import MinMaxScaler
from tensorflow.python.keras.models import Sequential
from tensorflow.python.keras.layers import Dense
from tensorflow.python.keras.wrappers.scikit_learn import KerasRegressor
from keras.models import model_from_json

# Load CSV from URL using NumPy
from numpy import loadtxt
from urllib.request import urlopen
# fix random seed for reproducibility
numpy.random.seed(7)

# load pima indians dataset
filename = 'training_data_hot_30.csv'
filename_test = 'data_hot.csv'
raw_data = open(filename, 'rt')
raw_data_test = open(filename_test, 'rt')
dataset = loadtxt(raw_data, delimiter=",")
dataset_test = loadtxt(raw_data_test, delimiter=",")
print(dataset.shape)
# split into input (X) and output (Y) variables
x = dataset[:,0:13]
x_new = dataset_test[:,0:13]
#14=tem, 15=hum, 16=co2
y = dataset[:,14]
y=np.reshape(y, (-1,1))
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
print(scaler_x.fit(x))
xscale=scaler_x.transform(x)
x_new_test=scaler_x.transform(x_new)
print(scaler_y.fit(y))
yscale=scaler_y.transform(y)

#data_len
data_len=np.shape(x)[0]
data_len_3=data_len-3420
data_len_6=data_len-6840
data_len_10=data_len-11400
data_len_20=data_len-22800

train_y_20=yscale[data_len_20:data_len,:]
train_x_20=xscale[data_len_20:data_len,:]
train_y_10=yscale[data_len_10:data_len,:]
train_x_10=xscale[data_len_10:data_len,:]
train_y_6=yscale[data_len_6:data_len,:]
train_x_6=xscale[data_len_6:data_len,:]
train_y_3=yscale[data_len_3:data_len,:]
train_x_3=xscale[data_len_3:data_len,:]
#X_train, X_test, y_train, y_test = train_test_split(xscale, yscale)
# create model
model = Sequential()
model.add(Dense(30, input_dim=13, activation='relu'))
model.add(Dense(25, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
model.summary()

# Compile model
model.compile(loss='mse', optimizer='adam', metrics=['mse','mae'])
# Fit the model
history = model.fit(xscale, yscale, epochs=100, batch_size=25,  verbose=1, validation_split=0.1)
print(history.history.keys())
# "Loss"

mse_5=history.history['mean_squared_error']
mse_5_val=history.history['val_mean_squared_error']

a= model.predict(x_new_test)
y_test_unscale=scaler_y.inverse_transform(a)

#save
with open("data_cold_30_co", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("data_cold_30_co.json.h5")
print("Saved model to disk")
