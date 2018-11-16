#!/usr/bin/env python3

'''
button_counter.py, Fall 2018
Casey anderson

counts number of button presses

button presses are identified when button.value is True and also diff state from prev_val

'''

from gpiozero import Button
from gpiozero import LED
from time import sleep

button = Button(16)
led = LED(17)

print("ready!")
led.on()

counter = 0
limit = 5
prev_val = button.value

try:
    while True:
        if button.value == True and button.value != prev_val:
            counter += 1
            print("counter is " + str(counter))
            if counter == limit:
                print("counter at limit, reset to 0")
                counter = 0
        prev_val = button.value
        sleep(0.01)
except KeyboardInterrupt:
    print("interrupted!")
    button.close()
    led.close()
