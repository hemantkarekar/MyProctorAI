from datetime import datetime
from flask import Flask, render_template
from flask_mysqldb import MySQL
from flask_sqlalchemy import SQLAlchemy
from admin import admin
from actors import student, faculty

app = Flask(__name__)

""" DATABASE """
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'test'
 
mysql = MySQL(app)
 
#Creating a connection cursor
cursor = mysql.connection.cursor()
 
#Executing SQL Statements
cursor.execute(''' CREATE TABLE testdb(name, downloads) ''')
cursor.execute(''' INSERT INTO testdb VALUES(Hemant,12) ''')
 
#Saving the Actions performed on the DB
mysql.connection.commit()
 
#Closing the cursor
cursor.close()

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
