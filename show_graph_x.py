import serial
import time
import os
import datetime
import shlex
from pylab import *


def main():
    con=serial.Serial('/dev/ttyAMA0', 19200, timeout=10)
    print con.portstr
    con.flushInput()
    data = []
    #while 1:
    for m in xrange(10):
        lop = 20
        add1 = 0
        add2 = 0
        add3 = 0
        realtemp = 0
        humidity = 0
        humidity1 = 0
        humidity2 = 0
        realhumidity = 0
        gas = 0
        for i in range(lop):
            str=con.readline()
            #print str
            add = str
            items = shlex.split(add)
            ad1 = float(items[2].rstrip(','))
            ad2 = float(items[3].rstrip(','))
            ad3 = float(items[4])

            add1 = add1 + ad1
            add2 = add2 + ad2
            add3 = add3 + ad3

        realtemp = (1.750-add1/lop)*125
        humidity = ((add2/lop)/5-0.1515)/0.00636
        humidity1 = 0.611*10**(7.5*realtemp/(realtemp+237.3))
        humidity2 = (humidity/100)*humidity1
        realhumidity = 217*humidity2/(realtemp+273.15)*20
        gas = add3/lop*200
#output data        
        print ('temp:%.1f humidity:%.1f realhumidity:%.3f gas:%.3f' % (realtemp,humidity,realhumidity,gas))
        print add1/lop,add2/lop,add3/lop
        
        a = []
        a.append(realtemp)
        a.append(humidity)
       #a.append(realhumidity)
        a.append(gas)
       #print a
        data.append(a)
        print "[",m,"]"
    y = array(data)
    print y
#graph
    y1 = y[:,0]
    y2 = y[:,1]
    y3 = y[:,2]

    tmp_x=y[:,0]
    num = len(tmp_x)
    x=arange(0,num,1)

    subplot(311)
    ylabel("temp[c]", fontsize=15)
    plot(x,y1,'r',marker='o',label="temperature")
    legend(loc="lower right")
    #ylim(20,40) #y範囲
    grid()

    subplot(312)
    ylabel("humi[%]", fontsize=15)
    plot(x,y2,'b',marker='x',label="humid")
    legend(loc="lower right")
    #ylim(20,40)
    grid()

    subplot(313)
    xlabel("Time[s]", fontsize=15)
    ylabel("gas", fontsize=15)
    plot(x,y3,'g',marker='x',label="gas")
    legend(loc="lower right")
    #ylim(30,40)
    grid()

    show()


if __name__ == '__main__':
    main()
