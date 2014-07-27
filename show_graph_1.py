#!/usr/bin/env python
# -*- coding: utf-8 -*-
#一画面で３つのデータを表示
import time
from pylab import *

#roop
#while True:
# 各フィールドは','で区切られており、カラム毎に分割する。
data = loadtxt('sensor_data.csv',delimiter=',',unpack=True)
tmp_x=data[0,:] #１行目取得
num = len(tmp_x)
x=arange(0,num,1)
y=data[1,:] #2行目取得
y2=data[2,:] #2行目取得
y3=data[3,:] #2行目取得

xlabel("Time", fontsize=20)
ylabel("Value", fontsize=20)
plot(x,y,marker='o',label="temperature")
plot(x,y2,marker='x',label="humid")
plot(x,y3,marker='x',label="gas")
legend(loc="upper right")
grid()

show()
#time.sleep(1)
