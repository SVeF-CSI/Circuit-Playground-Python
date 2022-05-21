import time
from adafruit_circuitplayground import cp


while True:
    print(cp.temperature * 1.8 + 32) #convert to F
    time.sleep(1)

