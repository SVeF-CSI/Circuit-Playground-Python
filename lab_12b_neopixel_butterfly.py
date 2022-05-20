import board
import neopixel
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1

while True:
    #down
    for i in range(5):
        led[i] = (255, 0, 0)
        time.sleep(0.1)
        led[i] = (0,0,0)
    #up
    for i in range(3,0,-1):
        led[i] = (255, 0, 0)
        time.sleep(0.1)
        led[i] = (0,0,0)
