#!/usr/bin/python

from pyA20.gpio import gpio as GPIO
from pyA20.gpio import port

import sys
import time

# Check if there are 3 parameters
if len(sys.argv) == 4:
    # Arguments
    ledPin = int(sys.argv[1])
    loopUntil = int(sys.argv[2])
    speed = float(sys.argv[3])

    # Setup GPIO
    GPIO.init()

    # Setup led (OUTPUT)
    GPIO.setcfg(ledPin, GPIO.OUTPUT)

    # We limit speed and how many blink we can do
    if speed > 3:
        speed = 3

    if loopUntil > 10:
        loopUntil = 10

    # Turn on/off the led in a loop
    for i in range(0, loopUntil):
        GPIO.output(ledPin, True)
        time.sleep(speed)
        GPIO.output(ledPin, False)
        time.sleep(speed)
else:
    print "usage:blink.py_orange pin loopUntil speed (in s)"
