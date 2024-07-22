from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user, login_required, current_user
from .forms import RegistrationForm, LoginForm, ProfileForm
from .models import Company
# from ..applications.models import Application
from werkzeug.security import generate_password_hash, check_password_hash
from ..extensions import mongo, ObjectId, get_table_info
from ..decoratros import role_checker


companies = Blueprint('companies', __name__, template_folder='templates', static_folder='static')

@companies.route('/')
def index():
    try:
        print(current_user.username, 'role ====> ', current_user.role)
    except Exception as e:
        print(f"Error: {e}")
    return render_template('companies/index.html')

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

    Function Steps:
    1. Initialize a RegistrationForm object.
    2. If the form is submitted and valid:
        2.1. Get the username and password from the form.
        2.2. Hash the password.
        2.3. Check if a user with the same username already exists.
        2.4. If the user does not exist, create a new user in the database and redirect to the login page.
        2.5. If the user already exists, display a flash message and redirect to the registration page.
    3. If the form is not submitted or contains errors, render the registration template with the form.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        username = form.username.data
        password = generate_password_hash(form.password.data)
        print(f"Registering user: {username}")

        existing_user = Company.get(username)
        print(f"Existing user: {existing_user}")

        # If the user doesn't exist, insert them into the database
        if existing_user == None:
            Company.create_new_user(username, password, 'company')
            flash('User registered successfully!', 'success')
            return redirect(url_for('companies.login'))
        
        elif existing_user['username'] == username :
            flash('Username already exists!', 'danger')
            return redirect(url_for('companies.register'))

    return render_template('companies/register.html', form=form)

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

    Function Steps:
    1. Initialize a LoginForm object.
    2. If the form is submitted and valid:
        2.1. Get the username and password from the form.
        2.2. Fetch user data from MongoDB using the username.
        2.3. Check if user exists and password is correct.
        2.4. If user exists and password is correct:
            2.4.1. Create a User object using the fetched user data.
            2.4.2. Log in the user.
            2.4.3. Print the current user's username and role.
            2.4.4. Display a success flash message and redirect to the dashboard page.
        2.5. If user does not exist or password is incorrect:
            2.5.1. Display an error flash message.
    3. If the form is not submitted or contains errors, render the login template with the form.
    """
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
        
        # Fetch user data from MongoDB
        user_data = Company.get(username)
        
        # Check if user exists and password is correct
        if user_data and check_password_hash(user_data.password, password):
            # Create a User object and log in the user
            user = Company.get_by_id(user_data.id)
            login_user(user)
            print (current_user.username, "\n", current_user.role)
            
            # Display success flash message and redirect to dashboard
            flash('Logged in successfully!', 'success')
            return redirect(url_for('companies.dashboard'))
        else:
            # Display error flash message
            flash('Invalid username or password!', 'danger')

    # Render the login template with the form
    return render_template('companies/login.html', form=form)

@companies.route('/logout')
@login_required
@role_checker('company')
def logout():
    """
    Logs out the current user.

    This function is decorated with @login_required to ensure that only authenticated users can access this route.
    It also uses the @role_checker decorator to restrict access to only users with the 'company' role.

    Parameters:
    None

    Returns:
    redirect: Redirects the user to the login page after successful logout.
    flash: Displays a success flash message indicating that the user has been logged out.
    """
    logout_user()
    flash('You have been logged out!', 'success')
    return redirect(url_for('companies.login'))


@companies.route('/dashboard')
@login_required
@role_checker('company')
def dashboard():

    table = get_table_info(current_user.id, current_user.role) # change current_user.id for adv_id
    print(table)
    if table != []:
        table_headers = [record for record in table[0].__dict__ if record != 'user_id' and record != 'id' and record != 'description' and record != 'description' and record != 'comp_id']

        table_data = [record.__dict__ for record in table]

        print(table_headers)
        print(table_data)

        print (current_user.username)
        return render_template('companies/dashboard.html', table_data=table_data, table_headers=table_headers)
    else:
        return render_template('companies/dashboard.html', table_data=None, table_headers=None)





@companies.route('/profile', methods=['GET', 'POST'])
@login_required
@role_checker('company')
def profile():
    """
    Handles company profile updates.

    Parameters:
    form (ProfileForm): The form object containing the company's profile details.

    Returns:
    render_template: If the form is not submitted or contains errors, render the profile template with the form and current user data.
    redirect: If the profile is successfully updated, redirect to the dashboard page.
    flash: If the username already exists, display a flash message.

    Function Steps:
    1. Initialize a ProfileForm object.
    2. If the form is submitted and valid:
        2.1. Get the username, current password, and new password from the form.
        2.2. Check if the current password is correct.
        2.3. If the new password is provided, hash it. If not, keep the current password.
        2.4. Prepare the profile data to be updated.
        2.5. Fetch the existing user data from MongoDB using the username.
        2.6. Check if the username already exists and it's not the current user's username.
        2.7. If the username already exists, display a flash message and redirect to the profile page.
        2.8. If the username is unique, update the user's profile in MongoDB.
        2.9. If an error occurs during the update, display an error flash message and redirect to the profile page.
        3.0. If the profile is successfully updated, display a success flash message and redirect to the dashboard page.
    3. If the form is not submitted or contains errors, render the profile template with the form and current user data.
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

        print(f"UPDATING USER: {username}")
        profile_data = {
            'username': form.username.data,
            'password': hashed_password
        }

        existing_user = Company.get(profile_data['username'])
        print(f"USER: {existing_user}")

        # Check if the username already exists and it's not the current user's username
        if existing_user and str(existing_user.id) != current_user.id:
            flash('Username already exists!', 'danger')
            return redirect(url_for('companies.profile'))

        try: 
            Company.update_profile(profile_data=profile_data)
        except Exception as e:
            print(f"Error updating user: {e}")
            flash('Error updating user!', 'danger')
            return redirect(url_for('companies.profile'))

        flash('Profile updated successfully!', 'success')
        return redirect(url_for('companies.dashboard'))

    return render_template('companies/profile.html', form=form, data=current_user)
