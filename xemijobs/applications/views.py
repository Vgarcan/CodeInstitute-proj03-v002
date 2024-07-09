from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import  login_required, current_user
# from .models import Job
from ..extensions import mongo, ObjectId
from ..decoratros import role_checker


applications = Blueprint('applications', __name__, template_folder='templates', static_folder='static')


@applications.route('/')
def index():
    return "<h1>this is application's INDEX</h1>"