from flask import render_template, redirect, url_for
from flask_login import LoginManager, login_required, login_user, logout_user
from flask_crud.models import User, application
from flask_crud.forms import *

login_manager = LoginManager()
login_manager.login_view = 'auth.login' 
login_manager.init_app(application)

@application.route('/') 
def template(): 
    return render_template('index.html')

@login_manager.user_loader
def load_user(id):
    return User.query.get(id)

@application.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == "GET":
        return render_template("login.html", form=UserForm())
    elif request.method == "POST":
        email=request.form.get("email")
        password=request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user and user.validate_password(password):
            login_user(user)
            return redirect(url_for('/'))
    return redirect('/login')


@application.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == "GET":
        return render_template('registration.html', form=UserForm())
    email = request.form.get("email")
    password = request.form.get("password")
    name = request.form.get("name")
    user = User(email=email, password=password, name=name)
    try:
        db.session.add(user)
        db.session.commit()
    except Exception as err:
        print(err)
    return redirect('/login')


@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login.index'))


@application.route('/university', methods=['GET'])
@login_required
def university_list():
    if request.method == "GET":
        universities = University.query.all()
        return render_template("university_list.html", university_list=universities)


@application.route('/university/<int:id>', methods=['GET'])
@login_required
def get_university(id):    
    if request.method == "GET":
        university = University.query.get(ident=id)
        return render_template(
            "university.html",
            un_id=id, 
            name=university.name,
            shor_tname=university.shortname,
            create_date=university.create_date
        )
    

@application.route('/university/create', methods=['GET', 'POST'])
@login_required
def create_university():
    form = UniversityForm()
    if request.method == "GET":
        return render_template("create_entity.html", title = "Университет", form=form)
    elif request.method == "POST":
        university = University(
            name = form.name.data,
            shortname = form.shortname.data,
            create_date = form.create_date.data
        )
        db.session.add(university)
        db.session.commit()
        return redirect('/university')


@application.route('/university/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_university(id):
    university = University.query.get(ident=id)
    form = UniversityForm(obj=university)
    if request.method == "GET":
        return render_template("create_entity.html", title = "Университет", form=form)
    elif request.method == "POST":
        university = University(
            name = form.name.data,
            shortname = form.shortname.data,
            create_date = form.create_date.data
        )
        db.session.commit()
        return redirect('/university')


@application.route('/university/delete/<int:id>')
@login_required
def delete_university(id):
    if request.method == "POST":
        university = University.query.get(ident=id)
        db.session.delete(university)
        db.session.commit()
        return redirect("/university")


@application.route('/student', methods=['GET'])
@login_required
def student_list():
    if request.method == "GET":
        students = Student.query.all()
        return render_template("student_list.html", student_list=students)


@application.route('/student/<int:id>', methods=['GET'])
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


@application.route('/student/create', methods=['GET', 'POST'])
@login_required
def create_student():
    form = StudentForm()
    if request.method == "GET":
        return render_template("create_entity.html", title = "Студент", form=form)
    elif request.method == "POST":
        student = Student(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            patronymic=form.patronymic.data,
            birthdate=form.birthdate.data,
            university=form.university.data,
            entrance_date=form.entrance_date.data
        )
        db.session.add(student)
        db.session.commit()
        return redirect('/student')


@application.route('/student/change/<int:id>', methods=['GET', 'POST'])
@login_required
def change_student(id):
    student = Student.query.get(ident=id)
    form = StudentForm(obj=student)
    form.university.query = University.query.all()
    if request.method == "GET":
        return render_template("create_entity.html", title = "Студент", form=form)
    elif request.method == "POST":
        student = Student(
            firstname=form.firstname.data,
            lastname=form.lastname.data,
            patronymic=form.patronymic.data,
            birthdate=form.birthdate.data,
            university=form.university.data,
            entrance_date=form.entrance_date.data
        )
        db.session.commit()
        return redirect('/student')


@application.route('/student/delete/<int:id>', methods=["POST"])
@login_required
def delete_student(id):
     if request.method == "POST":
        student = Student.query.get(ident=id)
        db.session.delete(student)
        db.session.commit()
        return redirect("/student")
     
if __name__ == "__main__": 
    application.run()
    