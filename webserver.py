import RPi.GPIO as GPIO
import time
from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def cube():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()
