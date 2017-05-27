import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

microphone_sensor = 4

GPIO.setup(microphone_sensor, GPIO.IN)

while True:
	try:
		#GPIO.input(...) == 0 => LOW voltage
		#GPIO.input(...) == 1 => HIGH voltage
		if GPIO.input(microphone_sensor):
			print("Sound detected!")
		time.sleep(0.5)
	except KeyboardInterrupt:
		GPIO.cleanup()
