import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

pir_pin = 4

GPIO.setup(pir_pin, GPIO.IN)

while True:
	try:
		if GPIO.input(pir_pin):
			print("Motion detected!")
		else:
			print("No motion!");
		time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()
