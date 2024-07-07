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

#! CRUD-functions

    ## Create
    #! no Login needed
    @staticmethod
    def create_new_user(username, password, role):
        """
        Create a new user in the companies collection.

        Parameters:
        username (str): The unique username of the company.
        password (str): The password for the company.
        role (str): The role of the company (e.g., 'admin', 'employee').

        Returns:
        None

        Raises:
        None

        Example:
        Company.create_new_user('john_doe', 'password123', 'admin')
        """
        new_user_data = {
            'username': username,
            'password': password,
            'role': role
        }
        mongo.db.companies.insert_one(new_user_data)


    ## Read
    #! no Login needed
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

        Example:
        company = Company.get_by_id('5f17c170a1b54a0017979d99')
        if company:
            print(f"Company found: {company.username}")
        else:
            print("Company not found.")
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
    @staticmethod
    def update_profile(**profile_data):
        """
        Update the current user's profile in the database.

        Parameters:
        profile_data (dict): A dictionary containing the fields and values to update.
                            The keys of the dictionary should match the fields in the database.

        Returns:
        None

        Raises:
        None

        Example:
        company = Company.get('john_doe')
        if company:
            company.update_profile(email='new_email@example.com', phone='1234567890')
            print("Company profile updated successfully.")
        else:
            print("Company not found.")

        Note:
        This method assumes that the current user is authenticated and authorized to update their own profile.
        """
        # Retrieve the current user's ID
        current_user_id = str(current_user.get_id())
        # Update the user's profile in the database
        mongo.db.companies.update_one(
            {'_id': ObjectId(current_user_id)},
            {"$set": profile_data})
        
    
    ## Delete
    #! only COMPANIES
    @staticmethod
    def delete_user():
        """
        Delete the current user from the companies collection.

        Parameters:
        None

        Returns:
        None

        Raises:
        None

        Example:
        company = Company.get('john_doe')
        if company:
            company.delete_user()
            print("Company deleted successfully.")
        else:
            print("Company not found.")

        Note:
        This method assumes that the current user is authenticated and authorized to delete their own profile.
        """
        # Retrieve the current user's ID
        current_user_id = str(current_user.get_id())
        # Delete the user from the database
        mongo.db.companies.delete_one({'_id': ObjectId(current_user_id)})