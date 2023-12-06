import secrets
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

application = Flask(__name__) 
application.config['SECRET_KEY'] = secrets.token_hex(16)
application.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:3306/university_db'
application.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(application)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

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
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=True)
    university = db.relationship('University', backref=db.backref('students'))
    entrance_date = db.Column(db.Date)

    def __repr__(self):
        return f"{self.firstname} {self.lastname} {self.patronymic}"