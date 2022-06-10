from adafruit_motor import servo
import time
import board
import pwmio


# create a PWMOut object on Pin A2.
# make sure the motor's orange wire is connected to A2
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

#go to 0
my_servo.angle = 0
#give it some time to get there
time.sleep(1) 

#go from 0 to 180, 5 degrees at a time
for angle in range(0, 180, 5):          
  my_servo.angle = angle
  time.sleep(0.3)

#go from 180 to 0, 5 degrees at a time
for angle in range(180, 0, -5):          
  my_servo.angle = angle
  time.sleep(0.3)
