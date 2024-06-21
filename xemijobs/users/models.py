from flask_login import UserMixin
from flask import current_app
from xemijobs.extensions import login_manager

class User(UserMixin):
    def __init__(self, username, password):
        self.username = username
        self.password = password
    
    @staticmethod
    def get(username):
        mongo = current_app.extensions['pymongo']
        user_data = mongo.db.users.find_one({'username': username})
        if user_data:
            return User(username=user_data['username'], password=user_data['password'])
        return None

@login_manager.user_loader
def load_user(username):
    return User.get(username)
