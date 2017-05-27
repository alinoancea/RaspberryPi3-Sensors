import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

laser_pin = 4
GPIO.setup(laser_pin, GPIO.OUT)

while True:
	try:
		GPIO.output(laser_pin, 1)
		time.sleep(1)
		GPIO.output(laser_pin, 0)
		time.sleep(1)
	except KeyboardInterrupt:
		GPIO.cleanup()

