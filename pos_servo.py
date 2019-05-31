
import Adafruit_BBIO.PWM as PWM
serpino="P9_14"
PWM.start(serpino,1.35,25)
while(1):
        dutycycle=input("Digite a posicao:")
        PWM.set_duty_cycle(serpino,dutycycle)


