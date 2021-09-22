from datetime import datetime
from flask import Flask, render_template
from admin import admin
from entity import student, faculty
app = Flask(__name__)
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

@app.route("/demo")
def demo():
    return render_template("demo.html")

if __name__ == "__main__":
    app.run(debug=True)
