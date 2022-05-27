import RPi.GPIO as GPIO
import time

def led(led, temp):
	# Used to identify the pins correctly
	GPIO.setmode(GPIO.BCM)
	# Each pin needs to be setup with the mode that will be working, in this case we want the output
	GPIO.setup(23, GPIO.OUT) 
	GPIO.setup(26, GPIO.OUT)

	print(temp, "...", led)

	if(int(temp) >= 25):
		# To change the pin level, HIGH to turn it on, and LOW do turn it off
		GPIO.output(23, GPIO.LOW)

		ledz = led
		
		while True:
			if(ledz == "LED ON"):
				# Turn on the LED
				GPIO.output(23, GPIO.HIGH)

				print("LED ON")
				time.sleep(2)
				ledz = "LED OFF"

				return ledz
			elif(ledz == "LED OFF"):
				# Turn of the LED
				GPIO.output(23, GPIO.LOW)

				print("LED OFF")
				ledz = "LED ON"

				return ledz
	elif(int(temp) <= 10):
		GPIO.output(26, GPIO.LOW)

		ledz = led
		
		while True:
			if(ledz == "LED ON"):
				# Turn on the LED
				GPIO.output(26, GPIO.HIGH)

				print("LED ON")
				ledz = "LED OFF"

				return ledz
			elif(ledz == "LED OFF"):
				# Turn of the LED
				GPIO.output(26, GPIO.LOW)

				print("LED is OFF")
				ledz = "LED ON"

				return ledz
	else:
		GPIO.output(26, GPIO.LOW)

		ledz = led
		
		while True:
			if(ledz == "LED ON"):
				# Turn on the LED
				GPIO.output(26, GPIO.HIGH)

				print("LED ON")
				ledz = "LED OFF"

				return ledz
			elif(ledz == "LED OFF"):
				# Turn of the LED
				GPIO.output(26, GPIO.LOW)

				print("LED OFF")
				time.sleep(2)
				ledz = "LED ON"

				return ledz