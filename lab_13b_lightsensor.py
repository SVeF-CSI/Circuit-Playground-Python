import board
import analogio
import time

light = analogio.AnalogIn(board.LIGHT)

print("startplot:","Light Sensor")

while True:
    print(light.value)
    time.sleep(1)
