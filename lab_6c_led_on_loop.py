import board
from digitalio import DigitalInOut, Direction


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT

while True:
  #indent!!! - This tells Python that following line(s) are part of the while loop
  led.value = True
