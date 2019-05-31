import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from time import sleep

psen="P9_15"
led="P9_12"
in1="P8_8"
in2="P8_10"
in3="P8_12"
in4="P8_14"
serpino="P9_14"
dc4="P8_7"
dc3="P8_9"
pwmdc="P8_13"
tp=0.01
dr=50
ct=2
GPIO.setup(dc4,GPIO.OUT)
GPIO.setup(dc3,GPIO.OUT)
PWM.start(serpino,3.45,25)
GPIO.setup(psen,GPIO.IN)
GPIO.setup(led,GPIO.OUT)
GPIO.setup(in1,GPIO.OUT)
GPIO.setup(in2,GPIO.OUT)
GPIO.setup(in3,GPIO.OUT)
GPIO.setup(in4,GPIO.OUT)
while(1):
    if(GPIO.input(psen)==0):
        ct=0
        for i in range(6):
            GPIO.output(led,GPIO.LOW)
            sleep(.5)
            GPIO.output(led,GPIO.HIGH)
            sleep(.5)
        GPIO.output(led,GPIO.LOW)
	PWM.set_duty_cycle(serpino,1.35)

	
        GPIO.output(dc4,GPIO.LOW)
        GPIO.output(dc3,GPIO.LOW)
        PWM.start(pwmdc,100,500)
        GPIO.output(dc4,GPIO.LOW)
	GPIO.output(dc3,GPIO.HIGH)
        sleep(.545)
        GPIO.output(dc4,GPIO.LOW)
        GPIO.output(dc3,GPIO.LOW)

	sleep(3)

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
	sleep(8)
	while(GPIO.input(psen)==0 and ct==0):
		sleep(0.1)
    if(GPIO.input(psen)==1 and ct ==0):
        ct=1
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
	sleep(4)
	PWM.set_duty_cycle(serpino,3.45)	

	GPIO.output("P8_7",GPIO.HIGH)
        GPIO.output("P8_9",GPIO.LOW)
        sleep(.545)
        GPIO.output("P8_7",GPIO.LOW)
        GPIO.output("P8_9",GPIO.LOW)





