from flask import Blueprint, render_template, request, redirect, url_for
from flask_login import login_required, current_user
from flask_crud.models import University, Student, db
from flask_crud.forms import *
views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    return render_template("home.html", user=current_user)


@views.route('/university', methods=['GET'])
@login_required
def university_list():
    if request.method == "GET":
        universities = University.query.all()
        return render_template("university_list.html", university_list=universities)


@views.route('/university/<int:id>', methods=['GET'])
@login_required
def get_university(id):    
    if request.method == "GET":
        university = University.query.get(ident=id)
        return render_template(
            "university.html",
            un_id=id, 
            name=university.name,
            shortname=university.shortname,
            create_date=university.create_date
        )
    
@views.route('/university/create', methods=['GET', 'POST'])
@login_required
def create_university():
    form = UniversityForm()
    if request.method == "POST":
        university = University(
            name = request.form.get("name"),
            shortname = request.form.get("shortname"),
            create_date = request.form.get("create_date")
        )
        db.session.add(university)
        db.session.commit()
        return redirect(url_for('views.university_list'))
    return render_template("create_university.html", form=form)


@views.route('/university/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_university(id):
    university = University.query.get(ident=id)
    form = UniversityForm(obj=university)
    if request.method == "GET":
        return render_template("create_university.html", form=form)
    elif request.method == "POST":
        university.name = request.form.get("name")
        university.shortname = request.form.get("shortname")
        university.create_date = request.form.get("create_date")
        db.session.commit()
        return redirect(url_for('views.university_list'))


@views.route('/university/delete/<int:id>')
@login_required
def delete_university(id):
    if request.method == "POST":
        university = University.query.get(ident=id)
        db.session.delete(university)
        db.session.commit()
        return redirect(url_for('views.university_list'))


@views.route('/student', methods=['GET'])
@login_required
def student_list():
    if request.method == "GET":
        students = Student.query.all()
        return render_template("student_list.html", student_list=students)


@views.route('/student/<int:id>', methods=['GET'])
@login_required
def get_student(id):
    if request.method == "GET":
        student = Student.query.get(ident=id)
        return render_template(
            "student.html",
            student_id=id, 
            firstname=student.firstname,
            lastname=student.lastname,
            patronymic=student.patronymic,
            birthdate=student.birthdate,
            university=student.university,
            entrance_date=student.entrance_date
        )


@views.route('/student/create', methods=['GET', 'POST'])
@login_required
def create_student():
    form = StudentForm()
    if request.method == "GET":
        return render_template("create_student.html", form=form)
    elif request.method == "POST":
        university = University.query.get(form.university.data)
        student = Student(
            firstname=request.form.get("firstname"),
            lastname=request.form.get("lastname"),
            patronymic=request.form.get("patronymic"),
            birthdate=request.form.get("birthdate"),
            university=university,
            entrance_date=request.form.get("entrance_date"),
        )
        db.session.add(student)
        db.session.commit()
        return redirect(url_for('views.student_list'))



@views.route('/student/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_student(id):
    student = Student.query.get(ident=id)
    form = StudentForm(obj=student)
    form.university.query = University.query.all()
    print(form.firstname)
    print(form.university)
    if request.method == "GET":
        return render_template("create_student.html", form=form)
    elif request.method == "POST":
        student.firstname=request.form.get("firstname")
        student.lastname=request.form.get("lastname")
        student.patronymic=request.form.get("patronymic")
        student.birthdate=request.form.get("birthdate")
        student.university_id=request.form.get("university")
        student.entrance_date=request.form.get("entrance_date")
        db.session.commit()
        return redirect(url_for('views.student_list'))


@views.route('/student/delete/<int:id>', methods=["POST"])
@login_required
def delete_student(id):
     if request.method == "POST":
        student = Student.query.get(ident=id)
        db.session.delete(student)
        db.session.commit()
        return redirect(url_for('views.student_list'))