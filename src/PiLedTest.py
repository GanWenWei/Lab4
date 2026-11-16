import RPi.GPIO as GPIO #import RPi.GPIO module
from time import sleep
from hal import hal_led as led

def init():
    GPIO.setmode(GPIO.BCM) #choose BCM mode
    GPIO.setwarnings(False)
    GPIO.setup(22,GPIO.IN) #set GPIO 22 as input
    GPIO.setup(24,GPIO.OUT)


def read_slide_switch():
    ret = 0

    if GPIO.input(22):
        ret = 1

    return ret

def set_output(led, level):
    GPIO.output(24, level)

init()

if read_slide_switch() == 0:
        for i in range(50):
            set_output(24, 1)
            sleep(0.05)

            set_output(24, 0)
            sleep(0.05)
else:
        set_output(24,1)
        sleep(0.05)