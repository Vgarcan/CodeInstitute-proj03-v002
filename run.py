import os
from dotenv import load_dotenv
from flask import Flask, render_template

# import the apps
from users.views import users
from companies.views import companies
from jobs.views import jobs


app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Load the BLUEPRINTS
app.register_blueprint(users, url_prefix='/users')
app.register_blueprint(companies, url_prefix='/companies')
app.register_blueprint(jobs, url_prefix='/jobs')


@app.route('/')
def index():
    return "<h1>Landing Page</h1><p>This is the main page for our website</p>"

if __name__ == '__main__':
    app.run(
        host=os.getenv('HOST'), 
        port=os.getenv('PORT'), 
        debug=True
    )


