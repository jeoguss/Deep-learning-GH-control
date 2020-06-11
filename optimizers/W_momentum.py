# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:10:05 2018

@author: BICAL-JDH
"""

import numpy as np
import matplotlib.pyplot as plt
from parameters import B1,W1_1,B2,W2_2,Xr_Xoffset,Xr_Xgain,Xr_Xmin,Y_Ymin,Y_YGain,Y_Yoffset
T=21#target
lr=0.02 #learning rateA
stepper=0.0001
betha=0.81

def tansig_apply(n):
    return 2/(1+np.exp(-2*n))-1

def NN(W):
    x=np.array([0.630,23.2000000000000,42,800,1,321,25.000000000000,75.000000000000,1.0000000000000])
    X=np.concatenate((x, W))
    Xr=X-Xr_Xoffset
    Xr=Xr*Xr_Xgain
    Xr=Xr+Xr_Xmin
    # Layer 1#
    Ax=np.dot(W1_1,Xr)
    Ax=Ax+B1
    A1=tansig_apply(Ax)
    #Layer 2#
    Ax2=np.dot(W2_2,A1)
    Ax2=Ax2+B2
    Y=Ax2-Y_Ymin
    Y=Y/Y_YGain
    Y=Y+Y_Yoffset
    return Y


iteration=60
nY_history= np.zeros(shape=(iteration, 1))
C_history=np.zeros(shape=(iteration, 1))
nW_history=np.zeros(shape=(iteration, 6))
W=np.array([0.91,	0.91,	1,	0.98,	0.951111,	0.95692])
nW=W
it=0
ep=1 #ini
Y=NN(W)
C=1/2*(T-Y)*(T-Y)
A=C/2
j=0


while(C>0.11):
    for i in range(0,6):  #step_1
       nY=NN(nW)
       C=1/2*(T-nY)*(T-nY)
       nW[i]=W[i]+C*lr+ep*0.03
       nY=NN(W)
       ep=Y-nY
       nY_history[j,0]=nY
       C_history[j,0]=C
       nW_history[j]=nW
       j=j+1
       Y=nY
       if (j==iteration-1):
           break
       if (nW[i]>0.95):
           nW[i]=1.0
           i = i+1
       if (abs(ep) < 0.5):
           i = i+1
           print(nW)
           print(C)
           print(nY)
           print(ep)
           print(i)
           print(j)
           if (i==6):
               i=0       
               
    plt.plot(C_history, 'y')
    plt.xlim([0,j-1])
    plt.xlabel('Iteration')
    plt.ylabel('Cost function')
    plt.show()

    plt.plot(nY_history, 'r')
    plt.xlim([0,j-2])
    plt.ylim([18,30])
    plt.xlabel('Iteration')
    plt.ylabel('Temperaturen')
    plt.show()
    
    plt.plot(nW_history, 'b')
    plt.xlim([0,j-2])
    plt.ylim([0,1.3])
    plt.xlabel('Iteration')
    plt.ylabel('Opening ratio')
    plt.show()
              
           










