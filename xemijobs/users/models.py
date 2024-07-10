from flask_login import UserMixin, current_user
from ..extensions import mongo
from bson import ObjectId, BSON
from xemijobs.extensions import login_manager

class User(UserMixin):
    def __init__(self, username, password, _id, role):
        self.username = username
        self.password = password
        self.id = str(_id) 
        self.role = role
    
    
    def get_id(self):
        return self.id

#! CRUD-functions

    ## Create
    #! no Login needed
    @staticmethod
    def create_new_user(username, password, role):
        """
        This function creates a new user in the database.

        Parameters:
        username (str): The username of the new user.
        password (str): The password of the new user.
        role (str): The role of the new user.

        Returns:
        None

        Raises:
        None

        Note:
        This function does not perform any checks to ensure that the username is unique.
        It is assumed that the caller will handle any necessary validation.
        """

        new_user_data = {
            'username': username,
            'password': password,
            'role': role
        }
        
        mongo.db.users.insert_one(new_user_data)


    ## Read
    #! no Login needed
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
            user_data = mongo.db.users.find_one({'_id': ObjectId(user_id)})
            if user_data:
                return User(
                    username=user_data['username'], 
                    password=user_data['password'],
                    _id=str(user_data['_id']),
                    role=user_data['role']
                )
        except Exception as e:
            print("==============> Exception in get_by_id:", e)
            return None
   

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
    def get_all_users():
    
        users_data = mongo.db.users.find()
        return [
            User(
                username=user_data['username'],
                password=user_data['password'],
                _id=str(user_data['_id']),
                role=user_data['role']
            )
            for user_data in users_data
        ]


    ## Update
    #! only USERS
    @staticmethod
    def update_profile(**profile_data):
        """
        Updates the profile of the currently logged-in user in the database.

        Parameters:
        profile_data (dict): A dictionary containing the fields and their new values to be updated.
            The keys of the dictionary should match the fields in the user document in the database.

        Returns:
        None

        Raises:
        None

        Note:
        This function assumes that the 'current_user' object is available and represents the currently logged-in user.
        It retrieves the unique ID of the current user and uses it to update the corresponding user document in the database.
        """
        current_user_id = str(current_user.get_id())
        mongo.db.users.update_one(
            {'_id': ObjectId(current_user_id)},
            {"$set": profile_data}
        )
        

    ## Delete
    #! only USERS
    @staticmethod
    def delete_user():
        """
        Deletes the currently logged-in user from the database.

        Parameters:
        None

        Returns:
        None

        Raises:
        None

        Note:
        This function assumes that the 'current_user' object is available and represents the currently logged-in user.
        It retrieves the unique ID of the current user and uses it to delete the corresponding user document in the database.
        """
        current_user_id = str(current_user.get_id())
        mongo.db.users.delete_one({'_id': ObjectId(current_user_id)})