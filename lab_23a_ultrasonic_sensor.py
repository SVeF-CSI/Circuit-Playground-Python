import time 
import board 
import adafruit_hcsr04


#Sonar's trigger pin should be connected to CPX's A0 connector 
#and echo pin should be connected to CPX's A1 connector
#If not, update this with the correct pin names
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.A0, echo_pin=board.A1)

while True:
    try:
        print(sonar.distance)
    except RuntimeError:
        print("Retrying!")
    time.sleep(2)
