import board
import analogio
import time

light = analogio.AnalogIn(board.LIGHT)

while True:
    print(light.value)
    time.sleep(1)
