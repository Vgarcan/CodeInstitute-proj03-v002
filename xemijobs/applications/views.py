from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import  login_required, current_user
from .models import Application
from ..jobs.models import Job
from ..decoratros import role_checker
from datetime import datetime


applications = Blueprint('applications', __name__, template_folder='templates', static_folder='static')


@applications.route('/apply-for/<adv_id>', methods=['GET','POST'])
@login_required
@role_checker('user')
def apply(adv_id):

    job = Job.get_by_id(adv_id)
    print ('=====================>>>>>', job.__dict__)
    if job == False:
        flash('Job does not exist','error')
        return redirect(url_for('users.dashboard'))
    
    application = {
        'adv_id': str(adv_id),
        'comp_id': str(job.comp_id),
        'user_id': str(current_user.id),
        'created_on': datetime.now(),
        'status' : 'pending'
    }
    print('=============>>>>',application)
    print('=============>>>>',current_user.id,"\n")
    print('=============>>>>',Application.get_all_applications(current_user.id, current_user.role),"\n")

    for application_ in Application.get_all_applications(current_user.id, current_user.role):
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


@applications.route('/delete-application/<appli_id>', methods=['POST'])
@login_required
def delete_user_appl(appli_id):

    Application.delete_application(appli_id)
    if current_user.role == 'user':
        return redirect(url_for('users.dashboard'))
    else:
        return redirect(url_for('companies.dashboard'))
    

# delete all applications

@applications.route('/delete-all-applications', methods=['POST'])
@login_required
def delete_all_appl():
    Application.delete_all_applications(current_user.id, current_user.role)
    if current_user.role == 'user':
        return redirect(url_for('users.dashboard'))
    else:
        return redirect(url_for('companies.dashboard'))