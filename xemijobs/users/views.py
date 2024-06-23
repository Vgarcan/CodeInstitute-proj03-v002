from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import mongo


users = Blueprint('users', __name__, template_folder='templates', static_folder='static')

@users.route('/')
def index():
    return "<h1>this is user's INDEX</h1>"

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        print(f"Registering user: {username}")

        existing_user = mongo.db.users.find_one({'username': username})
        print(f"Existing user: {existing_user}")

        # If the user doesn't exist, insert them into the database
        if existing_user == None:
            print(f"Inserting user: {username}")
            mongo.db.users.insert_one({'username': username, 'password': password})
            flash('User registered successfully!', 'success')
            return redirect(url_for('users.login'))
        
        elif existing_user['username'] == username :
            flash('Username already exists!', 'danger')
            return redirect(url_for('users.register'))
        
    # elif not form.validate_on_submit():
    #     flash('Form not validated!', 'danger')
    #     return redirect(url_for('users.register'))
    
    for field_name, field_object in form._fields.items():
            print(f"Field Name: {field_name}, Field Label: {field_object.label.text}")
    
    return render_template('register.html', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user_data = mongo.db.users.find_one({'username': username})
        if user_data and check_password_hash(user_data['password'], password):
            user = User(user_data['_id'],user_data['username'], user_data['password'])
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid username or password!', 'danger')

    return render_template('login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('index'))



@users.route('/test_mongo')
def test_mongo():
    try:
        from flask import jsonify
        collections = mongo.db.list_collection_names()
        return jsonify(collections)
    except Exception as e:
        return str(e), 500