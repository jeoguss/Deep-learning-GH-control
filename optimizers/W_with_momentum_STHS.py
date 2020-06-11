# -*- coding: utf-8 -*-
"""
Created on Thu Jan  4 11:10:05 2018

@author: BICAL-JDH
"""

import numpy as np
import matplotlib.pyplot as plt

from parameters import B1,W1_1,B2,W2_2,Xr_Xoffset,Xr_Xgain,Xr_Xmin,Y_Ymin,Y_YGain,Y_Yoffset
T=19 #target
lr=0.02 #learning rateA
stepper=0.0001
betha=0.81

def tansig_apply(n):
    return 2/(1+np.exp(-2*n))-1

def NN(W):
    x=np.array([0.700,23.0000000000000,80,600,0.5,320,18.000000000000,75.000000000000,1.0000000000000])
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


iteration=42
nY_history= np.zeros(shape=(iteration, 1))
C_history=np.zeros(shape=(iteration, 1))
VC_history=np.zeros(shape=(iteration, 1))
nW_history=np.zeros(shape=(iteration, 6))
W=np.array([0.11,	0.11,	0.101,	0.08,	0.011111,	0.07692])
nW=W
MnW=W
it=0
gam=0.91
ep=1 #ini
Vep=1
Y=NN(W)
VY=NN(W)
C=1/2*(T-Y)*(T-Y)
VC=1/2*(T-Y)*(T-Y)
A=C/2
j=0
global Vt,up_Vt
Vt=1
while(C>0.11):
    for i in range(0,6):  #step_1
       nY=NN(nW)
       mY=NN(MnW)
       VnY=NN(MnW)
       C=1/2*(T-nY)*(T-nY)
       VC=C-Vt
       nW[i]=W[i]+C*lr+ep*0.01
       MnW[i]=W[i]+VC*lr+ep*0.03
       ep=Y-nY
       Vep=VY-mY
       Y=NN(nW)
       VY=NN(MnW)
       mY=NN(MnW)
       up_Vt=gam*Vt*ep
       Vt=up_Vt
       nY_history[j,0]=nY
       C_history[j,0]=C
       VC_history[j,0]=VC
       nW_history[j]=nW
       j=j+1

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
    plt.ylim([18,28])
    plt.xlabel('Iteration')
    plt.ylabel('Temperaturen')
    plt.show()
              
    plt.plot(VC_history, 'g')
    plt.xlim([0,j-1])
    plt.xlabel('Iteration')
    plt.ylabel('Momentum Cost function')
    plt.show()










