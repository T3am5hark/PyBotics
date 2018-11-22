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
gpio.write(PIN1, 0)
gpio.write(PIN2, 0)
gpio.write(PIN3, 0)
gpio.write(PIN4, 0)

