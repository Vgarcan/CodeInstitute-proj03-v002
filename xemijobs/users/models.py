from flask_login import UserMixin
from ..extensions import mongo
from bson import ObjectId, BSON
from xemijobs.extensions import login_manager

class User(UserMixin):
    def __init__(self, username, password, _id, role):
        self.username = username
        self.password = password
        self.id = str(_id) 
        self.role = role
    
    @staticmethod
    def get(username):
        """
        Retrieve a user from the database by their username.

        Parameters:
        username (str): The username of the user to retrieve.

        Returns:
        User: An instance of the User class representing the retrieved user.
            If no user is found, returns None.

        Raises:
        None
        """
        user_data = mongo.db.users.find_one({'username': username})
        if user_data:
            return User(
                username=user_data['username'], 
                password=user_data['password'],
                _id=str(user_data['_id']),
                role=user_data['role']
            )
        return None
    
    @staticmethod
    def get_by_id(user_id):
        """
        This function retrieves a user from the database by their unique ID.

        Parameters:
        user_id (str): The unique ID of the user to retrieve.

        Returns:
        User: An instance of the User class representing the retrieved user.
            If no user is found, returns None.

        Raises:
        Exception: If any error occurs during the database query.
        """
        try:
            # Attempt to find the user in the database using their unique ID
            user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
            if user_data:
            # If a user is found, create a new User instance and return it
                return User(
                    username=user_data['username'], 
                    password=user_data['password'],
                    _id=str(user_data['_id']),
                    role=user_data['role']
                )
        except Exception as e:
            # If an error occurs, print the error message and return None
            print("==============> Exception in get_by_id:", e)
            return None
    
    def get_id(self):
        return self.id
