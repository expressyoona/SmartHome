# -*- coding: utf-8 -*-
import speech_recognition as sr  
import os

# get audio from the microphone                                                                       
r = sr.Recognizer()                                                                                   

while True:
    with sr.Microphone() as source:                                                                       
        print("Xin mời bạn nói:")                                                                                   
        audio = r.listen(source)
        
    try:
        voice = r.recognize_google(audio, language='vi-VN').lower()
        print('Bạn đã nói', voice)
        command = []
        if 'bật đèn' in voice:
            command.append('python3 /home/pi/SmartHome/ControlLED.py on')
        if 'bật quạt' in voice:
            command.append('python3 /home/pi/SmartHome/ControlFan.py on')
        if 'tắt đèn' in voice:
            command.append('python3 /home/pi/SmartHome/ControlLED.py off')            
        if 'tắt quạt' in voice:
            command.append('python3 /home/pi/SmartHome/ControlFan.py off')
        else:
            pass
        for cm in command:
            os.system(cm)
    except sr.UnknownValueError:
        print("Không thể nhận dạng")
    except sr.RequestError as e:
        print("Lỗi nhận dạng: {0}".format(e))
    except KeyboardInterrupt:
        pass
