#import RPi.GPIO as GPIO
#import time
import os
from flask import Flask
from flask import render_template

app = Flask(__name__, static_url_path='/static')

@app.route('/')
def cube():
    return render_template('index.html')
if __name__ == "__main__":
    app.run(debug=True)
