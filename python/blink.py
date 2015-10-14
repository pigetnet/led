#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time

if len(sys.argv) == 4:
    ledPin = int(sys.argv[1])
    loopUntil = int(sys.argv[2])
    speed = float(sys.argv[3])
    if speed > 3:
        speed = 3

    if loopUntil > 10:
        loopUntil = 10

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    GPIO.setup(ledPin, GPIO.OUT)

    for i in range(0, loopUntil):
        GPIO.output(ledPin, True)
        time.sleep(speed)
        GPIO.output(ledPin, False)
        time.sleep(speed)
else:
    print "usage:onoff.py pin loopUntil speed (in s)"
