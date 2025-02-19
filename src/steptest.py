

import stepper
import neopixel
import machine
from time import sleep
from time import localtime
from chars import chars
import os
import ntptime
# import wifimgr
from wifi_functions import connect
import ntptime

np = neopixel.NeoPixel(machine.Pin(8, machine.Pin.OUT), 10)
 
def setled(digit, digitcol, val):
    print(val, end='')
    if(digit == 0):
        col = digitcol
    elif digit == 1:
        col = digitcol + 7
    elif digit == 2:
        col = digitcol + 15
    elif digit == 3:
        col = digitcol + 22
    else:
        print("Ooops", )
    
    
    chip = col // 3
    pixel = col % 3
    current = np[chip]
    new = list(current)
    if pixel == 0:
        new[1] = val * 255
    elif pixel == 1:
        new[0] = val * 128
    elif pixel == 2:
        new[2] = val * 255
    else:
        print("oops")
    np[chip] = new
    np.write()


import network
import time


time.sleep(1)
connect()
time.sleep(1)

try:
    ntptime.settime()
except OSError as error:
    print("NTP Timeout")
    machine.reset()


# Define the stepper motor pins
IN1 = 21
IN2 = 20
IN3 = 10
IN4 = 9

# Initialize the stepper motor
stepper_motor = stepper.HalfStepMotor.frompins(IN1, IN2, IN3, IN4)
stepper_motor.stepms = 5
sleep_time = 0.5
columns = 6
rows = 10
row_height = 50
reveal_height = 1000
ndigits = 4
#steps = (4096-(rows*row_height)-reveal_height) # Does full rotate
steps = 1000


try:
    while True:
        gmt = localtime()

        hour = gmt[3]
        minutes = gmt[4]
        print(hour, minutes)
        digits = (str(hour // 10), str(hour % 10), str(minutes // 10), str(minutes % 10))
        print(digits)
    
        for r in range(rows):
            for d in range(ndigits):
                for c in range(columns):
                    cc = chars[digits[d]][r][c]
                    if chars[digits[d]][r][c] == '#':
                             setled(d, c, 1)
                    else:
                             setled(d, c, 0)
            print()
            sleep(sleep_time)
            stepper_motor.step(row_height)
        print()
        # Switch all leds off
        for n in range(10):
            np[n] = (0,00,00)
        np.write()
        #Rotate to reveal
        stepper_motor.step(reveal_height)
        sleep(60)
        stepper_motor.step(steps)
        
        
    
        

    
except KeyboardInterrupt:
    print('Keyboard interrupt')
