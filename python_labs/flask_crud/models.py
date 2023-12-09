from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(100))

    def validate_password(self, password) -> bool:
        return self.password == password


class University(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    name = db.Column(db.String(100), unique=True)
    shortname = db.Column(db.String(100), unique=True)
    create_date = db.Column(db.Date)

    def __repr__(self):
        return self.shortname


class Student(db.Model):
    id = db.Column(db.BigInteger, primary_key=True)
    firstname = db.Column(db.String(100), unique=True)
    lastname = db.Column(db.String(100), unique=True)
    patronymic = db.Column(db.String(100), unique=True)
    birthdate = db.Column(db.Date)
    entrance_date = db.Column(db.Date)
    university_id = db.Column(db.BigInteger, db.ForeignKey('university.id'))
    university = db.relationship('University', backref='students')

    def __repr__(self):
        return f"{self.firstname} {self.lastname} {self.patronymic}"