#flask server for plotly hw
import pandas as pd
import numpy as np
from flask import Flask, jsonify

sample_data = pd.read_json('samples.json')

s_data = sample_data.to_dict()

app = Flask(__name__)

@app.route("/")
def home():
    return jsonify(s_data)

if __name__ == '__main__':
    app.run(debug = True)