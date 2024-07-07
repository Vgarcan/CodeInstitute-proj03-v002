from flask_login import UserMixin, current_user
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
        """
        Retrieve a Company object by its username.

        Parameters:
        username (str): The unique username of the company.

        Returns:
        Company: A Company object if found, otherwise None.

        Raises:
        None

        Example:
        company = Company.get('john_doe')
        if company:
            print(f"Company found: {company.username}")
        else:
            print("Company not found.")
        """
        user_data = mongo.db.companies.find_one({'username': username})
        if user_data:
            return Company(
                username=user_data['username'], 
                password=user_data['password'],
                _id=str(user_data['_id']),
                role=user_data['role']
            )
        return None
        
 
    def get_id(self):
        return self.id

# TODO:
# Include the CRUD-Funtions in the model

#! create the {CRUD-functions}

    ## Create
    #! no Login needed
    ##? create_new_userComp function
    @staticmethod
    def create_new_user(username, password, role):
        # Create a new user document in the database
        new_user_data = {
            'username': username,
            'password': password,
            'role': role
        }
        mongo.db.companies.insert_one(new_user_data)
    ## Read
    #! no Login needed
    ##? get_by_id function - fetch one userComp by the id
    @staticmethod
    def get_by_id(user_id):
        """
        Retrieve a Company object by its unique identifier.

        Parameters:
        user_id (str): The unique identifier of the company.

        Returns:
        Company: A Company object if found, otherwise None.

        Raises:
        Exception: If an error occurs during the database query.
        """
        try:
            # Attempt to find the company in the database using the provided user_id
            user_data = mongo.db.companies.find_one({'_id': ObjectId(user_id)})
            
            # If a company is found, create a new Company object and return it
            if user_data:
                return Company(
                    username=user_data['username'], 
                    password=user_data['password'],
                    _id=str(user_data['_id']),
                    role=user_data['role']
                )
        except Exception as e:
            # If an error occurs, print the error message and return None
            print("==============> Exception in get_by_id:", e)
            return None
   

    ##? get_by_username function - fetch one userComp by username
    @staticmethod
    def get(username):
        """
        Retrieve a Company object by its username.

        Parameters:
        username (str): The unique username of the company.

        Returns:
        Company: A Company object if found, otherwise None.

        Raises:
        None

        Example:
        company = Company.get('john_doe')
        if company:
            print(f"Company found: {company.username}")
        else:
            print("Company not found.")
        """
        user_data = mongo.db.companies.find_one({'username': username})
        if user_data:
            return Company(
                username=user_data['username'], 
                password=user_data['password'],
                _id=str(user_data['_id']),
                role=user_data['role']
            )
        return None
    

    ## Update
    #! only COMPANIES
    ##? update_profile function
    @staticmethod
    def update_profile(**profile_data):
        # Retrieve the current user's ID
        current_user_id = str(current_user.get_id())
        # Update the user's profile in the database
        mongo.db.companies.update_one(
            {'_id': ObjectId(current_user_id)},
            {"$set": profile_data})
    
    ## Delete
    #! only COMPANIES
    ##? delete_user function
    @staticmethod
    def delete_user():
        # Retrieve the current user's ID
        current_user_id = str(current_user.get_id())
        # Delete the user from the database
        mongo.db.companies.delete_one({'_id': ObjectId(current_user_id)})