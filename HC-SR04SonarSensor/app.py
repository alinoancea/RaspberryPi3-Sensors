import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig_pin = 23 
echo_pin = 24

print("Distance Measurement In Progress")

GPIO.setup(trig_pin,GPIO.OUT)
GPIO.setup(echo_pin,GPIO.IN)

GPIO.output(trig_pin, False)
print("Waiting For Sensor To Settle")
time.sleep(2)

GPIO.output(trig_pin, True)
time.sleep(0.00001)
GPIO.output(trig_pin, False)

while GPIO.input(echo_pin) == 0:
  pulse_start = time.time()

while GPIO.input(echo_pin)==1:
  pulse_end = time.time()

pulse_duration = pulse_end - pulse_start

distance = pulse_duration * 17150

distance = round(distance, 2)

print("Distance: " + str(distance) + "cm")

GPIO.cleanup()
