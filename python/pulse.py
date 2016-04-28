#!/usr/bin/python
import RPi.GPIO as GPIO
import sys
import time

# Check if there are 2 parameters
if len(sys.argv) == 3:

    # Arguments
    ledPin = int(sys.argv[1])
    speed = float(sys.argv[2])/100
    
    # Setup GPIO
    GPIO.setmode(GPIO.BCM)
    GPIO.setwarnings(False)

    # Setup LED
    GPIO.setup(ledPin, GPIO.OUT)
    # PWM
    p = GPIO.PWM(ledPin, 50)
    p.start(0)

    # Limit speed
    if speed > 0.10:
        speed = 0.02

    try:
        # Gradually turn on
        for i in range(100):
            p.ChangeDutyCycle(i)
            time.sleep(speed)

        # Gradually turn off
        for i in range(100):
            p.ChangeDutyCycle(100-i)
            time.sleep(speed)

        # Stop PWM
        p.stop()

        # Clean GPIO
        GPIO.cleanup()
    except KeyboardInterrupt:
        pass
else:
    print "usage:pulse.py pin speed (in s)"
