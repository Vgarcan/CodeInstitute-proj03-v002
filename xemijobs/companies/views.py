from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegistrationForm, LoginForm
from .models import Company
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import mongo
from ..decoratros import role_checker


companies = Blueprint('companies', __name__, template_folder='templates', static_folder='static')

@companies.route('/')
def index():
    print(current_user.username, 'role ====> ', current_user.role)
    return "<h1>this is company's INDEX</h1>"

@companies.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles company registration.

    Parameters:
    form (RegistrationForm): The form object containing the company's registration details.

    Returns:
    render_template: If the form is not submitted or contains errors, render the registration template with the form.
    redirect: If the company is successfully registered, redirect to the login page.
    flash: If the username already exists, display a flash message.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        print(f"Registering user: {username}")

        existing_user = mongo.db.companies.find_one({'username': username})
        print(f"Existing user: {existing_user}")

        # If the user doesn't exist, insert them into the database
        if existing_user == None:
            print(f"Inserting user: {username}")
            mongo.db.companies.insert_one({'username': username, 'password': password, 'role':'company'})
            flash('User registered successfully!', 'success')
            return redirect(url_for('companies.login'))
        
        elif existing_user['username'] == username :
            flash('Username already exists!', 'danger')
            return redirect(url_for('companies.register'))

    
    for field_name, field_object in form._fields.items():
            print(f"Field Name: {field_name}, Field Label: {field_object.label.text}")
    
    return render_template('register.html', form=form)

@companies.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles company login.

    Parameters:
    form (LoginForm): The form object containing the company's login credentials.

    Returns:
    render_template: If the form is not submitted or contains errors, render the login template with the form.
    redirect: If the company is successfully logged in, redirect to the dashboard page.
    flash: If the username or password is invalid, display a flash message.
    """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Fetch user data from MongoDB
        user_data = mongo.db.companies.find_one({'username': username})
        
        # Check if user exists and password is correct
        if user_data and check_password_hash(user_data['password'], password):
            # Create a User object and log in the user
            user = Company(user_data['username'], user_data['password'], user_data['_id'], user_data['role'])
            login_user(user)
            print (current_user.username, "\n", current_user.role)
            
            # Display success flash message and redirect to dashboard
            flash('Logged in successfully!', 'success')
            return redirect(url_for('companies.dashboard'))
        else:
            # Display error flash message
            flash('Invalid username or password!', 'danger')

    # Render the login template with the form
    return render_template('login.html', form=form)

@companies.route('/logout')
@login_required
@role_checker('company')
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('companies.login'))


@companies.route('/dashboard')
@login_required
@role_checker('company')
def dashboard():
    return "<h1>this is company's DASHBOARD</h1>"

