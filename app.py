from datetime import datetime
import imp
from flask import Flask, Blueprint, render_template
from admin import admin
from actors import student, faculty
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from pages import page



app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/test'
db = SQLAlchemy(app)
class Testdb(db.Model):
    name = db.Column(db.String(255), primary_key=True)
    downloads = db.Column(db.String(255))

app.register_blueprint(student,url_prefix="/student")
app.register_blueprint(faculty,url_prefix="/faculty")

""" DATE """
@app.context_processor
def now():
    return {'now':datetime.utcnow()}

""" ERROR HANDLERS """
@app.errorhandler(404)
def not_found(e):
    return render_template("errors/404.html")

""" ROUTES """
@app.route("/")
def index():
    return render_template("pages/index.html")
@app.route("/<page>")
def show(page):
    return render_template(f"pages/{page}.html")


@app.route("/user/add")
@app.route("/user/register")
def user_add():
    return render_template("pages/adduser.html");

@app.route("/user/login")
def user_login():
    return render_template("pages/login.html");


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

@app.route("/faculty/<username>")
def user(username):
    return render_template("profile.html", username=username)

@app.route("/demo")
def demo():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(debug=True)
