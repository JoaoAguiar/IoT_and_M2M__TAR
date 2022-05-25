import RPi.GPIO as GPIO
import time

def led(led, temp):

	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23, GPIO.OUT)
	GPIO.setup(26, GPIO.OUT)

	print(temp, "...", led)
	if(int(temp) >= 25):
		GPIO.output(23, GPIO.LOW)
		#print("oi1")
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(23, GPIO.OUT)

		ledz = led
		while True:
			if(ledz == "LED ON"):
				GPIO.output(23, GPIO.HIGH)

				print("LED is ON QUENTE")
				time.sleep(2)
				ledz = "LED OFF"

				return ledz

			if(ledz=="LED OFF"):
				GPIO.output(23, GPIO.LOW)

				print("LED is OFF")
				#time.sleep(2)
				ledz = "LED ON"

				return ledz
	elif(int(temp) <=10):
		#print("oi2")

		GPIO.output(23, GPIO.LOW)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(26, GPIO.OUT)

		ledz = led
		
		while True:
			if(ledz == "LED ON"):
				GPIO.output(26, GPIO.HIGH)

				print("LED is ON COLD")
				return ledz

			if(ledz=="LED OFF"):
				GPIO.output(26, GPIO.LOW)

				print("LED is OFF")
				#time.sleep(2)
				ledz = "LED ON"

				return ledz
	else:
		#print("oi3") #verde mild

		GPIO.output(23, GPIO.LOW)
		GPIO.setmode(GPIO.BCM)
		GPIO.setup(26, GPIO.OUT)

		ledz = led
		
		while True:
			if(ledz == "LED ON"):
				GPIO.output(26, GPIO.HIGH)

				print("LED is ON MILD")
				#time.sleep(2)
				ledz = "LED OFF"

				return ledz

			if(ledz=="LED OFF"):
				GPIO.output(26, GPIO.LOW)

				print("LED is OFF")
				time.sleep(2)
				ledz = "LED ON"

				return ledz