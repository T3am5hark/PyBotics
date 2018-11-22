import numpy as np
import time
import os
import pigpio

PIN1 = 19
PIN2 = 13
PIN3 = 6
PIN4 = 5

gpio = pigpio.pi()

gpio.set_mode(PIN1, pigpio.OUTPUT)
gpio.set_mode(PIN2, pigpio.OUTPUT)
gpio.set_mode(PIN3, pigpio.OUTPUT)
gpio.set_mode(PIN4, pigpio.OUTPUT)

def stepper_sequence(step):
    if step == 0:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 1)
    elif step == 1:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 1)
        gpio.write(PIN4, 1)
    elif step == 2:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 1)
        gpio.write(PIN4, 0)
    elif step == 3:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 1)
        gpio.write(PIN3, 1)
        gpio.write(PIN4, 0)
    elif step == 4:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 1)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 0)
    elif step == 5:
        gpio.write(PIN1, 1)
        gpio.write(PIN2, 1)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 0)
    elif step == 6:
        gpio.write(PIN1, 1)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 0)
    elif step == 7:
        gpio.write(PIN1, 1)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 1)
    else:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 0)

def stepper_fast(step):
    if step == 0:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 1)
    elif step == 1:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 1)
        gpio.write(PIN4, 0)
    elif step == 2:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 1)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 0)
    elif step == 3:
        gpio.write(PIN1, 1)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 0)
    else:
        gpio.write(PIN1, 0)
        gpio.write(PIN2, 0)
        gpio.write(PIN3, 0)
        gpio.write(PIN4, 0)

i = 0
while True:
    #stepper_sequence(i)
    stepper_fast(i)
    i = (i+1) % 4
    #i = (i + 1) % 8
    #time.sleep(0.01)
    time.sleep(0.001)
