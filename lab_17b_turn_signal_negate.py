from adafruit_circuitplayground import cp

left_light = False
right_light = False

while True:
    if cp.button_a:
        while(cp.button_a):
            pass
        # click detected
        left_light = not left_light #negate



    if cp.button_b:
        while(cp.button_b):
            pass
        #click detected
        right_light = not right_light #negate

