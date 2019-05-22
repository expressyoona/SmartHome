import sqlite3
from time import sleep
from datetime import datetime
import lcd
import dht
import os

import ControlFan
import ControlLED
import RPi.GPIO as GPIO

conf = {}

def readConfig():
    conn = sqlite3.connect('conf.db')
    cur = conn.cursor()
    cur.execute('SELECT * FROM Config')
    row = cur.fetchone()
    conf['auto'], conf['LED'], conf['fan'], conf['start'], conf['end'], conf['pivot'] = row

def updateConfig(auto=None, LED=None, fan=None, start=None, end=None, pivot=None):
    pass
    

try:
    while True:
        readConfig()
        hud, temp = dht.getData()
        lcd.lcd_string("Auto: " + conf['auto'], lcd.LCD_LINE_1)
        lcd.lcd_string("Temp: " + str(temp) + " C", lcd.LCD_LINE_2)
        if conf['auto'] == 'On':
            if temp >= conf['pivot']:
                if ControlFan.getState() == 0:
                    os.system('python3 /home/pi/SmartHome/ControlFan.py on')
                    print('Turned on')
            else:
                if ControlFan.getState() == 1:
                    os.system('python3 /home/pi/SmartHome/ControlFan.py off')
                    print('Turned off')
            now = datetime.now().strftime('%H:%M')
            if conf['start'] < conf['end']:
                if conf['start'] <= now <= conf['end']:
                    if ControlLED.getState() == 0:
                        os.system('python3 /home/pi/SmartHome/ControlLED.py on')
                else:
                    if ControlLED.getState() == 1:
                        os.system('python3 /home/pi/SmartHome/ControlLED.py off')
            else:#Over night
                if now < conf['end'] or now > conf['start']:
                    if ControlLED.getState() == 0:
                        os.system('python3 /home/pi/SmartHome/ControlLED.py on')
                else:
                    if ControlLED.getState() == 1:
                        os.system('python3 /home/pi/SmartHome/ControlLED.py off')
        sleep(1)
except KeyboardInterrupt:
        lcd.lcd_byte(0x01, lcd.LCD_CMD)
        
