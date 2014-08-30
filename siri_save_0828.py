# -*- coding: utf-8 -*-

import serial
import time
import os
import datetime
import shlex
import RPi.GPIO as GPIO

#$B%a!<%kAw?.(B
def sendMail():
    if cond == 'uri':
        os.system("sendmail -t < detect_uri.txt")
    elif cond == 'eva':
        os.system("sendmail -t < detect_eva.txt")

def main():

    #arduino$B$N=i4|2=(B
    ser = serial.Serial('/dev/ttyACM0', 9600)
    time.sleep(2)
    ser.write('0')

    con=serial.Serial('/dev/ttyAMA0', 19200, timeout=10)
    print con.portstr
    con.flushInput()
    sreadTime = datetime.datetime.today()
    stime = ('lifilm_data/lifilm%s_%s_%s_%s.csv' % (sreadTime.year, sreadTime.month, sreadTime.day, sreadTime.hour))
   #print stime
    f = open( stime , 'a')
    f.close()

    cont = 0
    x = 0
    global cond

    while (x < 59): 
        lop = 33
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
        gus = add3/lop*200
        
        print ('temp%.1f humidity%.1f gus%.3f' % (realtemp,humidity,gus))
        print add1/lop,add2/lop,add3/lop
        
        # $B>r7oJ,4t(B($B%j%"%k%?%$%`(B)
        if humidity > 40 :
            cond = "uri"
            ser.write('a') #arudno$B8w$i$9(B
            #os.system("sendmail -t < detect_uri.txt")
        else:
            if gus > 80 :
                cond = "eva"
                ser.write('a') #arduno$B8w$i$9(B
                #os.system("sendmail -t < detect_eva.txt")
            else:
                ser.write('0') #arudno$B;_$a$k(B
                cond ="normal"
        print "condition:" ,cond

     #1$BJ,8e$N=hM}(B
        if cont == 10 :		
            #csv$B$K%G!<%?$N=q$-9~$_(B
            f = open( stime , 'a')
            readTime = datetime.datetime.today()
            dy=time.strftime('%y/%m/%d %H:%M',time.localtime())
            f.write('%s , %.2f, %.2f, %.3f, %s\n' % (dy,realtemp,humidity,gus,cond))
            f.close()
            
            #realtime.csv$B$r99?7(B
            f = open( 'lifilm_data/realtime.csv' , 'a')
            readTime = datetime.datetime.today()
            dy=time.strftime('%y/%m/%d %H:%M',time.localtime())
            f.write('%s , %.2f, %.2f, %.3f, %s\n' % (dy,realtemp,humidity,gus,cond))
            f.close()

            print "save!"
            cont = 1
            x += 1

           # sendMail()
            
        else :
            cont += 1
            print "cont:" ,cont
            print("---------------------------------")
        print "x:", x
    #aws$B$K%U%!%$%k%"%C%W%m!<%I(B
    scp_cmd = "scp -i okn_ubu1.pem "+stime+" ubuntu@54.92.62.157:~/lifilm_data"
    os.system(scp_cmd)
    print "end"

if __name__ == '__main__':
    main()
