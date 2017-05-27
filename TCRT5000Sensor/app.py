import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

TCRT_pin = 4

GPIO.setup(TCRT_pin, GPIO.IN)

while True:
	try:
		if not GPIO.input(TCRT_pin):
			print("Detect something!")
		else:
			print("Nothing here!")
		sleep(0.5)
	except KeyboardInterrupt:
		GPIO.cleanup()
