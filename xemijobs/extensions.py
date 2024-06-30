from flask_pymongo import PyMongo
from flask_login import LoginManager
# from bson import BSON, ObjectId

mongo = PyMongo()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    from .users.models import User
    from .companies.models import Company
    
    # Intentar cargar un usuario
    user = User.get_by_id(user_id)
    if user:
        return user
    
    # Intentar cargar una compañía
    company = Company.get_by_id(user_id)
    if company:
        return company
    
    return None