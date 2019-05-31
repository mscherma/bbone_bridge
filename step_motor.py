# -*- coding: utf-8 -*-
import  Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.GPIO as GPIO
from time import sleep

in1="P8_8"
in2="P8_10"
in3="P8_12"
in4="P8_14"
tp=0.01
dr=50
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
ct=0
while(1):
	GPIO.output(in1,GPIO.LOW)
	GPIO.output(in2,GPIO.LOW)
	GPIO.output(in3,GPIO.LOW)
	GPIO.output(in4,GPIO.LOW)
	cmd=input("Digite a ação desejada"+"\n""1-SUBIR" +"\n""2-DESCER: ")
	if cmd==1:
		for i in range(dr):
			GPIO.output(in1,GPIO.HIGH)
       			GPIO.output(in2,GPIO.LOW)
        		GPIO.output(in3,GPIO.LOW)
        		GPIO.output(in4,GPIO.HIGH)
        		sleep(tp)

        		GPIO.output(in1,GPIO.LOW)
        		GPIO.output(in2,GPIO.HIGH)
        		GPIO.output(in3,GPIO.LOW)
        		GPIO.output(in4,GPIO.HIGH)
        		sleep(tp)

        		GPIO.output(in1,GPIO.LOW)
        		GPIO.output(in2,GPIO.HIGH)
        		GPIO.output(in3,GPIO.HIGH)
        		GPIO.output(in4,GPIO.LOW)
        		sleep(tp)

        		GPIO.output(in1,GPIO.HIGH)
        		GPIO.output(in2,GPIO.LOW)
        		GPIO.output(in3,GPIO.HIGH)
        		GPIO.output(in4,GPIO.LOW)
        		sleep(tp)
		
	
	if cmd==2:
		for i in range(dr):
			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
			sleep(tp)

			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.LOW)
			GPIO.output(in4,GPIO.HIGH)
			sleep(tp)

			GPIO.output(in1,GPIO.HIGH)
			GPIO.output(in2,GPIO.LOW)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
			sleep(tp)

			GPIO.output(in1,GPIO.LOW)
			GPIO.output(in2,GPIO.HIGH)
			GPIO.output(in3,GPIO.HIGH)
			GPIO.output(in4,GPIO.LOW)
			sleep(tp)
