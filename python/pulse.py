#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time

if len(sys.argv) == 3:
    ledPin = int(sys.argv[1])
    speed = float(sys.argv[2])/100
    if speed > 0.10:
        speed = 0.02

    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)
    GPIO.setup(ledPin, GPIO.OUT)

    p = GPIO.PWM(ledPin, 50)
    p.start(0)


    try:
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(speed)

        for i in range(100):
            p.ChangeDutyCycle(100-i)
            time.sleep(speed)

        p.stop()
        GPIO.cleanup()
    except KeyboardInterrupt:
        pass
else:
    print "usage:onoff.py pin loopUntil speed (in s)"
