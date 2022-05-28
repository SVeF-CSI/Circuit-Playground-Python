import random
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness=0.1 #between 0 and 1

while True:
    #generate a random number
    rnd = random.randint(0,9) 
    
    #random RGB color
    red = random.randint(0,255)
    green = random.randint(0,255)
    blue = random.randint(0,255)
    
    #turn on the led at location rnd
    #using random RGB values
    cp.pixels[rnd] =(red,green,blue) 
    #cp.pixels[rnd] =(255,0,0) 
    time.sleep(0.1)
    
    #turn off
    cp.pixels[rnd] =(0,0,0)   #turn it off
    time.sleep(0.1)
