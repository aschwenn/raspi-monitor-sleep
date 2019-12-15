#!/usr/bin/env python
 
import sys
import time
import RPi.GPIO as GPIO
import subprocess
 
GPIO.setmode(GPIO.BCM)

''' CONSTANTS '''
TURNOFF_DELAY_SECONDS = 30
SENSOR_PIN = 17
USE_ALWAYS_ON_OVERRIDE = False
ALWAYS_ON_PIN = 16
ALWAYS_ON_STATE = 1 # will enable upon reading this value
USE_ALWAYS_OFF_OVERRIDE = True
ALWAYS_OFF_PIN = 20
ALWAYS_OFF_STATE = 0 # will enable upon reading this value

''' PROGRAM '''
def main():
    GPIO.setup(SENSOR_PIN, GPIO.IN)
    if USE_ALWAYS_ON_OVERRIDE:
        GPIO.setup(ALWAYS_ON_PIN, GPIO.IN)
    if USE_ALWAYS_OFF_OVERRIDE:
        GPIO.setup(ALWAYS_OFF_PIN, GPIO.IN)
    turned_off = False
    last_motion_time = time.time()
 
    while True:
        if USE_ALWAYS_ON_OVERRIDE:
            if GPIO.input(ALWAYS_ON_PIN) == ALWAYS_ON_STATE:
                if turned_off:
                    turned_off = False
                    turn_on()
                continue
        if USE_ALWAYS_OFF_OVERRIDE:
            if GPIO.input(ALWAYS_OFF_PIN) == ALWAYS_OFF_STATE:
                if not turned_off:
                    turned_off = True
                    turn_off()
                continue
        if GPIO.input(SENSOR_PIN):
            last_motion_time = time.time()
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() > (last_motion_time + TURNOFF_DELAY_SECONDS):
                turned_off = True
                turn_off()
        time.sleep(.1)
 
def turn_on():
    subprocess.call("sh /home/pi/raspi-monitor-sleep/turnon.sh", shell=True)
 
def turn_off():
    subprocess.call("sh /home/pi/raspi-monitor-sleep/turnoff.sh", shell=True)
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
	turn_on()
