# flask for web app.
from flask import Flask, request
from tensorflow.keras.models import load_model
import tensorflow as tf
import numpy as np
import flask

# Create a new web app.
app = Flask(__name__,static_url_path = '',static_folder = 'static')
model = load_model('turbine_model')

@app.route('/')
def home():
    return app.send_static_file('index.html')

@app.route("/<speed>")
def predict(speed):
    speed = float(speed)
    power = model.predict([speed])
    return {"value" : float(power[0][0])}

if __name__ == "__main__":
    app.run(debug = True)