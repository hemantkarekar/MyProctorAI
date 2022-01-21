from flask import Blueprint, render_template
page = Blueprint("aunthenticate",__name__, static_folder="static", template_folder="templates/auth", url_prefix="/auth")

""" COMMON PAGES """
@page.route("/")
def index():
    return render_template("index.html");

@page.route("/user/add")
@page.route("/user/register")
def user_add():
    return render_template("adduser.html");