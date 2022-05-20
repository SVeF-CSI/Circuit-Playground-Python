import board
import analogio
import time
import neopixel

led = neopixel.NeoPixel(board.NEOPIXEL, 10)
led.brightness = 0.1

light = analogio.AnalogIn(board.LIGHT)

while True:
    print(light.value)
    
    if light.value < 3000:
        #turn on NEOPIXEL LEDs 3-9 if value is < 3000
        for i in range(3,10):
            led[i] = (255, 255, 255)
    else: 
        #don't forget to turn them off
        for i in range(3,10):
            led[i] = (0, 0, 0)
            
    time.sleep(1)

# One problem with this algorithm is that if lights are turned on, don't keep turning them on.
# You should only change the state of LED lights when it changes from dark to light and vise versa. 
