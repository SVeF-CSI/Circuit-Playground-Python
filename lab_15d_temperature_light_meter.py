import time
from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.1

while True:
    
    temp = cp.temperature * 1.8 + 32
    
    if temp < 70:
        cp.pixels.fill((0, 0, 255))
    elif temp < 71:
        cp.pixels.fill((0, 85, 255))
    elif temp < 72:
        cp.pixels.fill((0, 170, 255))
    elif temp < 73:
        cp.pixels.fill((0, 255, 255))
    elif temp < 74:
        cp.pixels.fill((0, 255, 170))
    elif temp < 75:
        cp.pixels.fill((0, 255, 85))
    elif temp < 76:
        cp.pixels.fill((0, 255, 0))
    elif temp < 77:
        cp.pixels.fill((85, 255, 0))
    elif temp < 78:
        cp.pixels.fill((170, 255, 0))
    elif temp < 79:
        cp.pixels.fill((255, 255, 0))
    elif temp < 80:
        cp.pixels.fill((255, 170, 0))
    elif temp < 81:
        cp.pixels.fill((255, 85, 0))
    elif temp < 82:
        cp.pixels.fill((255, 0, 0))
    elif temp < 83:
        cp.pixels.fill((255, 0, 85))
    elif temp < 84:
        cp.pixels.fill((255, 0, 170))
    else:
        cp.pixels.fill((255, 0, 255))
    
    time.sleep(0.5)
