import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

tilt_pin = 4
GPIO.setup(tilt_pin, GPIO.IN)

while True:
	try:
		if not GPIO.input(tilt_pin):
			print("Tilt detected!")
		else:
			print("No tilt!")
		sleep(0.5)
	except KeyboardInterrupt:
		GPIO.cleanup()
