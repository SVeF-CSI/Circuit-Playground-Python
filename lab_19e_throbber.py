from adafruit_circuitplayground import cp

cp.pixels.brightness=0.1 #between 0 and 1

while True:

    #head - turn on each LED as it iterates from 0 to 9
    for i in range(10):
        cp.pixels[i] =(255,0,0)
        time.sleep(0.1)
    
    #tail - turn off each LED as it iterates from 0 to 9
    for i in range(10):
        cp.pixels[i] =(0,0,0)
        time.sleep(0.1)
