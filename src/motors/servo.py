import numpy as np
import pigpio

class ServoMotor(object):
    def __init__(self, gpio, pin_number, initial_pos=1500):
        self.gpio = gpio
        self.pin = pin_number
        self.gpio.set_mode(self.pin, pigpio.OUTPUT)
        self.position = 1500
        self.set_pulsewidth(initial_pos)

    def set_pulsewidth(self, pos=1500):
        if pos < 500 or pos > 2500:
            self.off()
        else:
            self.position = pos
            self.gpio.set_servo_pulsewidth(self.pin, self.position)

    def off(self):
        self.gpio.set_servo_pulsewidth(self.pin, 0)


class ServoManager(object):
    def __init__(self, servo, min_pos=500, max_pos=2500):
        self.servo = servo
        self.min_pos = min_pos
        self.max_pos = max_pos
        self._target = servo.position
        self._speed = 30
        self._hold_target = False

    def steer_min(self):
        self.servo.set_pulsewidth(self.min_pos)

    def steer_max(self):
        self.servo.set_pulsewidth(self.max_pos)

    def steer_random(self):
        self.servo.set_pulsewidth(self.random_position())

    def servo_off(self):
        self.servo.off()

    def new_target(self, target, speed=30, hold_target = False):
        self._target = np.maximum(np.minimum(target, self.max_pos), self.min_pos)
        self._speed = speed
        self._hold_target = hold_target

    def random_target(self, speed=30, hold_target = False):
        self.new_target(self.random_position(), speed=speed, hold_target=hold_target)

    def random_position(self):
        new_target = int(np.random.random()*(self.max_pos-self.min_pos)+self.min_pos)
        #print("tgt =", new_target)
        return new_target

    def track_to_target(self):
        if self.servo.position < self._target:
            self.servo.set_pulsewidth(self.servo.position+np.minimum(self._speed, self._target-self.servo.position))
        elif self.servo.position > self._target:
            self.servo.set_pulsewidth(self.servo.position-np.minimum(self._speed, self.servo.position-self._target))
        elif not self._hold_target:
            if self.servo.position != 0:
                self.servo_off()

    def is_on_target(self):
        if self._target == self.servo.position:
            return True
        return False

