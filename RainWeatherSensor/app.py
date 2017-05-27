import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

rain_sensor = 4

GPIO.setup(rain_sensor, GPIO.IN)

while True:
	try:
		if GPIO.input(rain_sensor) == 0:
			print("Rain!")
		else:
			print("Nothing!")
		time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()
