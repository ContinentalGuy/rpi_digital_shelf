#import RPi.GPIO as GPIO
#import time
import os
from flask import Flask, jsonify
from flask import render_template
from PI import distance

app = Flask(__name__, static_url_path='/static')

def set_color(int_val):
    if int_val == 0:
        return 'white'
    else:
        return 'rgb(250,80,0)'

@app.route('/')
def cube():
    infinite = True
    while infinite == True:
        # sensor_signals = DigitalShelf().check()
        # print(sensor_signals)
        sensor_signals = [0, 1, 0, 0, 1, 0]
        sensor_signals = list(map(set_color, sensor_signals))
        print(sensor_signals)
        return render_template('index.html', index0 = sensor_signals[0], index1 = sensor_signals[1], index2 = sensor_signals[2], index3 = sensor_signals[3], index4 = sensor_signals[4], index5 = sensor_signals[5])


@app.route('/upd/')
def update_color():
    return jsonify({'Sensor':'On'})

if __name__ == "__main__":
    app.run(debug=True)
