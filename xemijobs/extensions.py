from flask_pymongo import PyMongo
from flask_login import LoginManager
from bson import BSON, ObjectId

mongo = PyMongo()
login_manager = LoginManager()

# @login_manager.user_loader
# def load_user(user_id):
#     # if it is a NORMAL-USER:
#     from .users.models import User
#     try:
#         user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
#         if user_data:
#             return User(
#                 username=user_data['username'], 
#                 password=user_data['password'],
#                 _id=str(user_data['_id']) 
#             )
#     except BSON.errors.InvalidId:
#         return None

#     # IF it is a Company-USER:
#     from .companies.models import Company
#     try:
#         user_data = mongo.db.companies.find_one({'_id': ObjectId(user_id)})
#         if user_data:
#             return User(
#                 username=user_data['username'], 
#                 password=user_data['password'],
#                 _id=str(user_data['_id']) 
#             )
#     except BSON.errors.InvalidId:
#         return None
