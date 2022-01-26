from flask import Blueprint, render_template
accounts = Blueprint("aunthenticate",__name__, static_folder="static", template_folder="templates/accounts", url_prefix="/accounts")

""" COMMON accountsS """
@accounts.route("/<entity>/otp/verify")
def verify(username):
    return render_template("verifyOTP.html", username = username)
 
@accounts.route("/password/reset")
def reset_password():
    return render_template("verifyOTP.html");

@accounts.route("/signup")
def user_add():
    return render_template("adduser.html");