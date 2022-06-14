from adafruit_circuitplayground import cp
import random
import time

cp.pixels.brightness=0.1

while True:
    
    #button_b rolls a die
    if cp.button_b==True:
        while(cp.button_b==True):
            pass
        # click detected
        roll = random.randint(0,5)
        print("You rolled:",roll)
        
        #reset 
        for i in range(6):
            cp.pixels[i] =(0,0,0)
        
        #light up
        for i in range(roll+1):
            cp.pixels[i] =(0,0,255)
            time.sleep(0.05)
