from flask_login import UserMixin
from ..extensions import mongo
from bson import ObjectId, BSON
from xemijobs.extensions import login_manager

class Company(UserMixin):
    def __init__(self, username, password, _id):
        self.username = username
        self.password = password
        self.id = str(_id) 
    
    @staticmethod
    def get(username):
        user_data = mongo.db.users.find_one({'username': username})
        if user_data:
            return Company(
                username=user_data['username'], 
                password=user_data['password'],
                _id=str(user_data['_id'])  
            )
        return None
    
    def get_id(self):
        return self.id

@login_manager.user_loader
def load_user(user_id):
    try:
        user_data = mongo.db.companies.find_one({'_id': ObjectId(user_id)})
        if user_data:
            return Company(
                username=user_data['username'], 
                password=user_data['password'],
                _id=str(user_data['_id']) 
            )
    except BSON.errors.InvalidId:
        return None
