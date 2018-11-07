#!/usr/bin/env python3

'''
button_counter.py, Fall 2018
Casey anderson

counts number of button presses

button presses are identified when button.value is True and also diff state from prev_val

'''

from gpiozero import Button
from gpiozero import LED

button = Button(16)
led = LED(17)

print("ready!")
led.on()

counter = 0
prev_val = button.value

try:
    while True:
        if button.value == True and button.value != prev_val:
            print("increment counter")
            counter += 1
        prev_val = button.value
        print("counter is " + str(counter))
except KeyboardInterrupt:
    print("interrupted!")
    button.close()
    led.close()
