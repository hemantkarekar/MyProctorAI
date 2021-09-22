from flask import Blueprint, render_template

student = Blueprint("student",__name__, static_folder="static", template_folder="templates", url_prefix="/student")

@student.route("/home")
@student.route("/")
def student_index():
    return render_template("student_index.html")

faculty = Blueprint("faculty",__name__, static_folder="static", template_folder="templates", url_prefix="/faculty")

@faculty.route("/home")
@faculty.route("/")
def faculty_index():
    return render_template("faculty_index.html")