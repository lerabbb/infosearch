from django.db import models

class University(models.Model):
    name = models.CharField(max_length=100, unique=True)
    short_name = models.CharField(max_length=100, unique=True)
    create_date = models.DateField()

    def __str__(self):
        return self.short_name

class Student(models.Model):
    firstname = models.CharField(max_length=100, unique=True)
    lastname = models.CharField(max_length=100, unique=True)
    patronymic = models.CharField(max_length=100, unique=True)
    birthdate = models.DateField()
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    entrance_date = models.DateField()

    def __str__(self):
        return f"{self.firstname} {self.lastname} {self.patronymic}"