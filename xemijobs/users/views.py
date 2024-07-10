from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegistrationForm, LoginForm, ProfileForm
from .models import User
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import mongo, ObjectId
from ..decoratros import role_checker


users = Blueprint('users', __name__, template_folder='templates', static_folder='static')


@users.route('/')
def index():
    return "<h1>this is user's INDEX</h1>"


@users.route('/register', methods=['GET', 'POST'])
def register():
    """
    Handles user registration.

    Parameters:
    form (RegistrationForm): The form object containing the user's registration details.

    Returns:
    render_template: If the form is not submitted or contains errors, render the registration template with the form.
    redirect: If the user is successfully registered, redirect to the login page.
    flash: If the username already exists, display a flash message.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        role = 'user'
        print(f"Registering user: {username}")

        existing_user = mongo.db.users.find_one({'username': username})
        print(f"Existing user: {existing_user}")

        # If the user doesn't exist, insert them into the database
        if existing_user == None:
            print(f"Inserting user: {username}")
            User.create_new_user(username, password, role)
            flash('User registered successfully!', 'success')
            return redirect(url_for('users.login'))
        
        elif existing_user['username'] == username :
            flash('Username already exists!', 'danger')
            return redirect(url_for('users.register'))
    
    for field_name, field_object in form._fields.items():
            print(f"Field Name: {field_name}, Field Label: {field_object.label.text}")
    
    return render_template('users/register.html', form=form)


@users.route('/login', methods=['GET', 'POST'])
def login():
    """
    Handles user login.

    Parameters:
    form (LoginForm): The form object containing the user's login credentials.

    Returns:
    render_template: If the form is not submitted or contains errors, render the login template with the form.
    redirect: If the user is successfully logged in, redirect to the dashboard page.
    flash: If the username or password is invalid, display a flash message.
    """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        user_data = User.get(username)
        try:
            print('==============>>>>', user_data.username)
        except Exception as e:
            print ('==============>>>>', e)
        
        # Check if user exists and password is correct
        ## check_password_hash() ches if the hashed passwords marches given password
        if user_data and check_password_hash(user_data.password, password):
            # Create a User object and log in the user
            user = User.get_by_id(user_data.id)
            login_user(user)
            
            # Display success flash message and redirect to dashboard
            flash('Logged in successfully!', 'success')
            return redirect(url_for('users.dashboard'))
        else:
            # Display error flash message
            flash('Invalid username or password!', 'danger')

    # Render the login template with the form
    return render_template('users/login.html', form=form)


@users.route('/logout')
@login_required
@role_checker('user')
def logout():
    """
    Logs out the current user.

    This function logs out the current user by calling the `logout_user()` function from the `flask_login` module.
    It also displays a success flash message using the `flash()` function from the `flask` module.

    Parameters:
    None

    Returns:
    redirect: A redirect response to the login page (`users.login`)
    """
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('users.login'))


@users.route('/dashboard')
@login_required
@role_checker('user')
def dashboard():
    print (current_user.username)
    return render_template('users/dashboard.html')


@users.route('/profile', methods=['GET', 'POST'])
@login_required
@role_checker('user')
def profile():
    """
    Handles user profile updates.

    Parameters:
    form (ProfileForm): The form object containing the user's profile details.

    Returns:
    render_template: If the form is not submitted or contains errors, render the profile template with the form and current user data.
    redirect: If the user profile is successfully updated, redirect to the dashboard page.
    flash: If the username already exists, display a flash message.
    """
    form = ProfileForm()

    if form.validate_on_submit():
        username = form.username.data
        current_password = form.current_password.data
        new_password = form.new_password.data

        print(check_password_hash(current_user.password, current_password))
        if check_password_hash(current_user.password, current_password):
            # If the new password is provided
            if new_password:
                # Hash the new password
                hashed_password = generate_password_hash(new_password)
            # If the new password is not provided
            else:
                # Keep the current password if new is not provided
                hashed_password = current_user.password

        print(f"UPDATING TO USER: {username}")
        profile_data = {
            'username': form.username.data,
            'password': hashed_password,
            '_id': current_user.id,
        }

        existing_user = User.get(profile_data['username'])
        print(f"USER: {existing_user}")

        # Check if the username already exists and it's not the current user's username
        if existing_user and str(ObjectId(existing_user['_id'])) != current_user.id:
            flash('Username already exists!', 'danger')
            return redirect(url_for('users.profile'))

        # Update user information in the database
        try: 
            User.update_profile(profile_data=profile_data)
        except Exception as e:
            print(f"Error updating user: {e}")
            flash('Error updating user!', 'danger')
            return redirect(url_for('users.profile'))

        flash('Profile updated successfully!', 'success')

        return redirect(url_for('users.dashboard'))

    return render_template('users/profile.html', form=form, data=current_user)



@users.route('/users-list')
def list_of_users():
    """
    This function retrieves a list of all users from the database and renders a template with the user data.

    Parameters:
    None

    Returns:
    render_template: If users are found, render the 'users-list.html' template with the user data.
    redirect: If no users are found, display an info flash message and redirect to the index page.
    """

    data = User.get_all_users()
    if data is None:
        flash('No users found!', 'info')
        return redirect(url_for('users.index'))
    return render_template('users/users-list.html', data=data)
