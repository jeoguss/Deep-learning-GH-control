import numpy as np
import keras
import pandas 
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
from keras.models import load_model
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time
import datetime
import csv

from sklearn.externals import joblib

temp_scaler_x = joblib.load('temp_scaler_x.save') 
temp_scaler_y = joblib.load('temp_scaler_y.save') 
hum_scaler_x = joblib.load('hum_scaler_x.save') 
hum_scaler_y = joblib.load('hum_scaler_y.save') 

import tensorflow as tf 

temp_model = tf.keras.models.load_model('temp_model.h5')
hum_model = tf.keras.models.load_model('hum_model.h5')



xtime=[]
xtime_ahead=[]
temp=[]
temp_expect=[]
hum=[]
hum_expect=[]

def load_model():
    out_data=pd.read_csv('out_data.csv')
    R1_data=pd.read_csv('R1_data.csv')
    R2_data=pd.read_csv('R2_data.csv')
    R3_data=pd.read_csv('R3_data.csv')
    inside_data=pd.read_csv('inside_data.csv')
    out_data=out_data.values
    R1_data=R1_data.values
    R2_data=R2_data.values
    R3_data=R3_data.values
    inside_data=inside_data.values
    a=out_data[out_data.shape[0]-1,:]
    b=R1_data[R1_data.shape[0]-1,:]
    c=R2_data[R2_data.shape[0]-1,:]
    d=R3_data[R3_data.shape[0]-1,:]
    e=inside_data[inside_data.shape[0]-1,:]
    t=a[0].split(' ')
    tt=t[1].split(':')
    ttt=float(tt[0])*60+float(tt[1])
    ttt=ttt/1440
    input=[ttt,a[2],a[1],a[3],a[5],a[4],a[6],b[2],b[1],b[4],b[3],c[1],c[2],d[1]]
    input=numpy.array(input)
    input=np.reshape(input, (1,14))
    input_scale=temp_scaler_x.transform(input)
    
    a= temp_model.predict(input_scale)
    y_temp_unscale=temp_scaler_y.inverse_transform(a)
    
    b=hum_model.predict(input_scale)
    y_hum_unscale=hum_scaler_y.inverse_transform(a)
    
    return  y_temp_unscale, e[2], y_hum_unscale, e[3]

def animate(xtime,xtime_ahead,temp,temp_expect,hum,hum_expect):     
    plt.clf()       
    plt.subplot(211)# 1행1열 그래프에서 1행 1열
    plt.ylim(15,30)
    plt.ylabel('temperature')
    plt.plot(xtime[-10:],temp[-10:],'ro-', label='temp', linestyle='dashed')
    plt.plot(xtime_ahead[-10:],temp_expect[-10:],'ko-',label='temp_expected', linestyle='dashed')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.grid(True)
    plt.subplot(212)# 1행1열 그래프에서 1행 1열
    plt.ylim(20,100)
    plt.ylabel('humidity')
    plt.plot(xtime[-10:],hum[-10:],'ro-', label='hum', linestyle='dashed')
    plt.plot(xtime_ahead[-10:],hum_expect[-10:],'ko-',label='hum_expected', linestyle='dashed')
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
    plt.grid(True)
    plt.pause(0.1)

def work():
    expect=load_model()
    time_ahead = datetime.datetime.now() + datetime.timedelta(minutes = 30)
    time_ahead = time_ahead.strftime("%m-%d %H:%M")
    xtime_max= datetime.datetime.now() + datetime.timedelta(minutes = 60)
    time_now = datetime.datetime.now()
    time_now = time_now.strftime("%m-%d %H:%M")
    plot_data=[time_ahead, float(expect[0]), time_now, expect[1]]
    f = open('results_ai.csv','a', newline='')
    wr = csv.writer(f)
    wr.writerow(plot_data)
    print('results')
    f.close()
    
    xtime.append(time_now)
    xtime_ahead.append(time_ahead)
    temp.append(float(expect[0]))
    temp_expect.append(float(expect[1]))
    hum.append(float(expect[3]))
    hum_expect.append(float(expect[2]))
    
    animate(xtime,xtime,temp,temp_expect,hum,hum_expect)
    


while True:
    work()
    time.sleep(60)