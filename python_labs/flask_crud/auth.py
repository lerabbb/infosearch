from flask import Blueprint, render_template, request, flash, redirect, url_for
from flask_crud.models import User
from flask_crud.forms import LoginForm, RegistrationForm
from flask_crud import db
from flask_login import login_user, login_required, logout_user, current_user

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=["GET", "POST"])
def login():
    form = LoginForm()
    if request.method == "POST":
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            if user.validate_password(password):
                flash('Successful login', category='success')
                login_user(user, remember=True)
                return redirect(url_for('views.home'))
       
            else:
                flash('Wrong password', category='error')
       
        else:
            flash("User doesn't exist", category='error')
    
    return render_template("auth.html", form=form)


@auth.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route("/registration", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if request.method == "POST":
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")
        user = User.query.filter_by(email=email).first()
        if user:
            flash("User already exists", category='error')
            pass

        user = User(email=email, name=name, password=password)
        db.session.add(user)
        db.session.commit()
        login_user(user, remember=True)
        flash('Successful registration', category='success')
        return redirect(url_for('views.home'))

    return render_template("registration.html", form=form)