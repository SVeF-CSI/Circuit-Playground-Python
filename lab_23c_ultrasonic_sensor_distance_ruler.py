import time 
import board 
import adafruit_hcsr04
from adafruit_circuitplayground import cp

#set pixels brightness to 10%
cp.pixels.brightness=0.1

#Sonar's trigger pin should be connected to CPX's A0 connector 
#and echo pin should be connected to CPX's A1 connector
#If not, update this with the correct pin names
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)

while True:
    try:
        #get distance
        distance = sonar.distance
        
        #convert to inch
        distance = 0.393701 * distance
        
        #round to integer - math ceiling function could be used as well
        distance = round(distance)
        
        #cap distance at 10 (the range function will exclude 10)
        if distance > 10:
            distance = 10 #cap distance at 10
            
        #debug
        #print(distance)
        
        #lit up
        for i in range(distance):
            cp.pixels[i]=(255,0,0)
        for i in range(distance,10): #fill the rest with no color
            cp.pixels[i]=(0,0,0)
        
    except RuntimeError:
        print("Retrying!")
        
    time.sleep(0.5)
