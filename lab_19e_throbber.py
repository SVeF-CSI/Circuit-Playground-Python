import random
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness=0.1 #between 0 and 1

while True:
    #alt: throbber - spin 2 times
      for i in range(2):
          #head - turn on each LED as it iterate from 0 to 9
          for i in range(10):
              cp.pixels[i] =(196,0,32)
              time.sleep(0.07)
          #tail - turn off each LED as it iterate from 0 to 9
          for i in range(10):
              cp.pixels[i] =(0,0,0)
              time.sleep(0.07)
