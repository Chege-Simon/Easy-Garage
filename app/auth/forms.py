from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Required, Email, EqualTo, Length


class SignupForm(FlaskForm):
    sir_name = StringField('Sir Name', validators=[Required(), Length(min=3, max=14)])
    first_name = StringField('First Name', validators=[Required(), Length(min=3, max=14)])
    last_name = StringField('Last Name', validators=[Required(), Length(min=3, max=14)])
    email = StringField('Email', validators=[Required(), Length(min=3, max=120)])
    password = PasswordField('Password', validators=[Required(), Length(min=3, max=14)])
    confirm_password = PasswordField('Confirm Password', validators=[Required(), Length(min=3, max=14)])
    signup = SubmitField()


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Length(min=3, max=120), Email()])
    password = PasswordField('Password', validators=[Required(), Length(min=3, max=14)])
    login = SubmitField()