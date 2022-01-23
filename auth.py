from flask import Blueprint, render_template
auth = Blueprint("aunthenticate",__name__, static_folder="static", template_folder="templates/auth", url_prefix="/auth")

""" COMMON authS """
@auth.route("/<entity>/verify")
def index():
    return render_template("index.html");

@auth.route("/user/login")
def user_add():
    return render_template("adduser.html");
@auth.route("/user/register")
def user_add():
    return render_template("adduser.html");