import numpy as np
import time
import pigpio

gpio = pigpio.pi()       # pi1 accesses the local Pi's GPIO

MOUTH_PIN = 21
EYE_PIN = 20

gpio.set_mode(MOUTH_PIN, pigpio.OUTPUT)
gpio.set_mode(EYE_PIN, pigpio.OUTPUT)

MOUTH_MIN=5
MOUTH_MAX=15

EYE_MIN=9
EYE_MAX=21

cmd = 'gpio_pwm'
args = '{pin} 10000 {pos} 50'

gpio.set_servo_pulsewidth(MOUTH_PIN, 1500)
gpio.set_servo_pulsewidth(EYE_PIN, 1500)

print('Centering servos')
time.sleep(2)

gpio.set_servo_pulsewidth(MOUTH_PIN, 0)
gpio.set_servo_pulsewidth(EYE_PIN, 0)

print('Servos off... Done')
