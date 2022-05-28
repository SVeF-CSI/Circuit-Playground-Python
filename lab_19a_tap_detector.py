import time
from adafruit_circuitplayground import cp

# set tapped to true if tapped once
cp.detect_taps = 1

while True:
    if cp.tapped==True:
        print("Don't bother me!")
    time.sleep(0.05)
