from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, jsonify, redirect, url_for, session, request
from flask_session import Session


load_dotenv()
app = Flask(__name__, static_folder = 'static')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)

# @app.before_request
# def enforce_https():
#     if request.url.startswith('http://'):
#         url = request.url.replace('http://', 'https://', 1)
#         return redirect(url, code=301)

@app.route("/")
@app.route("/index")
@app.route("/home")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug = True)