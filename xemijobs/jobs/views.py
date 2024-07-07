from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import JobForm
from .models import Job
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import mongo, ObjectId
from ..decoratros import role_checker

import datetime

jobs = Blueprint('jobs', __name__, template_folder='templates', static_folder='static')

@jobs.route('/')
def index():
    return "<h1>this is jobs's INDEX</h1>"

@jobs.route('/page1')
def app_another():
    return "<h1>this is jobs's PAGE1</h1>"


@jobs.route('/job-list')
def job_list():
    ### This is going to show all the jobs in the database
    # 1. get all the jobs using the model function for that
    # 2. pass the jobs to the template for display
    listed_jobs = Job.get_all_jobs()
    # 3. make sure to add pagination or limit the number of jobs shown per page
    return "<h1>this is jobs's LISTINGS</h1>"


@jobs.route('/job-detail/<job_id>')
def job_detail(job_id):
    ### This is going to show the details of a single job using the job's ID passed with the URL
    # 1. get the job using the model function for that
    job_details= Job.get_by_id(job_id) 
    # 2. pass the job to the template for display
    # 3. add any additional details or information needed for the job detail page
    return "<h1>this is jobs's DETAIL</h1>"


@jobs.route('/create-job')
@login_required
@role_checker('company')
def create_job():
    ### This is goint to create a new job only for the company
    # 1. create a form for the company to fill out
    form = JobForm()
    # 2. validate the form data
    if form.validate_on_submit():
        details = {
            'post_title': form.title.data,
            'location': form.location.data,
            'salary': form.salary.data,
            'job_type': form.job_type.data,
            'description': form.description.data,
            'ends_on': form.ends_on.data,
            'published_on': datetime.now(),
            'company_name': current_user.username,
            'comp_id': current_user.id
        }
        
        try:
            Job.create_new_job(job_data=details)
        except Exception as e:
            print ('There was an error creating ======> ' + str(e))
        
    # 3. save the job to the database using the model
    # 4. redirect the company to the job detail page for the newly created job
    return "<h1>this is jobs's CREATE JOB</h1>"

@jobs.route('/edit-job/<job_id>')
@login_required
@role_checker('company')
def edit_job(job_id):
    ### This is going to edit an existing job only for the company
    # 1. get the job using the model function for that
    job_details=Job.get_by_id(job_id)
    # 2. reuse the JOB's form for the company to edit out and populate with the existing data
    form = JobForm()
    # 3. validate the form data
    if form.validate_on_submit():
        details = {
            'post_title': form.title.data,
            'location': form.location.data,
            'salary': form.salary.data,
            'job_type': form.job_type.data,
            'description': form.description.data,
            'ends_on': form.ends_on.data,
            'published_on': datetime.now(),
            'company_name': current_user.username,
            'comp_id': current_user.id
        }
    # 4. save the updated job to the database using the model
        try:
            Job.create_new_job(job_data=details)
        except Exception as e:
            print ('There was an error creating ======> ' + str(e))
    # 5. redirect the company to the job detail page for the updated job
    return "<h1>this is jobs's EDIT JOB</h1>"