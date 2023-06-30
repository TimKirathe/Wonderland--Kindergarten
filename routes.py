from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, jsonify, redirect, url_for, session
from flask_session import Session


load_dotenv()
app = Flask(__name__, static_folder = 'static')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug = True)