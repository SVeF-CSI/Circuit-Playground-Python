import board
from digitalio import DigitalInOut, Direction, Pull
import time


led = DigitalInOut(board.LED)
led.direction = Direction.OUTPUT


switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    if (switch.value):
        led.value = True
    else:
        led.value = False
