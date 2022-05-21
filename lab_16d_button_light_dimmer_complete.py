from adafruit_circuitplayground import cp

cp.pixels.brightness = 0.5
cp.pixels.fill((255, 255, 255)) 

while True:
    if cp.button_a:
        while(cp.button_a):
            pass
        print("pressed a")
        if cp.pixels.brightness!=0.0:
            cp.pixels.brightness -= 0.1
        print(cp.pixels.brightness)

    if cp.button_b:
        while(cp.button_b):
            pass
        print("pressed b")
        if cp.pixels.brightness!=1.0:
            cp.pixels.brightness += 0.1
        print(cp.pixels.brightness)
    

