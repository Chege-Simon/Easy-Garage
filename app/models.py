from flask import current_app
from app import db

class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    sir_name = db.Column(db.String(14), index=True)
    first_name = db.Column(db.String(14), index=True)
    last_name = db.Column(db.String(14), index=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def repr(self):
        return f'<User {self.id}, {self.sir_name}, {self.first_name}>'

