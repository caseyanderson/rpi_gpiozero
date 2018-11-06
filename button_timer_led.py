#!/usr/bin/python3

'''
button triggers countdown timer, which controls how long an led can be on


arg1 is BUTTON_PIN
arg2 is LED_PIN
arg3 is DUR (in seconds)

TO RUN: python3 button_timer_led.py BUTTON_PIN LED_PIN DUR
i.e. python3 button_timer_led.py 16 17 90


'''
from gpiozero import Button
from gpiozero import LED
import datetime
import time
import sys


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
        BUTTON_PIN = int(sys.argv[1])
        LED_PIN =  int(sys.argv[2])
        DUR = int(sys.argv[3])

        button = Button(BUTTON_PIN)
        led = LED(LED_PIN)

        prev_val = button.value

        print("ready!")

        while True:
            if button.value == True and not prev_val:
                led.on()
                delay = datetime.timedelta(seconds=DUR)
                print('Starting countdown for', delay)
                countdown_timer(int(delay.total_seconds()))
                led.off()
            prev_val = button.value
    except KeyboardInterrupt:
        print("interrupted!")
        button.close()
        led.close()

