from adafruit_motor import servo
import time
import board
import pwmio

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

#start the loop
for stop in stops:
    my_servo.angle = stop
    time.sleep(.5)
