from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import  login_required, current_user
from .forms import JobForm
from .models import Job
from ..extensions import mongo
from ..decoratros import role_checker

from datetime import datetime, date, time

jobs = Blueprint('jobs', __name__, template_folder='templates', static_folder='static')


@jobs.route('/job-list')
def job_list(page=1):
    # PAGINATION = 9
    per_page = 9
    offset = (page - 1) * per_page
    # data = rawdata[offset:offset + per_page]
    per_page = 9
    listed_jobs = Job.get_all_jobs(offset, per_page)
    return render_template("jobs/jobs-list.html",rawdata=listed_jobs, page=page)


@jobs.route('/job-detail/<job_id>')
def job_detail(job_id):
    job_details= Job.get_by_id(job_id) 
    return render_template("jobs/view-job.html", data= job_details)


@jobs.route('/create-job', methods=['GET', 'POST'])
@login_required
@role_checker('company')
def create_job():
    form = JobForm()

    if form.validate_on_submit():

        job_data = {
            'post_title': form.post_title.data,
            'location': form.location.data,
            'salary': form.salary.data,
            'job_type': form.job_type.data,
            'description': form.description.data,
            'published_on': datetime.now(),
            'ends_on': datetime.strptime(str(form.ends_on.data), '%Y-%m-%d').replace(hour=0, minute=00, second=00, microsecond=000000),
            'company_name': current_user.username,
            'comp_id': current_user.id
        }

        # print (datetime.now())
        # print (form.ends_on.data)
        
        try:
            Job.create_new_job(job_data = job_data)
            flash('Job created successfully', 'success')
            return redirect(url_for('jobs.job_list'))
        except Exception as e:
            print ('There was an error creating ======> ' + str(e))
            flash('Job was not Created: ' + str(e), "error")
        
    return render_template('jobs/create-job.html', form=form)

@jobs.route('/edit-job/<job_id>')
@login_required
@role_checker('company')
def edit_job(job_id):
    job_details=Job.get_by_id(job_id)

    form = JobForm()

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

    return "<h1>this is jobs's EDIT JOB</h1>"