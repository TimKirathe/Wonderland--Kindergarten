from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, jsonify, redirect, url_for, session, request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


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

@app.route("/contact", methods = ['GET', 'POST'])
def contact():
    if request.method == 'POST':
        if request.form["enquiry"]:
            parent_name = request.form["parentEnquiryName"]
            parent_email = request.form["parentEnquiryEmail"]
            parent_enquiry = request.form["enquiry"]

        else:

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug = True)