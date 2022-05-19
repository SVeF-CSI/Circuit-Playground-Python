import board
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 1)

led.brightness = 0.1

while True:
    led[0] = (255, 0, 0)
