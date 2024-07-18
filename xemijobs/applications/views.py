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
    print ('=====================>>>>>', job)
    if job == False:
        flash('Job does not exist','error')
        return redirect(url_for('users.dashboard'))
    
    application = {
        'user_id': str(current_user.id),
        'adv_id': str(adv_id),
        'comp_id': str(job.comp_id),
        'status' : 'pending'
    }
    print('=============>>>>',application)
    print('=============>>>>',current_user.id,"\n")
    for application_ in Application.get_all_sent_applications(current_user.id):
        for key, value in application_.__dict__.items():
            print('=============>>>>',key, ':', value)

        print('=============>>>>',application_.__dict__)
        if application_.adv_id == job.id:
            flash("User has already sent an application for this job.", "warning")
            return redirect(url_for('users.dashboard'))
        
    try:
        Application.create_new_application(application)
        flash('Application sent successfully!', 'success')
        return redirect(url_for('users.dashboard'))
    except Exception as e:
        flash(f'There was an error with your application: {e}', 'error')
        return redirect(url_for('users.dashboard'))




