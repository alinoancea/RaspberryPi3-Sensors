import RPi.GPIO as GPIO
import time
from threading import Thread

GPIO.setmode(GPIO.BCM)

# Enable pins for IN1-4 to control step sequence

pins1 = [5, 6, 13, 19]
pins2 = [17, 22, 23, 24]

sequence = [[1,0,0,1], [0,1,0,1], [0,1,1,0], [1,0,1,0]]

# Set pin states
for i in range(4):
	GPIO.setup(pins1[i], GPIO.OUT)
	GPIO.setup(pins2[i], GPIO.OUT)

	GPIO.output(pins1[i], False)
	GPIO.output(pins2[i], False)

def backward(pins, delay, steps):
	# Function for step sequence
	def setStep(vals):
		for i, val in enumerate(vals):
			GPIO.output(pins[i], val)

	# loop through step sequence based on number of steps
	for i in range(steps):
		for seq in sequence:
			setStep(seq)
			time.sleep(delay)

def forward(pins, delay, steps):
	# Function for step sequence
	def setStep(vals):
		for i, val in enumerate(vals):
			GPIO.output(pins[i], val)

	# loop through step sequence based on number of steps
	for i in range(steps):
		for seq in sequence[::-1]:
			setStep(seq)
			time.sleep(delay)

def main():
	dreapta = Thread(target = forward, args=(pins1, 0.002, 150))
	# stanga = Thread(target = forward, args=(pins2, 0.007, 75))

	dreapta.start()
	# stanga.start()

	dreapta.join()
	# stanga.join()

main()

for i in range(4):
	GPIO.output(pins1[i], False)
	GPIO.output(pins2[i], False)
GPIO.cleanup()