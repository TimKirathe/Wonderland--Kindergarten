from dotenv import load_dotenv
import os
from flask import Flask, request, render_template, jsonify, redirect, url_for, session, request
from flask_session import Session
from flask_sqlalchemy import SQLAlchemy


load_dotenv()
app = Flask(__name__, static_folder = 'static')
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URI']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = os.environ.get('DATABASE_TRACK_MODIFICATIONS')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SESSION_PERMANENT'] = False
Session(app)
db = SQLAlchemy()
Session(app)

class ParentEnquiry(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(120), nullable = False)
    email = db.Column(db.String(256), nullable = False)
    enquiry = db.Column(db.String, nullable = False)

    def __repr__(self):
        return f"User: {self.email}"
    
db.init_app(app)
with app.app_context():
    # User.__table__.drop(db.engine)
    db.create_all()

# with app.app_context():
#     delete all users from database
#     db.session.query(User).delete()
#     db.session.commit()
#     delete a specific user from the database
    # users = User.query.all()
    # print(users)
    # user = User.query.filter_by(email="mit@gmail.com").first()
    # print(user)
    # db.session.delete(user)
    # db.session.commit() 

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

            enq = ParentEnquiry(name=parent_name, email=parent_email, enquiry=parent_enquiry)
            db.session.add(enq)
            db.session.commit()

        else:
            student_first_name = request.form[""]
            student_last_name = request.form[""]
            student_first_name = request.form[""]
            student_first_name = request.form[""]
            student_first_name = request.form[""]
            student_first_name = request.form[""]
            student_first_name = request.form[""]
            student_first_name = request.form[""]
            student_first_name = request.form[""]

    return render_template("contact.html")

if __name__ == "__main__":
    app.run(debug = True)