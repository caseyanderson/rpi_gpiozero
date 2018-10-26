#!/usr/bin/env python3

'''
button_timer.py, Fall 2018
Casey anderson

increments a counter as long as button.is_pressed returns True

'''

from gpiozero import Button
from gpiozero import LED

button = Button(16)
led = LED(17)

print("ready!")
led.on()

counter = 0

try:
    while True:
        if button.is_pressed:
            counter += 1
        print("pressed for " + str(counter))
except KeyboardInterrupt:
    print("interrupted!")
    button.close()
    led.close()
