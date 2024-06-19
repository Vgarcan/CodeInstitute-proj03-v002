from flask import Blueprint, render_template

users = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@users.route('/')
def index():
    return "<h1>this is user's INDEX</h1>"

@users.route('/page1')
def app_another():
    return "<h1>this is user's PAGE1</h1>"