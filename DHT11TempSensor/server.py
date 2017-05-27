from time import sleep
import Adafruit_DHT

def temperature():
  SENSOR = Adafruit_DHT.DHT11
  PIN = 4
  humidity, temperature = Adafruit_DHT.read_retry(SENSOR, PIN)
  if humidity is not None and temperature is not None:
    print("Temperature: " + str(temperature))
    print("Humidity: " + str(humidity))
  else:
    print("Nu e bun")

while True:
  temperature()
  sleep(1)
