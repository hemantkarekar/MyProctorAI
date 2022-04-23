from datetime import datetime
from tkinter import font
from urllib import request
from flask import * 
from functools import wraps
from camera import generate_frames
# from admin import admin
# from actors import student, faculty
from accounts import accounts
from flask_sqlalchemy import *
from processes import *
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/proctorai_website'
db = SQLAlchemy(app)
""" 
id 50, name 200, username 100, email 200, password 100, user_type 50, credits int11, user_status 50, registered_on 50
"""
class Users(db.Model):
    id = db.Column(db.String(50), primary_key=True)
    name = db.Column(db.String(200))
    username = db.Column(db.String(100))
    email = db.Column(db.String(200))
    password = db.Column(db.String(100))
    user_type = db.Column(db.String(50))
    user_status = db.Column(db.String(50))
    registered_on = db.Column(db.String(50))
    credits = db.Column(db.Integer)

# app.register_blueprint(student)
# app.register_blueprint(faculty)
app.register_blueprint(accounts)

""" DATE """
@app.context_processor
def now():
    return {'now':datetime.utcnow()}

""" ERROR HANDLERS """
@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html")


@app.before_request
def make_session_permanent():
	session.permanent = True

def user_type_professor(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			if session['user_type']=="teacher":
				return f(*args, **kwargs)
			else:
				flash('You dont have privilege to access this page!','danger')
				return render_template("404.html") 
		else:
			flash('Unauthorized, Please login!','danger')
			return redirect(url_for('login'))
	return wrap

def user_type_student(f):
	@wraps(f)
	def wrap(*args, **kwargs):
		if 'logged_in' in session:
			if session['user_type']=="student":
				return f(*args, **kwargs)
			else:
				flash('You dont have privilege to access this page!','danger')
				return render_template("404.html") 
		else:
			flash('Unauthorized, Please login!','danger')
			return redirect(url_for('/login'))
	return wrap

""" ROUTES """
@app.route("/")
def index():
    return render_template("pages/index.html")

@app.route("/<page>")
def show(page):
    return render_template(f"pages/{page}.html")

@app.route("/register")
def register():
    return render_template("pages/adduser.html")
    
@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        session.permanent = True
        email = request.form["email"]
        password = request.form["password"]
        found_user = Users.query.filter_by(email = email).first()
        if found_user.password == password:
            session["username"] = found_user.username
            session["email"] = found_user.email
            session["user_type"] = found_user.user_type
            # flash(f"{found_user.username} is Found")
            return redirect(f"/{session['username']}/dashboard")
        else:
            return render_template("pages/login.html")
    elif request.method =="GET":
        if session:
            return redirect(f"/{session['username']}/dashboard")
        else:
            return render_template("pages/login.html")
            
@app.route("/logout")
def logout():
    session.clear();
    return redirect("/login")

@app.route("/<username>/dashboard")
def dashboard(username):
    if session:
        return render_template(f"{session['user_type'].lower()}/index.html");
    else:
        return redirect("/login")

@app.route("/<username>/exams")
def exams(username):
    if session:
        return render_template(f"{session['user_type'].lower()}/exams.html");
    else:
        return redirect("/login")

@app.route("/<username>/exam/demo")

def exam_demo(username):
    if session:
        session['blacklisted_processes'] = check_and_alert_blacklisted_processes()
        return render_template(f"{session['user_type'].lower()}/demo.html");
    else:
        return redirect("/login")

# @app.route("/pricing")
# def pricing():
#     return render_template("comingsoon.html")
# @app.route("/blogs")
# def blogs():
#     return render_template("comingsoon.html")

# @app.route("/login")
# def login():
#     return render_template("comingsoon.html")
# @app.route("/register")
# def register():
#     return render_template("comingsoon.html")
@app.route("/<username>/demo")
def demo(username, usertype="Admin"):
    if(usertype=="Admin"):
        return render_template("demo.html", username = username, usertype = usertype)


@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')


if __name__ == "__main__":
    app.secret_key = 'super secret key'
    app.config['SESSION_TYPE'] = 'filesystem'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
    # session.init_app(app)
    app.run(debug=True)
