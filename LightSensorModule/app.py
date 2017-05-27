import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

light_pin = 4

GPIO.setup(light_pin, GPIO.IN)

while True:
	try:
		if not GPIO.input(light_pin):
			print("Day")
		else:
			print("Night")
		sleep(0.5)
	except KeyboardInterrupt:
		GPIO.cleanup()
