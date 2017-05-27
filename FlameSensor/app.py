import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

flame_pin = 4
GPIO.setup(flame_pin, GPIO.IN)

while True:
	# It should be 1 for flame detect and 0 for nothing detect, but it seems that my sensor
	# output exactly the oposit, for nothing it gives 1 and 0 for flame...
	if (not GPIO.input(flame_pin)):
		print("Flame Detected")
	else:
		print("Not Detected")
	time.sleep(1)
