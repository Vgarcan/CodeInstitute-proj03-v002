

from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length, EqualTo


class RegisterNewJob(FlaskForm):
    post_title = StringField('post_title', validators=[DataRequired(), Length(min=4, max=25)])
    comp_name = StringField('comp_name', validators=[DataRequired(), Length(min=4, max=25)])
    comp_id = StringField('comp_id', validators=[DataRequired()])
    location = StringField('location', validators=[DataRequired(), Length(min=4, max=25)])
    salary = IntegerField('salary', validators=[DataRequired()])
    job_type = SelectField('job_type', validators=[DataRequired()],choices=["Full-time", "Part-time", "Remote"])
    description = StringField('description', validators=[DataRequired(), Length(min=4, max=500)])
    published_on = DateField('published_on', validators=[DataRequired()], format='%Y-%m-%d')
    ends_on = DateField('ends_on', validators=[DataRequired()], format='%Y-%m-%d')
    
    submit = SubmitField('Create New Job!')