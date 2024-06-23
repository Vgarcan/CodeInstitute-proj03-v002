from flask import Blueprint, render_template
from ..extensions import mongo

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
def index():
    return "<h1>this is main's INDEX</h1>"

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