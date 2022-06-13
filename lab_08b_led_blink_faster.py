import board
from digitalio import DigitalInOut, Direction
import time


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

while True:
  #indent!!! - This tells Python that following line(s) are part of the while loop
  led.value = True
  time.sleep(0.2)
  
  led.value = False
  time.sleep(0.4)
