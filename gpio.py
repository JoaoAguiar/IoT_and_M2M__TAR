import RPi.GPIO as GPIO
import time
def led():
	GPIO.setmode(GPIO.BCM)
	GPIO.setup(23,GPIO.OUT)

	while True:
		GPIO.output(23,GPIO.HIGH)
		print("LED is ON")
		ledz= "LED ON"
		time.sleep(3)

		GPIO.output(23,GPIO.LOW)
		print("LED is OFF")
		ledz = "LED OFF"
		time.sleep(3)

		return ledz
led()

