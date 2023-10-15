from adafruit_circuitplayground import cp

cp.pixels.brightness=0.1

cp.pixels[0] = (0,255,0)
cp.play_tone(262, 1) # note c

cp.pixels[1] = (0,255,0)
cp.play_tone(294, 1) # note d

cp.pixels[2] = (0,255,0)
cp.play_tone(330, 1) # note e

cp.pixels[3] = (0,255,0)
cp.play_tone(349, 1) # note f

cp.pixels[4] = (0,255,0)
cp.play_tone(392, 1) # note g

cp.pixels[5] = (0,255,0)
cp.play_tone(440, 1) # note a

cp.pixels[6] = (0,255,0)
cp.play_tone(494, 1) # note b

cp.pixels[7] = (0,255,0)
cp.play_tone(523, 1) # note c
