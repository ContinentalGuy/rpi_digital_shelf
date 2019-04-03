#import RPi.GPIO as GPIO
#import time
import os
from flask import Flask, jsonify
from flask import render_template
from PI.distance import *

app = Flask(__name__, static_url_path='/static')

def set_color(int_val):
    if int_val == 0:
        return 'white'
    else:
        return 'rgb(250,80,0)'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upd/', methods=['GET'])
def update_color():
    #sensor_names = ['s1', 's2', 's3', 's4', 's5', 's6']
    sensor_signals = DigitalShelf().check()
    num_of_sensors = len(sensor_signals)
    if num_of_sensors != 6:
        sensors_left = 6 - num_of_sensors
        for i in range(sensors_left):
            sensor_signals.append(0)
    #sensor_signals = [0,1,1,0,0,1]
    sensor_signals = list(map(set_color, sensor_signals))
    #print(sensor_signals)
    
    #return jsonify(dict(zip(sensor_names, sensor_signals)))
    return jsonify(sensor_signals)

if __name__ == "__main__":
    app.run(host='127.0.0.1', port = 8080, debug=True)
