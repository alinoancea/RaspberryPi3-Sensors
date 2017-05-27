import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

soil_humidity_pin = 17
GPIO.setup(soil_humidity_pin, GPIO.IN)

while True:
	try:
		if not GPIO.input(soil_humidity_pin):
			print("Wet soil!")
		else:
			print("Dry soil! Wet it up! :)")
		time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()

