import Adafruit_BBIO.PWM as PWM
import Adafruit_BBIO.GPIO as GPIO
from time import sleep
in4="P8_7"
in3="P8_9"
GPIO.setup("P8_7",GPIO.OUT)
GPIO.setup("P8_9",GPIO.OUT)
GPIO.output("P8_7",GPIO.LOW)
GPIO.output("P8_9",GPIO.LOW)
PWM.start("P8_13",100,500)
while(1):
        cmd=input("Digite o comando de controle do motor:")
        if cmd==1:
                GPIO.output("P8_7",GPIO.LOW)
                GPIO.output("P8_9",GPIO.LOW)
        elif cmd==2:
                GPIO.output("P8_7",GPIO.LOW)
                GPIO.output("P8_9",GPIO.HIGH)
		sleep(.545)
		GPIO.output("P8_7",GPIO.LOW)
                GPIO.output("P8_9",GPIO.LOW)
        elif cmd==3:
                GPIO.output("P8_7",GPIO.HIGH)
                GPIO.output("P8_9",GPIO.LOW)
       		sleep(.545)
		GPIO.output("P8_7",GPIO.LOW)
                GPIO.output("P8_9",GPIO.LOW)
	else:
                print("Comando nao valido")

