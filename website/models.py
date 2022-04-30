from . import db 
from flask_login import UserMixin
from sqlalchemy.sql import func

class Profile(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    gender = db.Column(db.String(100))
    age = db.Column(db.Integer)
    hypertension = db.Column(db.Integer)
    heart_disease = db.Column(db.Integer)
    married = db.Column(db.Integer)
    work_type = db.Column(db.String(100))
    residence_type = db.Column(db.String(100))
    avg_glucose_level = db.Column(db.Float)
    bmi = db.Column(db.Float)
    smoking_status = db.Column(db.String(100))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    firstName = db.Column(db.String(150))
    profile = db.relationship("Profile")
