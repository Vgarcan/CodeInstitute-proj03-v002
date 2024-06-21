from flask import Blueprint, render_template

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
def index():
    return "<h1>this is main's INDEX</h1>"

@main.route('/page1')
def app_another():
    return "<h1>this is main's PAGE1</h1>"