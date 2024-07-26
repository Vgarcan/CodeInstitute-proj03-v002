

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, DateField, SelectField, IntegerField
from wtforms.validators import DataRequired, Length


class JobForm(FlaskForm):
    post_title = StringField('Post Title', validators=[DataRequired(), Length(min=4, max=25)], name='post_title')
    location = StringField('Location', validators=[DataRequired(), Length(min=4, max=25)], name='location')
    salary = IntegerField('Salary', validators=[DataRequired()], name='salary')
    job_type = SelectField('Job Type', validators=[DataRequired()],choices=["Full-time", "Part-time", "Remote"], name='job_type')
    description = StringField('Description', validators=[DataRequired(), Length(min=4, max=500)], name='description')
    ends_on = DateField('Ends on:', validators=[DataRequired()], format='%Y-%m-%d', name='ends_on')

    # # data added in views 
    # published_on
    # comp_name
    # comp_id
    
    submit = SubmitField('Create New Job!')