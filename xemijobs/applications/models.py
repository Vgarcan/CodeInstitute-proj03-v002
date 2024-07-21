from ..extensions import mongo
from bson import ObjectId

class Application:
    def __init__(self, adv_id, comp_id, user_id,created_on, status, id):
        self.adv_id = adv_id
        self.comp_id = comp_id
        self.user_id = user_id
        self.created_on = created_on
        self.status = status
        self.id = str(id)

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
    def get_all_applications(passing_id, role):
        """
        Retrieves all applications from the database based on the given user or company identifier and role.

        Parameters:
        passing_id (str): The unique identifier of the user or company for which the applications are being retrieved.
        role (str): The role of the user or company. It can be either 'company' or 'user'.

        Returns:
        list: A list of Application objects representing the retrieved applications.
        Each Application object contains the following attributes:
        - adv_id (str): The unique identifier of the advertisement associated with the application.
        - comp_id (str): The unique identifier of the company associated with the application.
        - user_id (str): The unique identifier of the user associated with the application.
        - status (str): The status of the application.
        - id (str): The unique identifier of the application (ObjectId).
        """
        if role == 'company':
            applications = mongo.db.applications.find({'adv_id': passing_id})
        elif role == 'user':
            applications = mongo.db.applications.find({'user_id': passing_id})

        return [Application(
            adv_id=str(app['adv_id']),
            comp_id=str(app['comp_id']),
            user_id=str(app['user_id']),
            created_on=str(app['created_on']),
            status=str(app['status']),
            id=str(app['_id'])
        ) for app in applications]
    
    @staticmethod
    def get_all_sent_applications(user_id):
        """
        Retrieves a single application from the database based on the user's unique identifier.

        Parameters:
        user_id (str): The unique identifier of the user for which the application is being retrieved.

        Returns:
        dict: A dictionary representing the retrieved application.
        The dictionary contains the following keys:
        - adv_id (str): The unique identifier of the advertisement associated with the application.
        - comp_id (str): The unique identifier of the company associated with the application.
        - user_id (str): The unique identifier of the user associated with the application.
        - status (str): The status of the application.
        - id (str): The unique identifier of the application (ObjectId).
        """
        application = mongo.db.applications.find_one({'user_id': ObjectId(user_id)})
        return application
    
    ## Delete
    #! only USERS
    @staticmethod
    def delete_application(adv_id):
        """
        Deletes a specific application from the database based on its unique identifier.

        Parameters:
        adv_id (str): The unique identifier of the application to be deleted. This identifier is expected to be a string representation of an ObjectId.

        Returns:
        None. This function does not return any value. It deletes a document from the 'applications' collection in the database.
        """
        mongo.db.applications.delete_one({'_id': ObjectId(adv_id)})

    @staticmethod
    def delete_all_applications(id, user_role):
        """
        Deletes all applications from the database associated with a specific user or company.

        Parameters:
        id (str): The unique identifier of the user or company for which the applications are being deleted.
        user_role (str): The role of the user or company. It can be either 'company' or 'user'.

        Returns:
        None. This function does not return any value. It deletes documents from the 'applications' collection in the database.
        """
        if user_role == 'company':
            mongo.db.applications.delete_many({'comp_id': id})
        elif user_role == 'user':
            mongo.db.applications.delete_many({'user_id': id})




