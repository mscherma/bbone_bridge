
# -*- coding: utf-8 -*-
import  Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep
GPIO.setup("P9_12",GPIO.OUT)
GPIO.setup("P9_15",GPIO.OUT)
PWM.start("P9_14", 100,1000)
GPIO.output("P9_12",GPIO.LOW)
GPIO.output("P9_15",GPIO.LOW)
while(1):
        cmd=input("Digite a ação da cancela(1:abrir;2:fechar)")
        GPIO.output("P9_12",GPIO.LOW)
        GPIO.output("P9_15",GPIO.HIGH)
        sleep(15)
        PWM.stop("P9_14")

