#!/usr/bin/python
import RPi.GPIO as GPIO
import sys

if len(sys.argv) == 3:
    ledPin = int(sys.argv[1])
    state = int(sys.argv[2])
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    #print state
    # Setup led
    if state == 1:
        # We can't cleanup gpio or the led will not stay on
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.output(ledPin, True)
    if state == 0:
        # You just need to cleanup gpio
        GPIO.setup(ledPin, GPIO.OUT)
        GPIO.cleanup()

else:
    print "usage:onoff.py pin state"
