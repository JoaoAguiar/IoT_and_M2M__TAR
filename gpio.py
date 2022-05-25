from ast import Return
import RPi.GPIO as GPIO
import time
def led(aux):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23,GPIO.OUT)
	ledz = aux
	while True:
		print(ledz)
		if(ledz=="LED ON"):
			print("oi")
			GPIO.output(23,GPIO.HIGH)
			#print("LED is ON")
			ledz= "LED ON"
			time.sleep(3)

			ledz = "LED OFF"
			return ledz

		if(ledz=="LED OFF"):
			print("oi1")
			GPIO.output(23,GPIO.LOW)
			#print("LED is OFF")
			ledz = "LED OFF"
			time.sleep(3)
			print("sle")
			ledz = "LED ON"
			return ledz
#led()

