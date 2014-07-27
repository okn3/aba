#!/usr/bin/env python
# -*- coding: utf-8 -*-
#3画面で３つのデータを表示
import time
from pylab import *

data = loadtxt('sensor_data.csv',delimiter=',',unpack=True)

tmp_x=data[0,:]
num = len(tmp_x)
x=arange(0,num,1)

y1=data[1,:] 
y2=data[2,:]
y3=data[3,:]

subplot(311)
ylabel("temp[c]", fontsize=15)
plot(x,y1,'r',marker='o',label="temperature")
legend(loc="upper right")
grid()

subplot(312)
ylabel("humi[%]", fontsize=15)
plot(x,y2,'b',marker='x',label="humid")
legend(loc="upper right")
grid()


subplot(313)
xlabel("Time[s]", fontsize=15)
ylabel("gas", fontsize=15)
plot(x,y3,'g',marker='x',label="gas")
legend(loc="upper right")
grid()

show()
