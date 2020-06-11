# -*- coding: utf-8 -*-
"""
Created on Sun Apr 14 09:20:36 2019

@author: jeogus
"""

import serial
import matplotlib.pyplot as plt
import csv
import datetime
import time
import warnings
import matplotlib.animation as animation

EC_1_xlist = [0]
EC_1_ylist = []
VWC_1_xlist = [0]
VWC_1_ylist = []
Temp_1_xlist = [0]
Temp_1_ylist = []

EC_2_xlist = [0]
EC_2_ylist = []
VWC_2_xlist = [0]
VWC_2_ylist = []
Temp_2_xlist = [0]
Temp_2_ylist = []

EC_3_xlist = [0]
EC_3_ylist = []
VWC_3_xlist = [0]
VWC_3_ylist = []
Temp_3_xlist = [0]
Temp_3_ylist = []

EC_4_xlist = [0]
EC_4_ylist = []
VWC_4_xlist = [0]
VWC_4_ylist = []
Temp_4_xlist = [0]
Temp_4_ylist = []
xtime=[]

def animate1(xtime, EC_1_ylist, VWC_1_ylist,Temp_1_ylist):            
    
        plt.subplot(311)# 1행1열 그래프에서 1행 1열
        plt.ylim(-0.1,2)
        plt.ylabel('EC(dS/m)')
        plt.plot(xtime[-20:],EC_1_ylist[-20:],'ro-', linestyle='dashed', label='dS/m')
        plt.grid(True)
        plt.subplot(312)    # 1행1열 그래프에서 1행 2열    
        plt.ylim(-10,50)
        plt.ylabel('VWC(%)')
        plt.grid(True)
        plt.plot(xtime[-20:],VWC_1_ylist[-20:],'go-', linestyle='dashed', label='%')
        plt.subplot(313)    # 1행1열 그래프에서 2행 1열
        plt.ylim(-5,50)
        plt.grid(True)
        plt.ylabel('Temp(C)')
        plt.plot(xtime[-20:],Temp_1_ylist[-20:],'bo-', linestyle='dashed', label='degree C')
        time.sleep(0.1)
        
def animate(xtime, EC_1_ylist, VWC_1_ylist,Temp_1_ylist, EC_2_ylist, VWC_2_ylist,
            Temp_2_ylist,EC_3_ylist, VWC_3_ylist,Temp_3_ylist, 
            EC_4_ylist, VWC_4_ylist,Temp_4_ylist):     
        plt.clf()
        plt.subplot(311)# 1행1열 그래프에서 1행 1열
        plt.ylim(0,3)
        plt.ylabel('EC(dS/m)')
        plt.plot(xtime[-10:],EC_1_ylist[-10:],'ro-', label='Sensor-1', linestyle='dashed')
        plt.plot(xtime[-10:],EC_2_ylist[-10:],'ko-',label='Sensor-2', linestyle='dashed')
        plt.plot(xtime[-10:], EC_3_ylist[-10:],'bo-', label='Sensor-3', linestyle='dashed')
        plt.plot(xtime[-10:],EC_4_ylist[-10:],'go-',label='Sensor-4', linestyle='dashed')
        plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc='lower left', ncol=2, mode="expand", borderaxespad=0.)
        plt.grid(True)
        plt.subplot(312)    # 1행1열 그래프에서 1행 2열    
        plt.ylim(-5,80)
        plt.ylabel('VWC(%)')
        plt.grid(True)
        plt.plot(xtime[-10:],VWC_1_ylist[-10:],'ro-', label='VWC-1',linestyle='dashed')
        plt.plot(xtime[-10:],VWC_2_ylist[-10:],'ko-',label='VWC-2',linestyle='dashed')
        plt.plot(xtime[-10:], VWC_3_ylist[-10:],'bo-', label='VWC-3',linestyle='dashed')
        plt.plot(xtime[-10:],VWC_4_ylist[-10:],'go-',label='VWC-4', linestyle='dashed')
        plt.subplot(313)    # 1행1열 그래프에서 2행 1열
        plt.ylim(-10,50)
        plt.grid(True)
        plt.ylabel('Temp(C)')
        plt.plot(xtime[-10:],Temp_1_ylist[-10:],'ro-',linestyle='dashed')
        plt.plot(xtime[-10:],Temp_2_ylist[-10:],'ko-',linestyle='dashed')
        plt.plot(xtime[-10:],Temp_3_ylist[-10:],'bo-',linestyle='dashed')
        plt.plot(xtime[-10:],Temp_4_ylist[-10:],'go-',linestyle='dashed')
        #plt.show()
        plt.pause(0.1)
        time.sleep(0.5)


    #writer.writeheader()   #헤더 사용(루프용)

