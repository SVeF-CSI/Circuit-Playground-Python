from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.5
cp.pixels.fill((255, 255, 255))

while True:
    if cp.button_a:
        while(cp.button_a):
            pass
        print("pressed a")
        # enter your code here that decreases brightness by 0.1
        # 0.0 is the lowest setting so it cannot go below 0.0



    if cp.button_b:
        while(cp.button_b):
            pass
        print("pressed b")
        # enter your code here that increases brightness by 0.1
        # 1.0 is the highest setting it cannot go higher than 1.0
