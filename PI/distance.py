import time
import RPi.GPIO as GPIO

class DigitalShelf():
    def __init__(self):
        # GPIO Mode (Board / BCM)
        GPIO.setmode(GPIO.BCM)

        # Set 6x2 GPIO pins
        self.GPIO_TRIGGER_ECHOs = [
            (0,7),
            (5,1),
            (6,12),
            (13,16),
            (19,20),
            (26, 21)
            ]

        self.distances = []

    def set_direction(self):
        # Set GPIO direction (In / Out)
        for OUT, IN in self.GPIO_TRIGGER_ECHOs:
            GPIO.setup(IN, GPIO.IN)
            GPIO.setup(OUT, GPIO.OUT)

    def setup_sensors(self, trigger_pin):
        GPIO.output(trigger_pin, GPIO.LOW)
        print('PIN #{} is settled up'.format(trigger_pin))

    def distance(self, trigger_pin, echo_pin):
        GPIO.output(trigger_pin, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigger_pin, GPIO.LOW)
        print('Start measuring distance on PIN {}'.format(trigger_pin))

        while GPIO.input(echo_pin) == 0:
            pulse_start = time.time()
        while GPIO.input(echo_pin) == 1:
            pulse_stop = time.time()
        
        delta = pulse_stop - pulse_start
        dist = round(delta * 17150, 2)
        GPIO.cleanup()
        print(dist)
        return dist

    def run(self):
        self.set_direction()
        
        '''Setting up a LOW voltage on all sensor triggers'''
        for trig, echo in self.GPIO_TRIGGER_ECHOs:
            self.setup_sensors(trig)

        infinite = True
        while infinite == True:
            for trig, echo in self.GPIO_TRIGGER_ECHOs:
                self.distance(trig, echo)
