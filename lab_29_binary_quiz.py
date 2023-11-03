import time
import random
from adafruit_circuitplayground import cp

while True:

    #get a random number between 1 and 10
    rnd = random.randint(1,10)
    
    #debug
    print(rnd)
    
    #use rnd to light up LEDs
    #reset
    cp.pixels.fill((0,0,0)) 
    
    for i in range(rnd):
        cp.pixels[i] =(255,255,0) #YELLOW

    
    #get input
    user_input = input("What is your guess?")
    
    #convert to a decimal integer
    num = int(user_input,2)
    
    #debug
    print(num)
    
    #if num == rnd:
        #print('correct')
    #else:
        #print('incorrect')
    #blink
    for i in range(3):
        cp.pixels.fill((0,0,0)) #reset
        time.sleep(.1)
        if num == rnd:
            cp.pixels.fill((0,255,0)) #green
        else:
            cp.pixels.fill((255,0,0)) #red
        time.sleep(.1)
    cp.pixels.fill((0,0,0)) #reset
    time.sleep(.1)
