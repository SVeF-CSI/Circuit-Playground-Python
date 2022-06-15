import board
from digitalio import DigitalInOut, Direction, Pull
import time
import neopixel

#led is now referring to the neopixel led & not the D13 led
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.1

#switch 
switch = DigitalInOut(board.SLIDE_SWITCH)
switch.direction = Direction.INPUT
switch.pull = Pull.UP

while True:
    if (switch.value==True):
        #red
        led[0] = (255, 0, 0)
    else:
        #green
        led[0] = (0, 255, 0)
