import board
import neopixel
import time

led = neopixel.NeoPixel(board.NEOPIXEL, 10)

led.brightness = 0.1

while True:
    for i in range(10):
        led[i] = (255, 0, 0)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (255, 128, 0)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (255, 255, 0)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (128, 255, 0)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (0, 255, 0)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (0, 255, 128)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (0, 255, 255)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (0, 128, 255)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (0, 0, 255)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (128, 0, 255)
        time.sleep(0.01)
    for i in range(10):
        led[i] = (255, 0, 255)
        time.sleep(0.04)
    for i in range(10):
        led[i] = (255, 0, 128)
        time.sleep(0.04)