ser = serial.Serial('/dev/ttyACM0',9600,timeout=10)

while True:
    x=0
    while x < 6 :
        recvBytes = ser.readline()
        if len(recvBytes)<14:
            time.sleep(0.3)
        elif len(recvBytes)>17:           # 데이터를 읽고
            recvStr = recvBytes[:-5].decode()   # 문자열로 변환한 다음
            protocol = recvStr.split(':')[0]    # 프로토콜 부분을 추출]
            value = recvStr.split(':')[1]       # 데이터 부분을 추출
            value = value.split('+')
            time.sleep(0.5)
            if  x==5: 
                EC_1_ylist.append(EC_1_xlist[-1])
                EC_2_ylist.append(EC_2_xlist[-1])
                EC_3_ylist.append(EC_3_xlist[-1])
                EC_4_ylist.append(EC_4_xlist[-1])
                VWC_1_xlist[-1]=round(100*(4.3*0.000001*VWC_4_xlist[-1]*VWC_4_xlist[-1]*VWC_4_xlist[-1]-5.5*0.0001*VWC_4_xlist[-1]*VWC_4_xlist[-1]+2.92*0.01*VWC_4_xlist[-1]-5.3*0.01),2)
                VWC_2_xlist[-1]=round(100*(4.3*0.000001*VWC_2_xlist[-1]*VWC_2_xlist[-1]*VWC_2_xlist[-1]-5.5*0.0001*VWC_2_xlist[-1]*VWC_2_xlist[-1]+2.92*0.01*VWC_2_xlist[-1]-5.3*0.01),2)
                VWC_3_xlist[-1]=round(100*(4.3*0.000001*VWC_3_xlist[-1]*VWC_3_xlist[-1]*VWC_3_xlist[-1]-5.5*0.0001*VWC_3_xlist[-1]*VWC_3_xlist[-1]+2.92*0.01*VWC_3_xlist[-1]-5.3*0.01),2)
                VWC_4_xlist[-1]=round(100*(4.3*0.000001*VWC_4_xlist[-1]*VWC_4_xlist[-1]*VWC_4_xlist[-1]-5.5*0.0001*VWC_4_xlist[-1]*VWC_4_xlist[-1]+2.92*0.01*VWC_4_xlist[-1]-5.3*0.01),2)
                #VWC_1_ylist.append(100*(4.3*0.000001*VWC_1_xlist[-1]*VWC_1_xlist[-1]*VWC_1_xlist[-1]-5.5*0.0001*VWC_1_xlist[-1]*VWC_1_xlist[-1]+2.92*0.01*VWC_1_xlist[-1]-5.3*0.01))
                #VWC_2_ylist.append(100*(4.3*0.000001*VWC_2_xlist[-1]*VWC_2_xlist[-1]*VWC_2_xlist[-1]-5.5*0.0001*VWC_2_xlist[-1]*VWC_2_xlist[-1]+2.92*0.01*VWC_2_xlist[-1]-5.3*0.01))
                #VWC_3_ylist.append(100*(4.3*0.000001*VWC_3_xlist[-1]*VWC_3_xlist[-1]*VWC_3_xlist[-1]-5.5*0.0001*VWC_3_xlist[-1]*VWC_3_xlist[-1]+2.92*0.01*VWC_3_xlist[-1]-5.3*0.01))
                #VWC_4_ylist.append(100*(4.3*0.000001*VWC_4_xlist[-1]*VWC_4_xlist[-1]*VWC_4_xlist[-1]-5.5*0.0001*VWC_4_xlist[-1]*VWC_4_xlist[-1]+2.92*0.01*VWC_4_xlist[-1]-5.3*0.01))
                VWC_1_ylist.append(VWC_1_xlist[-1])
                VWC_2_ylist.append(VWC_2_xlist[-1])
                VWC_3_ylist.append(VWC_3_xlist[-1])
                VWC_4_ylist.append(VWC_4_xlist[-1])
                Temp_1_ylist.append(Temp_1_xlist[-1]) 
                Temp_2_ylist.append(Temp_2_xlist[-1])
                Temp_3_ylist.append(Temp_3_xlist[-1]) 
                Temp_4_ylist.append(Temp_4_xlist[-1])
                xtime.append(datetime.datetime.now())
                with open('test_2.csv', mode='a',newline='\n') as csv_file:
                    fieldnames = ['Time','EC-1', 'VWC-1', 'Temp-1','EC-2', 'VWC-2', 'Temp-2','EC-3', 'VWC-3','Temp-3','EC-4', 'VWC-4', 'Temp-4']
                    writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
                    #writer.writeheader() #only 1st loop
                    writer.writerow({'Time':datetime.datetime.now().strftime("%y-%m-%d-%H:%M:%S") ,'EC-1':EC_1_ylist[-1], 'VWC-1':VWC_1_ylist[-1],'Temp-1': Temp_1_ylist[-1],
                             'EC-2':EC_2_ylist[-1], 'VWC-2':VWC_2_ylist[-1], 'Temp-2': Temp_2_ylist[-1],
                             'EC-3':EC_3_ylist[-1],'VWC-3':VWC_3_ylist[-1], 'Temp-3': Temp_3_ylist[-1],
                             'EC-4':EC_4_ylist[-1], 'VWC-4':VWC_4_ylist[-1], 'Temp-4': Temp_4_ylist[-1]})
                x=x+1

                animate(xtime, EC_1_ylist, VWC_1_ylist,Temp_1_ylist,EC_2_ylist,VWC_2_ylist,Temp_2_ylist,EC_3_ylist,VWC_3_ylist,Temp_3_ylist,EC_4_ylist,VWC_4_ylist,Temp_4_ylist)
                #animate1(xtime, EC_1_ylist, VWC_1_ylist,Temp_1_ylist)
                plt.pause(0.1)               
                print('save-value')
                print('Time:', datetime.datetime.now().strftime("%y-%m-%d-%H:%M:%S"),'\n','EC-1:',EC_1_ylist[-1], 'VWC-1:',VWC_1_ylist[-1],'Temp-1:', Temp_1_ylist[-1],'\n','EC-2:',EC_2_ylist[-1], 'VWC-2:',VWC_2_ylist[-1], 'Temp-2:', Temp_2_ylist[-1],'\n',
                             'EC-3:',EC_3_ylist[-1],'VWC-3:',VWC_3_ylist[-1], 'Temp-3:', Temp_3_ylist[-1],'\n',
                             'EC-4:',EC_4_ylist[-1], 'VWC-4:',VWC_4_ylist[-1], 'Temp-4:', Temp_4_ylist[-1])
            elif protocol==('sensor-6'):  
                EC_1_xlist.append(float(value[2]))
                VWC_1_xlist.append(float(value[1])) 
                Temp_1_xlist.append(float(value[3]))
                x=x+1
            elif protocol==('sensor-7'):
                EC_2_xlist.append(float(value[2]))
                VWC_2_xlist.append(float(value[1])) 
                Temp_2_xlist.append(float(value[3]))
                x=x+1
            elif protocol==('sensor-8'):
                EC_3_xlist.append(float(value[2]))
                VWC_3_xlist.append(float(value[1])) 
                Temp_3_xlist.append(float(value[3]))
                x=x+1
            elif protocol==('sensor-9'):
                EC_4_xlist.append(float(value[2]))
                VWC_4_xlist.append(float(value[1])) 
                Temp_4_xlist.append(float(value[3]))
                x=x+1


         
                



