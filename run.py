import os
from dotenv import load_dotenv
from flask import Flask
from xemijobs.extensions import mongo, login_manager, csrf

# Import the blueprints
from xemijobs.main.views import main
from xemijobs.users.views import users
from xemijobs.companies.views import companies
from xemijobs.jobs.views import jobs

# Load environment variables
load_dotenv()

# Initialize the FLASK APP
app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
app.config['MONGO_URI'] = os.getenv('MONGO_URI')

# Initialize the EXTENSIONS
mongo.init_app(app)
csrf.init_app(app)
login_manager.init_app(app)
login_manager.login_view = 'users.login'

# Load the BLUEPRINTS
app.register_blueprint(main, url_prefix='/')
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(companies, url_prefix='/companies')
app.register_blueprint(jobs, url_prefix='/jobs')

# @app.route('/')
# def index():
#     return "<h1>Landing Page</h1><p>This is the main page for our website</p>"

@app.route('/success')
def success_registration():
    return "<h1>Form PASSES</h1><p>Good job</p>"

if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST'), 
        port=os.getenv('PORT'), 
        debug=True
    )
