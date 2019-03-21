import time
import RPi.GPIO as GPIO

class DigitalShelf():
    def __init__(self):
        # GPIO Mode (Board / BCM)
        GPIO.setmode(GPIO.BCM)

        # Set GPIO pins
        self.GPIO_TRIGGER_ECHOs = [
            (0,7),
            (5,1),
            (6,12),
            (13,16),
            (19,20),
            (26, 21)
            ]

    def set_direction(self):
        # Set GPIO direction (In / Out)
        for OUT, IN in GPIO_TRIGGER_ECHOs:
            GPIO.setup(IN, GPIO.IN)
            GPIO.setup(IN, GPIO.OUT)

    def distance(self):
    
