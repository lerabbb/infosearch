from flask import request
from wtforms_alchemy import ModelForm, QuerySelectField
from .models import *

class UserForm(ModelForm):
    class Meta:
        model = User

class UniversityForm(ModelForm):
    class Meta:
        model = University

class StudentForm(ModelForm):
    class Meta:
        model = Student
    university = QuerySelectField('university')
    