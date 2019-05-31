import Adafruit_BBIO.GPIO as GPIO
outpin="P9_12"
GPIO.setup(outpin,GPIO.OUT)
from time import sleep
i=10
while i==10:
    GPIO.output(outpin,GPIO.LOW)
    sleep(.5)
    GPIO.output(outpin,GPIO.HIGH)
    sleep(.5)

