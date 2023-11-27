from django import forms
from . import models

class UniversityForm(forms.ModelForm):
    class Meta:
        model = models.University
        fields = ('name', 'short_name', 'create_date')

class StudentForm(forms.ModelForm):
    class Meta:
        model = models.Student
        fields = (
            'firstname',
            'lastname',
            'patronymic',
            'birthdate',
            'university',
            'entrance_date'
        )