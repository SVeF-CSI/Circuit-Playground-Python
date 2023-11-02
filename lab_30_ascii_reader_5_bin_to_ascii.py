from adafruit_motor import servo
import time
import board
import pwmio


#copy code from your IR servo lam
import board
from digitalio import DigitalInOut, Direction, Pull
import time

#define ir as a digital device connected to A3 <----change
ir = DigitalInOut(board.A3) 

#configure ir as INPUT
#Remember, you're going to READ the sensor output in CPX)
ir.direction = Direction.INPUT



# create a PWMOut object on Pin A2.
# make sure the servo's OUT is connected to A2
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

#initialize the servo object with a different min_pulse and max_pulse than adafruit 
my_servo = servo.Servo(pwm, min_pulse = 500, max_pulse = 2500)

#init servo
#always move to 0 before the loop
my_servo.angle = 0
#give some time to move the arm 
time.sleep(1)

#define stops as a list
stops = [14, 39, 63, 85, 107, 133, 159]


#save values of each "pie" here
reading=""

#start the loop
#first stop
for stop in stops:
    my_servo.angle = stop
    time.sleep(.5)
    
    #read the IR sensor
    #print(ir.value) prints black->True, white = False
    
    #let's store True/False as 1 or 0 as string such as "1010111"
    #where black = 1 and white is 0 
    
    #cover string concatenation
    
    if ir.value==True:
        reading+="1"
    else:
        reading+="0"

    #show me value
    print(reading)

#convert this to an integer
#cover binary to decimal conversion
#python has a function to do this easily
num = int(reading,2) #convert reading in decimal to integer
print(num)

#convert decimal num to an ascii char value 
#again Python has a function to do this
ascii = chr(num) #convert decimal num to ascii character
print(ascii)




#after the loop, move the servo back to 0
my_servo.angle = 0
#give some time to move the arm 
time.sleep(1)
