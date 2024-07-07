from flask import Blueprint, render_template
from ..extensions import mongo
from flask_login import login_required, current_user

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/page1')
def app_another():
    return "<h1>this is main's PAGE1</h1>"

@main.route('/test_mongo')
def test_mongo():
    try:
        from flask import jsonify
        collections = mongo.db.list_collection_names()
        return jsonify(collections)
    except Exception as e:
        return str(e), 500
    
@main.route('/profile')
# @login_required
def profile():
    return render_template('profile.html', user=current_user)
