from flask import Flask, jsonify, request
import pandas as pd

app = Flask(__name__)

df = pd.read_csv("data.csv")

@app.route("/")
def home():
    msg = jsonify({"message": "My CSV API is running!"})
