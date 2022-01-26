from flask import *

student = Blueprint("student",__name__, static_folder="static", template_folder="templates/student")

@student.route("/<username>/dashboard")
def student_index(username = session["username"]):
    if(session):
        return render_template("index.html", username = username)
    else:
        return redirect("/login");

faculty = Blueprint("faculty",__name__, static_folder="static", template_folder="templates/faculty")

@faculty.route("/<username>/dashboard")
def faculty_index(username = session["username"]):
    if(session):
        return render_template("index.html", username = username)
    else:
        return redirect("/login");

admin = Blueprint("faculty",__name__, static_folder="static",  template_folder="templates/faculty")
@admin.route("/<username>/dashboard")
def admin_index(username = session["username"]):
    if(session):
        return render_template("index.html", username = username)
    else:
        return redirect("/login");