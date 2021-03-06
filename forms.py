from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo
from flask import redirect, session
from functools import wraps

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class SignUp(FlaskForm):
    username = StringField('Username', validators=[
        Length(min=4, max=25),
        DataRequired()
    ])
    email = StringField('Email Address', validators=[
        Length(min=6, max=35),
        DataRequired()
    ])
    password = PasswordField('New Password', [
        DataRequired(),
        EqualTo('confirm', message='Passwords must match')
    ])
    confirm = PasswordField('Confirm your new password')
    submit = SubmitField('Create account')
    
def login_required(f):
    """
    Written by Harvard CS50 staff: Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function