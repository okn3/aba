# -*- coding: utf-8 -*-

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
    sreadTime = datetime.datetime.today()
    stime = ('lifilm%s_%s_%s_%s_%s.csv' % (sreadTime.year, sreadTime.month, sreadTime.day, sreadTime.hour,sreadTime.minute))
   #print stime
    f = open( stime , 'a')
    f.close()
    cont = 0
    #while 1:
    for x in range(10):
       # lop = 35
        lop = 10
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
            try:
#            print str #test
                add = str
                items = shlex.split(add)
                print items #test
                ad1 = float(items[2].rstrip(','))
                ad2 = float(items[3].rstrip(','))
                ad3 = float(items[4])
            
                add1 = add1 + ad1
                add2 = add2 + ad2
                add3 = add3 + ad3
            except:
                print "detect error"

        realtemp = (1.750-add1/lop)*125
        humidity = ((add2/lop)/5-0.1515)/0.00636
#real humi NG
     #   humidity1 = 0.611*10**(7.5*realtemp/(realtemp+237.3))
     #   humidity2 = (humidity/100)*humidity1
     #   realhumidity = 217*humidity2/(realtemp+273.15)*20
        gus = add3/lop*200
        
        #print ('temp%.1f humidity%.1f realhumidity%.3f gus%.3f' % (realtemp,humidity,realhumidity,gus))
        print ('temp%.1f humidity%.1f gus%.3f' % (realtemp,humidity,gus))
        print add1/lop,add2/lop,add3/lop

        if humidity > 40 :
            GPIO.output(24, GPIO.HIGH)
            GPIO.output(25, GPIO.LOW)
            cond = "uri"
            os.system("sendmail -t < detect_uri.txt")
        else:
            if gus > 80 :
                GPIO.output(23, GPIO.HIGH)
                GPIO.output(25, GPIO.LOW)
                cond = "eva"
                os.system("sendmail -t < detect_eva.txt")
            else:
                GPIO.output(23, GPIO.LOW)
                GPIO.output(24, GPIO.LOW)
                GPIO.output(25, GPIO.HIGH)
                cond ="normal"
        print "condition:" ,cond
        
        #if cont == 10 :		
        #if cont == 3 :		
        f = open( stime , 'a')
        readTime = datetime.datetime.today()
        dy=time.strftime('%y/%m/%d %H:%M.%S',time.localtime())
        f.write('%s , %.2f, %.2f, %.3f, %.3f, %s\n' % (dy,realtemp,humidity,realhumidity,gus,cond))
        f.close()
        print "save!"
        #    cont = 1
        #else :
        #    cont += 1
        #print "cont:" ,cont
        print("-------------------------------------------")
        #print x

    else:
        scp_cmd = "scp -i okn_ubu1.pem "+stime+" ubuntu@54.92.62.157:~/lifilm_data"
        os.system(scp_cmd)
        print "end"

if __name__ == '__main__':
    main()
