from time import sleep
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

gas_pin=4
GPIO.setup(gas_pin, GPIO.IN)
sleep(0.1)

while True:
	if not GPIO.input(gas_pin):
		print("Gas detected!")
	else:
		print("0 gas!")
	sleep(0.3)
 
