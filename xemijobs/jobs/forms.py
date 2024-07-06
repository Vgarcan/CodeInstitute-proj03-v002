

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length


class JobForm(FlaskForm):
    post_title = StringField('post_title', validators=[DataRequired(), Length(min=4, max=25)])
    location = StringField('location', validators=[DataRequired(), Length(min=4, max=25)])
    salary = IntegerField('salary', validators=[DataRequired()])
    job_type = SelectField('job_type', validators=[DataRequired()],choices=["Full-time", "Part-time", "Remote"])
    description = StringField('description', validators=[DataRequired(), Length(min=4, max=500)])
    ends_on = DateField('ends_on', validators=[DataRequired()], format='%Y-%m-%d')

    # # data added in views 
    # published_on
    # comp_name
    # comp_id
    
    submit = SubmitField('Create New Job!')