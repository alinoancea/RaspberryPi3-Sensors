import RPi.GPIO as GPIO, time

GPIO.setmode(GPIO.BCM)

def RCtime (PiPin):
    measurement = 0
    GPIO.setup(PiPin, GPIO.OUT)
    GPIO.output(PiPin, GPIO.LOW)
    time.sleep(0.1)

    GPIO.setup(PiPin, GPIO.IN)
    # Count loops until voltage across
    # capacitor reads high on GPIO
    while GPIO.input(PiPin) == GPIO.LOW:
        measurement += 1

    return measurement

while True:
    print(RCtime(14))
