from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField
from wtforms.validators import DataRequired, Length, EqualTo, Optional

## REGISTRATION FORM (COMPANY)
class RegistrationForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=25)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=36)]
    )
    confirm_password = PasswordField(
        "confirm_password", validators=[DataRequired(), EqualTo("password")]
    )
    submit = SubmitField("Register")


## LOGIN FORM (COMPANY)
class LoginForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=4, max=25)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=6, max=36)]
    )
    submit = SubmitField("Login")


## PROFILE FORM (COMPANY)
class ProfileForm(FlaskForm):
    username = StringField(
        "Username", validators=[DataRequired(), Length(min=2, max=20)]
    )
    theme = SelectField(
        "Choose your theme",
        validators=[DataRequired()],
        choices=[
            "None",
            "neon-blue-theme",
            "pink-theme",
            "dark-elegant-theme",
            "modern-sophisticated-theme",
            "fresh-vibrant-theme",
            "sunset-breeze-theme",
            "ocean-mist-theme",
            "tropical-twilight-theme",
            "midnight-bloom-theme",
            "serene-dawn-theme",
        ],
        name="theme",
    )
    new_password = PasswordField(
        "New Password", validators=[Optional(), Length(min=6, max=20)]
    )
    confirm_password = PasswordField(
        "Confirm New Password", validators=[EqualTo("new_password")]
    )
    current_password = PasswordField("Current Password", validators=[DataRequired()])
    submit = SubmitField("Update Profile")
