from flask_pymongo import PyMongo
from flask_login import LoginManager
from bson import BSON, ObjectId

mongo = PyMongo()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    """
    This function is used by Flask-Login to reload the user object from the user ID stored in the session.
    It tries to load a User first, if not found, it tries to load a Company.

    Parameters:
    user_id (str): The unique identifier of the user or company.

    Returns:
    User or Company object: The loaded user or company object if found, otherwise None.
    """
    from .users.models import User
    from .companies.models import Company
    
    # Tries to load a User
    user = User.get_by_id(user_id)
    if user:
        return user
    
    ##! If the user is null:
    
    # Tries to load a Company
    company = Company.get_by_id(user_id)
    if company:
        return company
    
    return None