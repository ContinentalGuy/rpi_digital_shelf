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
        for OUT, IN in GPIO_TRIGGER_ECHOs:
            GPIO.setup(IN, GPIO.IN)
            GPIO.setup(IN, GPIO.OUT)

    def setup_sensors(self, trigger_pin):
        GPIO.output(trigger_pin, GPIO.LOW)
        print('PIN #{} is settled up'.format(trigger_pin))

    def distance(self, trigger_pin, echo_pin):
        GPIO.output(trigger, GPIO.HIGH)
        time.sleep(0.00001)
        GPIO.output(trigger, GPIO.LOW)

        while GPIO.input(echo_pin) == 0:
            pulse_start = time.time()
        while GPIO.input(echo_pin) == 1:
            pulse_stop = time.time()
        
        delta = pulse_stop - pulse_start
        dist = round(delta * 17150, 2)
        GPIO.cleanup()
        print(dist)
        return dist
