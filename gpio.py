import RPi.GPIO as GPIO
import time

def led(led, temp):
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(26, GPIO.OUT)

	if(int(temp) >= 25):
		GPIO.output(23, GPIO.LOW)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(23, GPIO.OUT)

		ledz = led

		while True:
			if(ledz == "LED ON"):
				GPIO.output(23, GPIO.HIGH)

				time.sleep(2)
				ledz = "LED OFF"

				return ledz
			if(ledz=="LED OFF"):
				GPIO.output(23, GPIO.LOW)

				print("LED is OFF")
				ledz = "LED ON"

				return ledz
	elif(int(temp) <= 10):
		GPIO.output(23, GPIO.LOW)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(26, GPIO.OUT)

		ledz = led
		
		while True:
			if(ledz == "LED ON"):
				GPIO.output(26, GPIO.HIGH)

				return ledz
			if(ledz=="LED OFF"):
				GPIO.output(26, GPIO.LOW)

				print("LED is OFF")
				ledz = "LED ON"

				return ledz
	else:
		GPIO.output(23, GPIO.LOW)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(26, GPIO.OUT)

		ledz = led
		
		while True:
			if(ledz == "LED ON"):
				GPIO.output(26, GPIO.HIGH)

				ledz = "LED OFF"

				return ledz
			if(ledz=="LED OFF"):
				GPIO.output(26, GPIO.LOW)

				print("LED is OFF")
				ledz = "LED ON"

				return ledz