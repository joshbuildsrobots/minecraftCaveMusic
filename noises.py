import vlc
import time
import serial
import random

feather = serial.Serial("COM4", "19200")

while True:  
    x = int(feather.readline())
    print(x)
    if x <= 15000:
        y = random.randint(0, 99)
        print(y)
        if y == 0:
            z = str(random.randint(1, 19))
            print("playing cave"+z)
            vlc.MediaPlayer("caveNoises/cave"+z).play()
            time.sleep(30*60)
            feather.reset_input_buffer()