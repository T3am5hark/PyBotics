import numpy as np
import time
import pigpio

from src.motors.servo import ServoMotor, ServoManager

gpio = pigpio.pi()       # pi1 accesses the local Pi's GPIO

MOUTH_PIN = 21
EYE_PIN = 20
print('Init Servos')
mouth_servo = ServoMotor(gpio, MOUTH_PIN)
eye_servo = ServoMotor(gpio, EYE_PIN)
time.sleep(0.25)
mouth_servo.off()
eye_servo.off()

# Range limits on mouth and eye actuator servos
MOUTH_MIN=500
MOUTH_MAX=1500
EYE_MIN=900
EYE_MAX=2100

mouth_mgr = ServoManager(mouth_servo, MOUTH_MIN, MOUTH_MAX)
eye_mgr = ServoManager(eye_servo, EYE_MIN, EYE_MAX)

mouth_mgr.random_target()
eye_mgr.random_target()

class ControlParameters(object):

    def __init__(self,
                 prob_talk_pause=0.04,
                 prob_exit_talk_pause=0.01,
                 prob_mouth_open=0.2,
                 prob_new_eye_position=0.015,
                 loop_sleep_s=0.004,
                 min_eye_speed=10, max_eye_speed=120,
                 min_mouth_speed=25, max_mouth_speed=75):
        self.prob_talk_pause=prob_talk_pause
        self.prob_exit_talk_pause = prob_exit_talk_pause
        self.prob_mouth_open=prob_mouth_open
        self.prob_new_eye_position = prob_new_eye_position
        self.loop_sleep_s=loop_sleep_s
        self.min_eye_speed=min_eye_speed
        self.max_eye_speed=max_eye_speed
        self.min_mouth_speed=min_mouth_speed
        self.max_mouth_speed=max_mouth_speed

    @property
    def eye_delta(self):
        return self.max_eye_speed-self.min_eye_speed

    @property
    def mouth_delta(self):
        return self.max_mouth_speed-self.min_mouth_speed

    def get_speed(self, min, delta):
        return min + delta*np.random.random()

    def get_eye_speed(self):
        return self.get_speed(self.min_eye_speed, self.eye_delta)

    def get_mouth_speed(self):
        return self.get_speed(self.min_mouth_speed, self.mouth_delta)

ctrl = ControlParameters()
mouth_pause = False

# Main control loop
while True:

    # Incremental track to position
    mouth_mgr.track_to_target()
    eye_mgr.track_to_target()

    if mouth_pause:
        if np.random.random() < ctrl.prob_exit_talk_pause:
            mouth_pause = False

    if mouth_mgr.is_on_target():
        # Fast mouth close
        if mouth_mgr.servo.position < 1300:
            mouth_mgr.new_target(1300, speed=150)
        elif np.random.random() < ctrl.prob_talk_pause:
            mouth_pause=True
        if np.random.random() < ctrl.prob_mouth_open and not mouth_pause:
            mouth_mgr.random_target(ctrl.get_mouth_speed())

    if eye_mgr.is_on_target():
        if (np.random.random() < ctrl.prob_new_eye_position):
            eye_mgr.random_target(ctrl.get_eye_speed())

    time.sleep(ctrl.loop_sleep_s)
