#################
# created20140625
#################


import serial
import time
import os
import datetime
import shlex
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)
GPIO.setup(25,GPIO.OUT)
def main():
    con=serial.Serial('/dev/ttyAMA0', 19200, timeout=10)
    print con.portstr
    con.flushInput()
#ファイル名指定
    sreadTime = datetime.datetime.today()
    stime = ('lifilm%s_%s_%s.csv' % (sreadTime.year, sreadTime.month, sreadTime.day))
   #print stime
    f = open( stime , 'a')
    f.close()
    while 1:
        lop =20 
        add1 = 0
        add2 = 0
        add3 = 0
        realtemp = 0
        humidity = 0
        humidity1 = 0
        humidity2 = 0
        realhumidity = 0
        gus = 0
        for i in range(lop):
            str=con.readline()
           # print str
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
        gus = add3/lop*200
        
        print ('temp%.1f humidity%.1f realhumidity%.3f gus%.3f' % (realtemp,humidity,realhumidity,gus))
        print add1/lop,add2/lop,add3/lop

        if humidity > 50 :
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            cond = "uri"
        else:
            if gus > 80 :
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(25, GPIO.LOW)
                cond = "eva"
            else:
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.HIGH)
                cond =""
        print "condition:" ,cond

    #ファイル書き込み
        f = open( stime , 'a')
        readTime = datetime.datetime.today()
        dy=time.strftime('%d/%m/%y %H:%M',time.localtime())
        f.write('%s , %.2f, %.2f, %.3f, %.3f, %s\n' % (dy,realtemp,humidity,realhumidity,gus,cond))
        f.close()
        print("-------------------------------------------")
		
if __name__ == '__main__':
    main()
