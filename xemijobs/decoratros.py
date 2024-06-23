import functools
from flask import redirect, url_for, flash
from flask_login import current_user

def role_checker(role):
    def decorator(f):
        @functools.wraps(f)
        def decorated_function(*args, **kwargs):
            
            if current_user.role != role:
                flash('You do not have permission to view this page!', 'danger')
                if role == 'user':
                    return redirect(url_for('users.index'))
                elif role == 'company':
                    return redirect(url_for('companies.index'))
            
            return f(*args, **kwargs)
        
        return decorated_function
    
    return decorator