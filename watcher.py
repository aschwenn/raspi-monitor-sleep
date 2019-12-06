#!/usr/bin/env python
 
import sys
import time
import RPi.GPIO as GPIO
import subprocess
 
GPIO.setmode(GPIO.BCM)

''' CONSTANTS '''
TURNOFF_DELAY_SECONDS = 5
PIN = 17
 
def main():
    GPIO.setup(PIN, GPIO.IN)
    turned_off = False
    last_motion_time = time.time()
 
    while True:
        if GPIO.input(PIN):
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
    subprocess.call("sh turnon.sh", shell=True)
 
def turn_off():
    subprocess.call("sh turnoff.sh", shell=True)
 
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        GPIO.cleanup()
	turn_on()
