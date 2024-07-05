from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
# from .forms import RegistrationForm, LoginForm, ProfileForm
# from .models import Company
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import mongo, ObjectId
from ..decoratros import role_checker

jobs = Blueprint('jobs', __name__, template_folder='templates', static_folder='static')

@jobs.route('/')
def index():
    return "<h1>this is jobs's INDEX</h1>"

@jobs.route('/page1')
def app_another():
    return "<h1>this is jobs's PAGE1</h1>"


@jobs.route('/job-list')
def job_list():
    return "<h1>this is jobs's LISTINGS</h1>"


@jobs.route('/job-detail')
def job_detail():
    return "<h1>this is jobs's DETAIL</h1>"


@jobs.route('/create-job')
@login_required
@role_checker('company')
def create_job():
    return "<h1>this is jobs's CREATE JOB</h1>"

@jobs.route('/edit-job')
@login_required
@role_checker('company')
def edit_job():
    return "<h1>this is jobs's EDIT JOB</h1>"