from adafruit_motor import servo
from adafruit_circuitplayground import cp
import time
import board
import pwmio


# create a PWMOut object on Pin A2.
# make sure the motor's orange wire is connected to A2
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

#initial gate position - close
opengate = False;
my_servo.angle = 80


while True:
                
    if cp.button_a:
        while(cp.button_a):
            pass
        # click detected: open
        #go to 100
        print("open")
        my_servo.angle = 180
        #give it some time to get there
        time.sleep(1) 
            
        #print("left_light:",left_light)
        #print("   right_light:",right_light)

    if cp.button_b:
        while(cp.button_b):
            pass
        #click detected: close
        #go to 0
        print("close")
        my_servo.angle = 80
        #give it some time to get there
        time.sleep(1) 
