from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=36)])
    confirm_password = PasswordField('confirm_password', validators=[DataRequired(), EqualTo('password')])

    # name = StringField('Name', validators=[DataRequired(), Length(min=1, max=50)])
    # surname = StringField('Surname', validators=[DataRequired(), Length(min=1, max=50)])

    
    submit = SubmitField('Register')

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=6, max=36)])
    submit = SubmitField('Login')
