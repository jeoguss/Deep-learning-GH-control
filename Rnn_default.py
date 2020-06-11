#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  5 08:18:23 2019

@author: jeogus
"""
from numpy import loadtxt
from urllib.request import urlopen
import numpy as np
import pandas as pd
from math import sqrt
from numpy import concatenate
from matplotlib import pyplot
from pandas import read_csv
from pandas import DataFrame
from pandas import concat
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import mean_squared_error
from keras.models import Sequential
from keras.layers import Dense
from keras.layers import LSTM
import numpy
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from tensorflow.python.keras.wrappers.scikit_learn import KerasRegressor
from keras.models import model_from_json
from sklearn.model_selection import cross_val_score
from sklearn.model_selection import KFold
from sklearn.pipeline import Pipeline

# convert series to supervised learning
def series_to_supervised(data, n_in=1, n_out=1, dropnan=True):
	n_vars = 1 if type(data) is list else data.shape[1]
	df = DataFrame(data)
	cols, names = list(), list()
	# input sequence (t-n, ... t-1)
	for i in range(n_in, 0, -1):
		cols.append(df.shift(i))
		names += [('var%d(t-%d)' % (j+1, i)) for j in range(n_vars)]
	# forecast sequence (t, t+1, ... t+n)
	for i in range(0, n_out):
		cols.append(df.shift(-i))
		if i == 0:
			names += [('var%d(t)' % (j+1)) for j in range(n_vars)]
		else:
			names += [('var%d(t+%d)' % (j+1, i)) for j in range(n_vars)]
	# put it all together
	agg = concat(cols, axis=1)
	agg.columns = names
	# drop rows with NaN values
	if dropnan:
		agg.dropna(inplace=True)
	return agg
 
# load dataset
numpy.random.seed(7)

# load pima indians dataset
filename = 'RNN_30.csv'
filename_test = 'test_30.csv'
raw_data = open(filename, 'rt')
raw_data_test = open(filename_test, 'rt')
dataset = loadtxt(raw_data, delimiter=",")
dataset_test = loadtxt(raw_data_test, delimiter=",")
print(dataset.shape)
# split into input (X) and output (Y) variables
x = dataset[:,0:13]
x_new = dataset_test[:,0:13]
#14=tem, 15=hum, 16=co2
y = dataset[:,16]
y=np.reshape(y, (-1,1))
scaler_x = MinMaxScaler()
scaler_y = MinMaxScaler()
print(scaler_x.fit(x))
xscale=scaler_x.transform(x)
x_new_test=scaler_x.transform(x_new)
print(scaler_y.fit(y))
yscale=scaler_y.transform(y)

reframed = series_to_supervised(xscale, 1, 1)
reframed_val= series_to_supervised(x_new_test, 1, 1)
train_X = reframed.values
test_X = reframed_val.values
y_new=yscale[:-1,:]
# drop columns we don't want to predict
print(reframed.head())

# reshape input to be 3D [samples, timesteps, features]

train_X = train_X.reshape((train_X.shape[0], 1, train_X.shape[1]))
test_X = test_X.reshape((test_X.shape[0], 1, test_X.shape[1]))
print(train_X.shape, train_y.shape, test_X.shape, test_y.shape)

# design network
model = Sequential()
model.add(LSTM(55, input_shape=(train_X.shape[1], train_X.shape[2])))
model.add(Dense(1))
model.compile(loss='mse', optimizer='adam')
# fit network
history = model.fit(train_X, y_new, epochs=100, batch_size=200, verbose=2, shuffle=False)
# plot history
pyplot.plot(history.history['loss'], label='train')
pyplot.legend()
pyplot.show()
 # make a prediction
yhat = model.predict(test_X)
mse=history.history['loss']
#test_X = test_X.reshape((test_X.shape[0], test_X.shape[2]))
# invert scaling for forecast
#inv_yhat = concatenate((yhat, test_X[:, 1:]), axis=1)
#inv_yhat = scaler.inverse_transform(inv_yhat)
#inv_yhat = inv_yhat[:,0]
# invert scaling for actual
#test_y = test_y.reshape((len(test_y), 1))
#inv_y = concatenate((test_y, test_X[:, 3:]), axis=1)
#inv_y = scaler_val.inverse_transform(inv_y)
#inv_y = inv_y[:,0]
# calculate RMSE
y_test_unscale=scaler_y.inverse_transform(yhat)

