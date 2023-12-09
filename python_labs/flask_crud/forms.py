from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField
from wtforms.validators import DataRequired, Length, Email  
from .models import *

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Length(max=100), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Login')

class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    email = StringField('Email', validators=[DataRequired(), Length(max=100), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Length(max=100)])
    submit = SubmitField('Registration')

class UniversityForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(max=100)])
    shortname = StringField('Short name', validators=[DataRequired(), Length(max=100)])
    create_date = DateField('Date of creating', validators=[DataRequired()])
    submit = SubmitField('Add new university')

class StudentForm(FlaskForm):
    firstname = StringField('Firstname', validators=[DataRequired(), Length(max=100)])
    lastname = StringField('Lastname', validators=[DataRequired(), Length(max=100)])
    patronymic = StringField('Patronymic', validators=[DataRequired(), Length(max=100)])
    birthdate = DateField('Birth date', validators=[DataRequired()])
    entrance_date = DateField('Date of entrance', validators=[DataRequired()])
    university = SelectField('University', validators=[DataRequired()], coerce=int)
    submit = SubmitField('Add new student')

    def __init__(self, *args, **kwargs):
        super(StudentForm, self).__init__(args, kwargs=kwargs)
        self.university.choices = [(un.id, un.shortname) for un in University.query.all()]