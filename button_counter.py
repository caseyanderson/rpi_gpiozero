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
import argparse

if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--btn", type=int, default=16,
            help="The button pin")
        parser.add_argument("--led", type=int, default=17,
            help="The LED pin")
        parser.add_argument("--limit", type=int, default=5,
            help="The counter limit")
        args = parser.parse_args()

        button = Button(args.btn)
        led = LED(args.led)

        print("ready!")
        led.on()

        counter = 0
        limit = args.limit
        prev_val = button.value

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
