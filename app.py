from datetime import datetime
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from admin import admin
from actors import student, faculty

app = Flask(__name__)

""" DATABASE """
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:////temp/examapp.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

class ExamApp(db.Model):
    uid = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable=False)

    def __repr__(self) -> str:
        return f"{self.uid}"

app.register_blueprint(admin)
app.register_blueprint(student)
app.register_blueprint(faculty)

""" DATE """
@app.context_processor
def now():
    return {'now':datetime.utcnow()}

""" ERROR HANDLERS """
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

""" ROUTES """
@app.route("/")
def index():
    return render_template("index.html");

@app.route("/features")
def features():
    return render_template("comingsoon.html")
@app.route("/pricing")
def pricing():
    return render_template("comingsoon.html")
@app.route("/blogs")
def blogs():
    return render_template("comingsoon.html")
@app.route("/login")
def login():
    return render_template("comingsoon.html")
@app.route("/register")
def register():
    return render_template("comingsoon.html")

@app.route("/student/<username>")
@app.route("/faculty/<username>")
def user(username):
    return render_template("profile.html", username=username)

@app.route("/demo")
def demo():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(debug=True)
