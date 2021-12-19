from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey, PrimaryKeyConstraint

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    age = db.Column(db.Integer)
    sex = db.Column(db.Integer)
    dalt = db.Column(db.Integer)


class Answers(db.Model):
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    id = db.Column(db.Integer, primary_key=True)
    q1 = db.Column(db.Integer)
    q2 = db.Column(db.Integer)
    q3 = db.Column(db.Integer)
    q4 = db.Column(db.Integer)
    q5 = db.Column(db.Integer)
    q6 = db.Column(db.Integer)
    q7 = db.Column(db.Integer)
    q8 = db.Column(db.Integer)
    q9 = db.Column(db.Integer)
    q10 = db.Column(db.Integer)
    q11 = db.Column(db.Integer)
    q12 = db.Column(db.Integer)
    q13 = db.Column(db.Integer)
    q14 = db.Column(db.Integer)
    q15 = db.Column(db.Integer)
