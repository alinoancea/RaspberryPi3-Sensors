import time
import RPi.GPIO as GPIO
from threading import Thread

print("Begin setup")

GPIO.setmode(GPIO.BCM)
StepPins = [17,22,23,24]
Seq = [[1,0,0,1],
       [1,0,0,0],
       [1,1,0,0],
       [0,1,0,0],
       [0,1,1,0],
       [0,0,1,0],
       [0,0,1,1],
       [0,0,0,1]]

StepCount = len(Seq)

StepDir = 1 # 1 clockwise; -1 reverse
WaitTime = 0.0008
stop = 1

for pin in StepPins:
    GPIO.setup(pin, GPIO.OUT)
    GPIO.output(pin, False)

print("End of setup")

def run():
    StepCounter = 0
    while True and stop:
        for pin in range(0, 4):
            xpin = StepPins[pin]
            if Seq[StepCounter][pin] != 0:
                GPIO.output(xpin, True)
            else:
                GPIO.output(xpin, False)

        StepCounter += StepDir

        if (StepCounter>=StepCount):
            StepCounter = 0
        if (StepCounter<0):
            StepCounter = StepCount+StepDir

        time.sleep(WaitTime)

    print("Begin cleanup")
    for pin in StepPins:
        GPIO.output(pin, False)
    GPIO.cleanup()
    print("End of cleanup")

if __name__ == "__main__":
    thread = Thread(target = run)
    thread.start()
    try:
        thread.join()
    except KeyboardInterrupt:
        stop = 0
