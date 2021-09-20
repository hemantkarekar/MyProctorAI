from flask import Blueprint, render_template

admin = Blueprint("admin",__name__, static_folder="static", template_folder="templates", url_prefix="/admin")

@admin.route("/dashboard")
@admin.route("/")
def dashboard():
    return "<h1>Dashboard</h1>"