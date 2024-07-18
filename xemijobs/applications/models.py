from ..extensions import mongo
from bson import ObjectId

class Application:
    def __init__(self,adv_id, comp_id, user_id, status, id):
        self.adv_id = adv_id
        self.comp_id = comp_id
        self.user_id = user_id
        self.status = status
        self.id = id

    def get_id(self):
        return self.id
    
    #! CRUD-functions

    ## Create
    #! only USERS
    @staticmethod
    def create_new_application(application):
        """
        Creates a new application in the database for a specific company and user.

        Parameters:
        comp_id (str): The unique identifier of the company for which the application is being created.
        user_id (str): The unique identifier of the user creating the application.

        Returns:
        None. This function does not return any value. It inserts a new document into the 'applications' collection in the database.
        """
        
        mongo.db.applications.insert_one(application)

    ## Read
    @staticmethod
    def get_all_applications(passing_id):
        """
        Retrieves all applications from the database associated with a specific company.

        Parameters:
        passing_id (str): The unique identifier of the company for which the applications are being retrieved.

        Returns:
        list: A list of Application objects representing the retrieved applications.
        Each Application object contains the following attributes:
        - comp_id (str): The unique identifier of the company associated with the application.
        - user_id (str): The unique identifier of the user associated with the application.
        - id (str): The unique identifier of the application (ObjectId).
        """
        applications = mongo.db.applications.find({'comp_id': ObjectId(passing_id)})
        return [Application(
            adv_id=str(app['adv_id']),
            comp_id=str(app['comp_id']),
            user_id=str(app['user_id']),
            status=str(app['status']),
            id=str(app['_id'])
        )for app in applications]
    
    @staticmethod
    def get_all_sent_applications(user_id):
        """
        Retrieves all applications from the database associated with a specific company.

        Parameters:
        passing_id (str): The unique identifier of the company for which the applications are being retrieved.

        Returns:
        list: A list of Application objects representing the retrieved applications.
        Each Application object contains the following attributes:
        - comp_id (str): The unique identifier of the company associated with the application.
        - user_id (str): The unique identifier of the user associated with the application.
        - id (str): The unique identifier of the application (ObjectId).
        """
        applications = mongo.db.applications.find({'user_id': user_id})
        return [Application(
            adv_id=str(app["adv_id"]),
            comp_id=str(app['comp_id']),
            user_id=str(app['user_id']),
            status=str(app['status']),
            id=str(ObjectId(app["_id"]))
        )for app in applications]

    @staticmethod
    def get_by_id(id):
        """
        Retrieves an application from the database by its unique identifier.

        Parameters:
        self (Application): The instance of the Application class. This parameter is not used in the function's logic, but it is required for compatibility with class methods.
        id (str): The unique identifier of the application to be retrieved. This identifier is expected to be a string representation of an ObjectId.

        Returns:
        dict: A dictionary representing the retrieved application. If no application is found with the given identifier, this function returns None.
        The dictionary contains the following fields:
        - '_id': The unique identifier of the application (ObjectId).
        - 'comp_id': The unique identifier of the company associated with the application.
        - 'user_id': The unique identifier of the user associated with the application.
        """
        aplication = mongo.db.applications.find_one({'_id': ObjectId(id)})
        return aplication
    
    ## Delete
    #! only USERS
    @staticmethod
    def delete_application(id):
        mongo.db.applications.delete_one({'_id': ObjectId(id)})

    @staticmethod
    #! login required 
    def delete_all_company_applications(id, user_role):
        """
        Deletes all applications from the database associated with a specific company or user, based on the user's role.

        Parameters:
        id (str): The unique identifier of the company or user for which the applications are being deleted.
            If the user_role is 'company', this parameter represents the company's unique identifier.
            If the user_role is 'user', this parameter represents the user's unique identifier.
        user_role (str): The role of the user performing the deletion.
            It can be either 'company' or 'user'.

        Returns:
        None. This function does not return any value. It deletes documents from the 'applications' collection in the database.
        """
        if user_role == 'company':
            mongo.db.applications.delete_many({'comp_id': ObjectId(id)})
        elif user_role == 'user':
            mongo.db.applications.delete_many({'user_id': ObjectId(id)})




