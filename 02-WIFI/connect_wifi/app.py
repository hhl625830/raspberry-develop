# -*- coding: utf-8 -*-
"""
-------------------------------------------------
   File Name：     app.py
   Description :
   Author :       HuHongLin
   date：          2018/8/18
-------------------------------------------------
   Change Activity:
                   2018/8/18 13:29:
-------------------------------------------------
"""
import os

from flask import Flask, render_template, jsonify, request


def add_ssid(ssid, password, priority):
    network = 'network={\n' \
              '   ssid="' + ssid + '"\n' \
                                   '   psk="' + password + '"\n' \
                                                           '   priority=' + str(priority) + '\n' \
                                                                                            '}\n'

    os.system("sudo chmod 777 /home/pi/Public/WIFI/wpa_supplicant.conf")
    f = open(r'/home/pi/Public/WIFI/wpa_supplicant.conf', 'a+')
    f.write(network)
    f.flush()
    f.close()


def connect_wifi():
    os.system('sudo cp /home/pi/Public/WIFI/dhcpcd.conf /etc/')
    os.system('sudo cp /home/pi/Public/WIFI/wpa_supplicant.conf /etc/wpa_supplicant/')
    os.system('sudo reboot')


app = Flask(__name__)


@app.route('/connect', methods=['POST', 'GET'])
def connect():
    name = request.args.get('name')
    password = request.args.get('password')
    priority = request.args.get('priority')
    add_ssid(name, password, priority)
    connect_wifi()
    return "connect OK"


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)
