from flask import Blueprint, render_template

jobs = Blueprint('jobs', __name__, template_folder='templates', static_folder='static')

@jobs.route('/')
def index():
    return "<h1>this is jobs's INDEX</h1>"

@jobs.route('/page1')
def app_another():
    return "<h1>this is jobs's PAGE1</h1>"