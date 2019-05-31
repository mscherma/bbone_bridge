import Adafruit_BBIO.GPIO as GPIO
import Adafruit_BBIO.PWM as PWM
from threading import Thread
import time
import sys

BRIDGE_UP = 1 #Flag para subir a ponte
BRIDGE_DOWN = 0 #Flag para descer a ponte

BARRIER_UP = 1 #Flag para subir a cancela
BARRIER_DOWN = 0 #Flag para descer a cancela

class cSensor(Thread):
	def __init__(self, pin):
		self.pin = pin
		GPIO.setup(pin, GPIO.IN)
		Thread.__init__(self)

	def run(self):
		self.status = GPIO.input(self.pin) #0 se presença, 1 se ausência

class cLed(Thread):
	def __init__(self, pin, tt, rep):
		self.pin = pin
		self.tt = tt
		self.rep = rep
		GPIO.setup(pin, GPIO.OUT)
		Thread.__init__(self)

	def on(self):
		GPIO.output(self.pin, GPIO.HIGH)

	def off(self):
		GPIO.output(self.pin, GPIO.LOW)

	def blink(self):
		on()
		time.sleep(self.tt)
		off()
		time.sleep(self.tt)

	def run(self):
		for i in range(self.rep):
			blink(self.tt)

class cStep:
	def __init__(self, pin1, pin2, pin3, pin4):
		self.pin1 = pin1
		self.pin2 = pin2
		self.pin3 = pin3
		self.pin4 = pin4
		GPIO.setup(self.pin1, GPIO.OUT)
		GPIO.setup(self.pin2, GPIO.OUT)
		GPIO.setup(self.pin3, GPIO.OUT)
		GPIO.setup(self.pin4, GPIO.OUT)

	def spin(self, dir, tp, step_number):
		self.dir = dir
		self.tp = tp
		self.step_number = step_number

		if self.dir == BRIDGE_UP:
			for i in range(self.step_number):
				GPIO.output(self.pin1, GPIO.HIGH)
	       		GPIO.output(self.pin2, GPIO.LOW)
	        	GPIO.output(self.pin3, GPIO.LOW)
	        	GPIO.output(self.pin4, GPIO.HIGH)
	        	time.sleep(self.tp)

	        	GPIO.output(self.pin1, GPIO.LOW)
	        	GPIO.output(self.pin2, GPIO.HIGH)
	        	GPIO.output(self.pin3, GPIO.LOW)
	        	GPIO.output(self.pin4, GPIO.HIGH)
	        	time.sleep(self.tp)

	        	GPIO.output(self.pin1, GPIO.LOW)
	        	GPIO.output(self.pin2, GPIO.HIGH)
	        	GPIO.output(self.pin3, GPIO.HIGH)
	        	GPIO.output(self.pin4, GPIO.LOW)
	        	time.sleep(self.tp)

	        	GPIO.output(self.pin1, GPIO.HIGH)
	        	GPIO.output(self.pin2, GPIO.LOW)
	        	GPIO.output(self.pin3, GPIO.HIGH)
	        	GPIO.output(self.pin4, GPIO.LOW)
	        	time.sleep(self.tp)

	    if self.dir == BRIDGE_DOWN:
	    	for i in range(self.step_number):
	    		GPIO.output(self.pin1, GPIO.LOW)
				GPIO.output(self.pin2, GPIO.HIGH)
				GPIO.output(self.pin3, GPIO.LOW)
				GPIO.output(self.pin4, GPIO.HIGH)
				time.sleep(self.tp)

				GPIO.output(self.pin1, GPIO.HIGH)
				GPIO.output(self.pin2, GPIO.LOW)
				GPIO.output(self.pin3, GPIO.LOW)
				GPIO.output(self.pin4, GPIO.HIGH)
				time.sleep(self.tp)

				GPIO.output(self.pin1, GPIO.HIGH)
				GPIO.output(self.pin2, GPIO.LOW)
				GPIO.output(self.pin3, GPIO.HIGH)
				GPIO.output(self.pin4, GPIO.LOW)
				time.sleep(self.tp)

				GPIO.output(self.pin1, GPIO.LOW)
				GPIO.output(self.pin2, GPIO.HIGH)
				GPIO.output(self.pin3, GPIO.HIGH)
				GPIO.output(self.pin4, GPIO.LOW)
				time.sleep(self.tp)

class cDCMotor:
	def __init__(self, pin3, pin4, pinpwm):
		self.pin3 = pin3
		self.pin4 = pin4
		self.pinpwm = pinpwm
		GPIO.setup(self.pin3, GPIO.OUT)
		GPIO.setup(self.pin4, GPIO.OUT)
		PWM.start(self.pinpwm, 100, 500)
		GPIO.output(self.pin3, GPIO.LOW)
		GPIO.output(self.pin4, GPIO.LOW)

	def stop(self):
		GPIO.output(self.pin3, GPIO.LOW)
		GPIO.output(self.pin4, GPIO.LOW)

	def spin(self, dir):
		self.dir = dir

		if self.dir == BARRIER_UP:
			GPIO.output(self.pin3, GPIO.LOW)
			GPIO.output(self.pin4, GPIO.HIGH)

		if self.dir == BARRIER_DOWN:
			GPIO.output(self.pin3, GPIO.HIGH)
			GPIO.output(self.pin4, GPIO.LOW)

class cTowerPro:
	def __init__(self, pinpwm):
		self.pinpwm = pinpwm
		PWM.start(self.pinpwm, 1.35, 25)

	def open(self):
		PWM.set_duty_cycle(self.pinpwm, 3.45)

	def close(self):
		PWM.set_duty_cycle(self.pinpwm, 1.45)

GPIO.cleanup() #Reset all pins

sensor = cSensor("P9_15")
led = cLed("P9_12", 0.5, 6)

cancela_dc = cDCMotor("P8_7", "P8_9")
cancela_servo = cTowerPro("P9_14")
motores_ponte = cStep("P8_8", "P8_10", "P8_12", "P8_14")

bridge_status = 0 #0 pra fechada, 1 pra aberta

class cMain(Thread):
	def __init__(self):
		Thread.__init__(self)

	def __run__(self):
		if sensor.status == 0 and bridge_status == 0:
			sys.stdout.write("Opening!\n")
			led.start()
			cancela_servo.close()
			cancela_dc.spin(BARRIER_DOWN)
			time.sleep(.545)
			cancela_dc.stop()
			time.sleep(3)
			motores_ponte.spin(BRIDGE_UP)
			bridge_status = 1
		elif sensor.status == 1 and bridge_status == 1:
			sys.stdout.write("Closing!\n")
			motores_ponte.spin(BRIDGE_DOWN)
		elif sensor.status == 0 and bridge_status == 0:
			while(sensor.status == 0):
				sys.stdout.write("Waiting!\n")


main_thread = cMain()

while(True):
	sensor.run()
	main_thread.run()