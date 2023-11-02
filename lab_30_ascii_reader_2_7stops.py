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
#my_servo = servo.Servo(pwm)

#go to 0 degree 
my_servo.angle = 0

#give some time to move the arm 
time.sleep(1)

#firs stop
my_servo.angle = 12
time.sleep(.5)

#second stop
my_servo.angle = 37
time.sleep(.5)

#3rd stop
my_servo.angle = 63
time.sleep(.5)

#4th
my_servo.angle = 90
time.sleep(.5)

#5th
my_servo.angle = 115
time.sleep(.5)

#6th
my_servo.angle = 145
time.sleep(.5)

#7th
my_servo.angle = 167
time.sleep(.5)
