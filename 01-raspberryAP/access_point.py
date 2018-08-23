# -*- coding: utf-8 -*-
# @Time    : 2018/8/4 16:30
# @Author  : HUHONGLIN
# @File    : led.py
# @Software: PyCharm 
import os
import time

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

GPIO.setup(40, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setwarnings(False)

def create_ap():
    os.system("sudo cp /home/pi/Public/AP/wpa_supplicant.conf /home/pi/Public/WIFI")
    os.system("sudo cp /home/pi/Public/AP/dhcpcd.conf /etc/")
    os.system("sudo reboot")
def my_callback(channel):
    print("button pressed!")
    create_ap()
    time.sleep(0.5)
    pass

GPIO.add_event_detect(40, GPIO.RISING, callback=my_callback)
while True:
    try:
        print("I'm working...")
        time.sleep(5)
        pass
    except KeyboardInterrupt:
        break
        pass
    pass
GPIO.cleanup()
