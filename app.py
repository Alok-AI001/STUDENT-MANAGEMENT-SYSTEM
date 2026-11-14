import os
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import or_

app = Flask(__name__)
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "change-this-secret-before-production")

database_url = os.environ.get("DATABASE_URL", "").strip()
if database_url.startswith("postgres://"):
    database_url = database_url.replace("postgres://", "postgresql+psycopg://", 1)
elif database_url.startswith("postgresql://"):
    database_url = database_url.replace("postgresql://", "postgresql+psycopg://", 1)

if database_url:
    app.config["SQLALCHEMY_DATABASE_URI"] = database_url
else:
    instance_dir = Path(app.instance_path)
    instance_dir.mkdir(parents=True, exist_ok=True)
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + str(instance_dir / "students.db")

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(30), unique=True, nullable=False)
    name = db.Column(db.String(100), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    course = db.Column(db.String(100), nullable=False)
    branch = db.Column(db.String(100), nullable=False)
    marks = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Student {self.student_id}: {self.name}>"


with app.app_context():
    db.create_all()


@app.route("/")
def index():
    search = request.args.get("q", "").strip()
    query = Student.query
    if search:
        pattern = f"%{search}%"
        query = query.filter(
            or_(
                Student.student_id.ilike(pattern),
                Student.name.ilike(pattern),
                Student.course.ilike(pattern),
                Student.branch.ilike(pattern),
            )
        )
    students = query.order_by(Student.id.desc()).all()
    total_students = Student.query.count()
    average_marks = db.session.query(db.func.avg(Student.marks)).scalar() or 0
    return render_template(
        "index.html",
        students=students,
        search=search,
        total_students=total_students,
        average_marks=round(average_marks, 1),
    )


@app.route("/students/add", methods=["GET", "POST"])
def add_student():
    if request.method == "POST":
        student_id = request.form.get("student_id", "").strip()
        name = request.form.get("name", "").strip()
        course = request.form.get("course", "").strip()
        branch = request.form.get("branch", "").strip()
        try:
            age = int(request.form.get("age", ""))
            marks = float(request.form.get("marks", ""))
        except ValueError:
            flash("Please enter a valid age and marks.", "danger")
            return render_template("student_form.html", student=None)

        if not all([student_id, name, course, branch]):
            flash("Please fill in every field.", "danger")
            return render_template("student_form.html", student=None)
        if age < 1 or age > 120 or marks < 0 or marks > 100:
            flash("Age must be 1–120 and marks must be between 0 and 100.", "danger")
            return render_template("student_form.html", student=None)
        if Student.query.filter_by(student_id=student_id).first():
            flash("That student ID already exists. Please use a unique ID.", "danger")
            return render_template("student_form.html", student=None)

        student = Student(
            student_id=student_id,
            name=name,
            age=age,
            course=course,
            branch=branch,
            marks=marks,
        )
        db.session.add(student)
        db.session.commit()
        flash("Student added successfully.", "success")
        return redirect(url_for("index"))

    return render_template("student_form.html", student=None)


@app.route("/students/<int:student_pk>")
def view_student(student_pk):
    student = db.get_or_404(Student, student_pk)
    return render_template("student_detail.html", student=student)


@app.route("/students/<int:student_pk>/edit", methods=["GET", "POST"])
def edit_student(student_pk):
    student = db.get_or_404(Student, student_pk)
    if request.method == "POST":
        student_id = request.form.get("student_id", "").strip()
        name = request.form.get("name", "").strip()
        course = request.form.get("course", "").strip()
        branch = request.form.get("branch", "").strip()
        try:
            age = int(request.form.get("age", ""))
            marks = float(request.form.get("marks", ""))
        except ValueError:
            flash("Please enter a valid age and marks.", "danger")
            return render_template("student_form.html", student=student)

        duplicate = Student.query.filter(
            Student.student_id == student_id, Student.id != student.id
        ).first()
        if not all([student_id, name, course, branch]):
            flash("Please fill in every field.", "danger")
            return render_template("student_form.html", student=student)
        if age < 1 or age > 120 or marks < 0 or marks > 100:
            flash("Age must be 1–120 and marks must be between 0 and 100.", "danger")
            return render_template("student_form.html", student=student)
        if duplicate:
            flash("That student ID is already used by another student.", "danger")
            return render_template("student_form.html", student=student)

        student.student_id = student_id
        student.name = name
        student.age = age
        student.course = course
        student.branch = branch
        student.marks = marks
        db.session.commit()
        flash("Student details updated successfully.", "success")
        return redirect(url_for("view_student", student_pk=student.id))

    return render_template("student_form.html", student=student)


@app.route("/students/<int:student_pk>/delete", methods=["POST"])
def delete_student(student_pk):
    student = db.get_or_404(Student, student_pk)
    db.session.delete(student)
    db.session.commit()
    flash("Student deleted successfully.", "success")
    return redirect(url_for("index"))


@app.errorhandler(404)
def not_found(_error):
    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)
