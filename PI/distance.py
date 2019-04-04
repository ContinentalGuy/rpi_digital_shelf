import time
import RPi.GPIO as GPIO

class DigitalShelf():
    def __init__(self):
        # GPIO Mode (Board / BCM)
        GPIO.setmode(GPIO.BCM)

        # Disable warnings
        #GPIO.setwarnings(False)

        # Cleanup
        #GPIO.cleanup()

        # Set 6x2 GPIO pins
        self.GPIO_TRIGGER_ECHOs = [
            (0,7),
            (5,1),
            (6,12),
            (13,16),
            (19,20),
            (26, 21)
            ]

        self.GPIO_TRIGGER_ECHOs = [
            (0,7),
            (13,16),
            (19,20),
            (26,21)
            ]

        # Variable that contains number of
        # seconds delay between each sensor check
        self.delay = 1

        # Array with distances
        self.distances = []

        # Threshold config value
        self.threshold = 10

    def set_direction(self):
        # Set GPIO direction (In / Out)
        for OUT, IN in self.GPIO_TRIGGER_ECHOs:
            print('IN: {}, OUT: {}'.format(IN,OUT))
            GPIO.setup(IN, GPIO.IN)
            GPIO.setup(OUT, GPIO.OUT)

    def distance(self, trigger_pin, echo_pin):
        GPIO.output(trigger_pin, True)
        time.sleep(0.00001)
        GPIO.output(trigger_pin, False)

        pulse_start = time.time()
        pulse_stop = time.time()

        while GPIO.input(echo_pin) == 0:
            pulse_start = time.time()
        while GPIO.input(echo_pin) == 1:
            pulse_stop = time.time()

        delta = pulse_stop - pulse_start
        dist = round(delta * 17150, 2)

#        print(dist)

        if dist <= self.threshold:
            return 1
        else:
            return 0

    def check(self):
        self.set_direction()
        self.distances = []
        for trigger, echo in self.GPIO_TRIGGER_ECHOs:
            distance = self.distance(trigger, echo)
            self.distances.append(distance)
            time.sleep(self.delay)
#        print(self.distances)
        return self.distances
