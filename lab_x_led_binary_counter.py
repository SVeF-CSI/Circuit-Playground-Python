import time
from adafruit_circuitplayground import cp

while True:

    #get input
    user_input = input("Enter a binary number between 1 and 10:")
    
    #convert to a decimal integer
    num = int(user_input,2)
    
    #debug
    print(num)
    
    #use num to light up LEDs
    #reset
    cp.pixels.fill((0,0,0)) 
    
    if num<=10:
        for i in range(num):
            cp.pixels[i] =(0,0,255) 
    else:
        cp.pixels.fill((255,0,0)) 
