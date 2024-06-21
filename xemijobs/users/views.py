from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required
from .forms import RegistrationForm, LoginForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import mongo

users = Blueprint('users', __name__)

@users.route('/')
def index():
    return "<h1>this is user's INDEX</h1>"

@users.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)

        existing_user = mongo.db.users.find_one({'username': username})
        if existing_user is None:
            mongo.db.users.insert_one({'username': username, 'password': password})
            flash('User registered successfully!', 'success')
            return redirect(url_for('users.login'))
        else:
            flash('Username already exists!', 'danger')
    return render_template('register.html', form=form)

@users.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user_data = mongo.db.users.find_one({'username': username})
        if user_data and check_password_hash(user_data['password'], password):
            user = User(user_data['username'], user_data['password'])
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password!', 'danger')
    return render_template('login.html', form=form)

@users.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('index'))
