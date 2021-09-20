# 💻 Advanced Anti-Cheating Examination Portal

*Last updated on Sept 11, 2019*

## Table of Contents

[Introduction](#introduction)

[Features](#features)

[Developer's Guide](#developers_guide)

## Introduction

The primary aim of this project is - **to make a demo of examination platform which is cheating proof to nearly all possibilities.** At the end of this project work, you will be getting a exam portal where no student can cheat in any possible ways.

## Features



# Developer's Guide

## ⚙ Installation Steps

1. Install Python, Add it to the System Environment Variables.
2. Open the project in VSCode.
3. Run `pip install virtualenv ` to install virtual environment.
4. Run `virtualenv env` to create a new virtual environment.
5. Run `Set-ExecutionPolicy unrestricted`, if it throws an error, run the same command in Admin PowerShell, and when prompted press `A`.
6. 🔸 Run `.\env\Scripts\activate.ps1` to enable virtualenv.
7. Run `pip install flask`.

## 🔹 Important Code Blocks

```python
from flask import Blueprint, render_template

admin = Blueprint("admin",__name__, static_folder="static", template_folder="templates", url_prefix="/admin")

@admin.route("/dashboard")
@admin.route("/")
def dashboard():
    return "<h1>Dashboard</h1>"
```

```python
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
    
```

