#!/usr/bin/env python3 

import RPi.GPIO as GPIO
import sys

PIN = 17

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(PIN, GPIO.IN)
GPIO.setup(PIN, GPIO.OUT)

def getState():
     return GPIO.input(PIN)

if __name__ == '__main__':
     mode = sys.argv[-1]
     
     if mode == 'on':
          GPIO.output(PIN, GPIO.HIGH)
     elif mode == 'off':
          GPIO.output(PIN, GPIO.LOW)
     else:
          print('Pass an argument!!!')
