#!/usr/bin/python
from pyA20.gpio import gpio as GPIO
from pyA20.gpio import port
import sys

# Check if there are 2 parameters
if len(sys.argv) == 3:

    # Arguments
    ledPin = int(sys.argv[1])
    state = int(sys.argv[2])

    # Setup GPIO
    GPIO.init()

    # Setup led
    if state == 1:
        # Setup LED as OUTPUT
        GPIO.setcfg(ledPin, GPIO.OUTPUT)
        # Turn on LED (we keep the state)
        GPIO.output(ledPin, True)
    if state == 0:
        # Setup LED as OUTPUT
        # Clean state (this will turn off the led)
        GPIO.setcfg(ledPin, GPIO.OUTPUT)
        GPIO.output(ledPin, False)

else:
    print "usage:onoff_orange.py pin state"
