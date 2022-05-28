from adafruit_circuitplayground import cp
import time


left_light = False
right_light = False

cp.pixels.brightness=0.1

while True:
                
    if cp.button_a:
        while(cp.button_a):
            pass
        # click detected
        left_light = not left_light
        if left_light:
            right_light = False
            
        #print("left_light:",left_light)
        #print("   right_light:",right_light)

    if cp.button_b:
        while(cp.button_b):
            pass
        #click detected
        right_light = not right_light
        if right_light:
            left_light = False
        #print("right_light:",right_light)
        #print("   left_light:",left_light)

    #light operation
    if left_light:
        #start the turn signal sequence
        #limitation - while this is going on, 
        #it's not checking switch status
        for i in range(5):
            cp.pixels[i] =(228,20,10)
            time.sleep(0.1)
    #everything off
    for i in range(5): 
        cp.pixels[i] =(0,0,0)


    if right_light:
        #start the turn signal sequence
        #limitation - while this is going on, 
        #it's not checking switch status
        for i in range(9,4,-1):
            cp.pixels[i] =(228,20,10)
            time.sleep(0.1)
    #stop the turn signal sequence
    for i in range(5):
        cp.pixels[i] =(0,0,0)
