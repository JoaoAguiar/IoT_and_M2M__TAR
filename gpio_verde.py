from ast import Return
import RPi.GPIO as GPIO
import time

def led():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(26,GPIO.OUT)

	while True:
		#print(ledz)
		#if(ledz=="LED ON"):
		print("oi")
		GPIO.output(26,GPIO.HIGH)
		#print("LED is ON")
		#ledz= "LED ON"
		time.sleep(2)

		#ledz = "LED OFF"

		#if(ledz=="LED OFF"):
			#print("oi1")
		GPIO.output(26,GPIO.LOW)
		print("LED is OFF")
		#ledz = "LED OFF"
		time.sleep(2)
		#ledz = "LED ON"
led()

