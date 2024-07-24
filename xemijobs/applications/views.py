from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import  login_required, current_user
from .models import Application
from ..jobs.models import Job
from ..decoratros import role_checker
from datetime import datetime


applications = Blueprint('applications', __name__, template_folder='templates', static_folder='static')

# CREATE
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

# UPDATE

@applications.route('/update-application/<appli_id>/<adv_id>/<status>', methods=['GET','POST'])
@login_required
@role_checker('company')
def update_appl(appli_id, status, adv_id):
    try:
        Application.update_application_status(appli_id, status)
        flash('Application status updated successfully!', 'success')
    except Exception as e:
        flash(f'Error updating application status: {e}', 'error')

    return redirect(url_for('companies.adv_dash', adv_id= adv_id))

# DELETE
@applications.route('/delete-application/<appli_id>', methods=['GET','POST'])
@login_required
@role_checker('user')
def delete_user_appl(appli_id):

    Application.delete_application(appli_id)
    if current_user.role == 'user':
        return redirect(url_for('users.dashboard'))
    else:
        return redirect(url_for('companies.dashboard'))


@applications.route('/delete-all-applications', methods=['POST'])
@login_required
def delete_all_appl():
    Application.delete_all_applications(current_user.id, current_user.role)
    if current_user.role == 'user':
        return redirect(url_for('users.dashboard'))
    elif current_user.role == 'company':
        return redirect(url_for('companies.dashboard'))

@applications.route('/delete-applis-from-adv/<adv_id>', methods=['GET','POST'])
@login_required
@role_checker('company')
def delete_all_appls_from_adv(adv_id):
    try:
        Application.delete_all_applications_from_advert(adv_id, current_user.role)
        flash('All applications from this advert successfully deleted!!', 'success')

        return redirect(url_for('jobs.delete_comp_adv', adv_id=adv_id))
    except Exception as e:
        flash('There was an error deleting the applications: '+str(e), 'error')
        return redirect(url_for('companies.dashboard'))


