import RPi.GPIO as GPIO
import time
import os
import sys

# set BCM_GPIO 23 as relay pin
RelayPin = 23

GPIO.setwarnings(False)
#set the gpio modes to BCM numbering
GPIO.setmode(GPIO.BCM)
#set RelayPin's mode to output,and initial level to LOW(0V)
GPIO.setup(RelayPin,GPIO.OUT,initial=GPIO.LOW)

def getState():
    return GPIO.input(RelayPin)

if __name__ == '__main__':

    mode = sys.argv[-1]

    if mode == 'on':
         GPIO.output(RelayPin, GPIO.HIGH)
         #print('Turned on')
    elif mode == 'off':
         GPIO.output(RelayPin, GPIO.LOW)
         #print('Turned off')
    else:
         print('Pass a argument')
         pass


    
