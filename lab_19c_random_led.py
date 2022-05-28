import random
import time
from adafruit_circuitplayground import cp

cp.pixels.brightness=0.3

while True:
    #generate a random number
    rnd = random.randint(1,9) #fill in the blank
	
	#turn on (keep this red for now)
    cp.pixels[rnd] =(255,0,0)
    time.sleep(0.1)
    
    #turn off
    cp.pixels[rnd] =(0,0,0)   #turn it off
    time.sleep(0.1)
