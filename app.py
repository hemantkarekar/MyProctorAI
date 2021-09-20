from flask import Flask, render_template
from admin import admin
app = Flask(__name__)
app.register_blueprint(admin)

""" ERROR HANDLERS """
@app.errorhandler(404)
def not_found(e):
    return render_template("404.html")

""" ROUTES """
@app.route("/")
def index():
    return render_template("index.html");

@app.route("/exam")
def exam():
    return "<p>Hello, Exam!</p>"

if __name__ == "__main__":
    app.run(debug=True)
    