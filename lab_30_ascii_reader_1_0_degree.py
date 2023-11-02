from adafruit_motor import servo
import time
import board
import pwmio


# create a PWMOut object on Pin A2.
# make sure the motor's orange wire is connected to A2
pwm = pwmio.PWMOut(board.A2, duty_cycle=2 ** 15, frequency=50)

#initialize the servo object with a different min_pulse and max_pulse than adafruit 
my_servo = servo.Servo(pwm, min_pulse = 500, max_pulse = 2500)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

#go to 0 degree 
my_servo.angle = 0

#give some time to move the arm 
time.sleep(1)
