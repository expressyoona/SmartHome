#!flask/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from flask import render_template
from flask_cors import CORS

import ControlFan
import ControlLED
import dht

from os import system

app = Flask(__name__)
CORS(app)

result = {}

@app.route('/', methods=['GET','POST'])
def controlEquip():
    if request.method == 'GET':
        global result
        result['LED'] = ControlLED.getState()
        result['Fan'] = ControlFan.getState()
        return jsonify(result)
    elif request.method == 'POST':
        if not request.json or 'text' not in request.json or 'lang' not in request.json:
            abort(400)
            #Handle

        global result
        result['LED'] = ControlLED.getState()
        result['Fan'] = ControlFan.getState()
        result['State'] = 'Success'
        
        if request.json['lang'] == 'en':
            if 'turn on the light' in request.json['text']:
                system('python3 /home/pi/SmartHome/ControlLED.py on')
            elif 'turn off the light' in request.json['text']:
                system('python3 /home/pi/SmartHome/ControlLED.py off')
            elif 'turn off the fan' in request.json['text']:
                system('python3 /home/pi/SmartHome/ControlFan.py off')
            elif 'turn on the fan' in request.json['text']:
                system('python3 /home/pi/SmartHome/ControlFan.py on')
            else:
                result['State']  = 'Invalid command'
        elif request.json['lang'] == 'vi':
            if 'bật đèn' in request.json['text']:
                system('python3 /home/pi/SmartHome/ControlLED.py on')
            elif 'tắt đèn' in request.json['text']:
                system('python3 /home/pi/SmartHome/ControlLED.py off')
            elif 'bật quạt' in request.json['text']:
                system('python3 /home/pi/SmartHome/ControlFan.py off')
            elif 'tắt quạt' in request.json['text']:
                system('python3 /home/pi/SmartHome/ControlFan.py on')
            else:
                result['State'] = 'Không rõ lệnh'
        else:
                result['State'] = 'Invalid language/Ngôn ngữ không hợp lệ'
        return jsonify(result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
