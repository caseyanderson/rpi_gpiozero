#!/usr/bin/env python3

'''
button triggers countdown timer, which controls how long an led can be on


TO RUN: python3 button_timer_led.py --btn 16 --led 17 --dur 30
'''
from gpiozero import Button
from gpiozero import LED
import datetime
import time
import argparse


def countdown_timer(x, now=datetime.datetime.now):
    target = now()
    one_second_later = datetime.timedelta(seconds=1)
    for remaining in range(x, 0, -1):
        target += one_second_later
        print(datetime.timedelta(seconds=remaining-1), 'remaining', end='\r')
        time.sleep((target - now()).total_seconds())
    print('\nTIMER ended')


if __name__ == '__main__':
    try:
        parser = argparse.ArgumentParser()
        parser.add_argument("--btn", type=int, default=16,
            help="The button pin")
        parser.add_argument("--led", type=int, default=17,
            help="The LED pin")
        parser.add_argument("--dur", type=int, default=10,
            help="The timer duration (in seconds)")
        args = parser.parse_args()

        BUTTON_PIN = int(args.btn)
        LED_PIN =  int(args.led)
        DUR = int(args.dur)

        button = Button(BUTTON_PIN)
        led = LED(LED_PIN)

        prev_val = button.value

        print("ready!")

        while True:
            if button.value == True and button.value != prev_val:
                led.on()
                delay = datetime.timedelta(seconds=DUR)
                print('Starting countdown for', delay)
                countdown_timer(int(delay.total_seconds()))
                led.off()
            prev_val = button.value
            time.sleep(0.05)
    except KeyboardInterrupt:
        print("interrupted!")
        button.close()
        led.close()
