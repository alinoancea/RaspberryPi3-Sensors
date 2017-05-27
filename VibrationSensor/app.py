import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

vibration_pin = 4

GPIO.setup(vibration_pin, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)

sleep(0.5)

while True:
	if GPIO.input(vibration_pin) == 1:
		print("Vibration detected!")
	else:
		print("No vibration!")
	sleep(0.3)
