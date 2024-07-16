from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import  login_required, current_user
from .models import Application
from ..jobs.models import Job
from ..users.models import User
from ..companies.models import Company
from ..extensions import mongo, ObjectId
from ..decoratros import role_checker


applications = Blueprint('applications', __name__, template_folder='templates', static_folder='static')


@applications.route('/')
def index():
    return "<h1>this is application's INDEX</h1>"



@applications.route('/succeed')
def succeed():
    flash('You successfully applied for the job!', category='success')
    return redirect('users.dashboard')

@applications.route('/apply-for/<adv_id>', methods=['GET','POST'])
@login_required
@role_checker('user')
def apply(adv_id):

    job = Job.get_by_id(adv_id)
    if job == False:
        flash('Job does not exist','error')
        return redirect(url_for('users.dashboard'))
    
    application = {
        'user_id': str(current_user.id),
        'job_id': str(job.id),
        'comp_id': str(job.comp_id),
    }

    try:
        mongo.db.applications.insert_one(application)
        flash('Application sent successfully!', 'success')
        return redirect(url_for('users.dashboard'))
    except Exception as e:
        flash(f'There was an error with your application: {e}', 'error')
        redirect('users.dashboard')


        


