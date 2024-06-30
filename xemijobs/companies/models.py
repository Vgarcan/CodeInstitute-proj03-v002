from flask_login import UserMixin
from ..extensions import mongo
from bson import ObjectId, BSON
from xemijobs.extensions import login_manager

class Company(UserMixin):
    def __init__(self, username, password, _id, role):
        self.username = username
        self.password = password
        self.id = str(_id)
        self.role = role 
    
    @staticmethod
    def get(username):
        user_data = mongo.db.company.find_one({'username': username})
        if user_data:
            return Company(
                username=user_data['username'], 
                password=user_data['password'],
                _id=str(user_data['_id']),
                role = user_data['role']
            )
        return None
    
    def get_by_id(user_id):
        try:
            user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
            if user_data:
                return Company(
                    username=user_data['username'], 
                    password=user_data['password'],
                    _id=str(user_data['_id']),
                    role=user_data['role']
                )
        except Exception as e:
            print("==============> Exception in get_by_id:", e)
            return None
    
    def get_id(self):
        return self.id

