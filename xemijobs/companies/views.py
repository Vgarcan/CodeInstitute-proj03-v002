from flask import Blueprint, render_template

companies = Blueprint('companies', __name__, template_folder='templates', static_folder='static')

@companies.route('/')
def index():
    return "<h1>this is companies's INDEX</h1>"

@companies.route('/page1')
def app_another():
    return "<h1>this is companies's PAGE1</h1>"