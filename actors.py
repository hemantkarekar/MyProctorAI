from flask import Blueprint, render_template

admin = Blueprint("admin",__name__, static_folder="static", template_folder="templates/admin", url_prefix="/admin")

@admin.route("/")
def admin_index():
    return render_template("faculty_index.html")
student = Blueprint("student",__name__, static_folder="static", template_folder="templates/student", url_prefix="/student")

@student.route("/<username>")
def student_index(username):
    return render_template("student_index.html", username = username)

@student.route("/exams")
def student_exams():
    return render_template("student_exams.html")


faculty = Blueprint("faculty",__name__, static_folder="static", template_folder="templates/faculty", url_prefix="/faculty")

@faculty.route("/")
def faculty_index():
    return render_template("faculty_index.html")