import serial
import time
import os
import datetime
import shlex
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(25,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)

def main():
    con=serial.Serial('/dev/ttyAMA0', 19200, timeout=10)
    print con.portstr
    con.flushInput()
#ファイル名指定
    #sreadTime = datetime.datetime.today()
    #stime = ('lifilm%s_%s_%s_%s.csv' % (sreadTime.year, sreadTime.month, sreadTime.day, sreadTime.hour))
    #print stime
    #f = open( stime , 'a')
    f = open("sensor_data.csv",'a')
    f.close()
    while 1:
        lop = 20
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
        gus = add3/lop*200
        
        print ('temp%.1f humidity%.1f realhumidity%.3f gus%.3f' % (realtemp,humidity,realhumidity,gus))
       # print add1/lop,add2/lop,add3/lop

        #f = open( stime , 'a')
        f = open("sensor_data.csv" , 'a')		
        readTime = datetime.datetime.today()
        dy=time.strftime('%H%M%S',time.localtime())
        #f.write('%s:%s.%s , %.2f, %.2f, %.3f, %.3f,  ,\n' % (readTime.hour,readTime.minute,readTime.second,realtemp,humidity,realhumidity,gus))
        f.write('%s , %.2f, %.2f, %.3f, %.3f\n' % (dy,realtemp,humidity,realhumidity,gus))
	    #f.write(str)
        f.close()
        #print ('WriteData %s' %(stime))
        #print (' ')
		
		#LED光らす
       	if realtemp > 28 :
           GPIO.output(25, GPIO.HIGH)
           print("detect:temp")
        else:
           GPIO.output(25, GPIO.LOW)
		
        if humidity > 30 :
            GPIO.output(24, GPIO.HIGH) 
            print("detect:humid")
        else:
            GPIO.output(24, GPIO.LOW)

if __name__ == '__main__':
    main()
