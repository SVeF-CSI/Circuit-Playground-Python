
import board
import neopixel
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1

while True:
    #each time the for loop runs, i changes from 0 to 1 to 2 to 3...all the way to 9
    #i is used to select which LED light to turn on/off
    for i in range(10):
        #starts with red
        led[i] = (255, 0, 0)
        time.sleep(0.1)
        led[i] = (0,0,0)
        
        #then green
        led[i] = (0, 255, 0)
        time.sleep(0.1)
        led[i] = (0,0,0)
        
        #then blue
        led[i] = (0, 0, 255)
        time.sleep(0.1)
        led[i] = (0,0,0)
