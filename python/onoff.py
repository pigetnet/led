#!/usr/bin/python
import RPi.GPIO as GPIO
import sys

# Check if there are 2 parameters
if len(sys.argv) == 3:

    # Arguments
    ledPin = int(sys.argv[1])
    state = int(sys.argv[2])

    # Setup GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Setup led
    if state == 1:
        # Setup LED as OUTPUT
        GPIO.setup(ledPin, GPIO.OUT)
        # Turn on LED (we keep the state)
        GPIO.output(ledPin, True)
    if state == 0:
        # Setup LED as OUTPUT
        # Clean state (this will turn off the led)
        GPIO.setup(ledPin, GPIO.OUT)
	GPIO.output(ledPin, False)       
else:
    print "usage:onoff.py pin state"
