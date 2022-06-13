import time 
import board 
import adafruit_hcsr04
from adafruit_circuitplayground import cp


#Sonar's trigger pin should be connected to CPX's A2 connector 
#and echo pin should be connected to CPX's A1 connector
#If not, update this with the correct pin names
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A2, echo_pin=board.A1)

while True:
    try:
        #print(sonar.distance)
        cp.play_tone(700,sonar.distance/100)
        
        
    except RuntimeError:
        print("Retrying!")
