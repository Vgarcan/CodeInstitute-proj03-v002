from flask_pymongo import PyMongo
from flask_login import LoginManager
from bson import BSON, ObjectId

mongo = PyMongo()
login_manager = LoginManager()

@login_manager.user_loader
def load_user(user_id):
    """
    This function is used by Flask-Login to reload the user object from the user ID stored in the session.
    It tries to load a User first, if not found, it tries to load a Company.

    Parameters:
    user_id (str): The unique identifier of the user or company.

    Returns:
    User or Company object: The loaded user or company object if found, otherwise None.
    """
    from .users.models import User
    from .companies.models import Company
    
    # Tries to load a User
    user = User.get_by_id(user_id)
    if user:
        return user
    
    ##! If the user is null:
    
    # Tries to load a Company
    company = Company.get_by_id(user_id)
    if company:
        return company
    
    return None


def get_info_for(collection, id):
    """
    This function retrieves the name associated with a given collection and ID.

    Parameters:
    collection (str): The name of the collection from which to retrieve the name.
        It can be one of the following: 'users', 'companies', or 'jobs'.
    id (str): The unique identifier of the document within the specified collection.

    Returns:
    str: The name associated with the given collection and ID.
        If the collection is 'users', it returns the username of the user.
        If the collection is 'companies', it returns the username of the company.
        If the collection is 'jobs', it returns the post title of the job.
    """

    from .jobs.models import Job
    from .users.models import User
    from .companies.models import Company


    if collection == 'users':
        return User.get_by_id(id).username.replace('_', ' ').capitalize()
    elif collection == 'companies':
        return Company.get_by_id(id).username.replace('_', ' ').capitalize()
    elif collection == 'jobs':
        return Job.get_by_id(id).post_title.replace('_', ' ').capitalize()

def get_table_info(id,role, adv_id = None):
    if role == 'user':
        from .applications.models import Application
        table = Application.get_all_applications(id, role)
        return table
    elif role == 'company':
        if adv_id == None:
            from .jobs.models import Job
            table = Job.get_comp_jobs(id)
            return table
        elif adv_id != None:
            from .applications.models import Application
            print("=======================> " + adv_id)
            table = Application.get_all_applications(adv_id, role)
            return table
        
def get_total_jobs():
    from .jobs.models import Job
    return Job.number_of_jobs()

def get_adds_for_info(id):
    from .jobs.models import Job

    # get all ids from all jobs
    all_adds = Job.get_comp_jobs(id)
    id_list = [add.get_id() for add in all_adds]
    total_adds = len(id_list)

    # for each id in list add all applications
    from .applications.models import Application
    appl_total=0
    interviews_total=0

    for add_id in id_list:
        all_appl_for_add = Application.get_all_applications(add_id, 'company')
        appl_total += len(all_appl_for_add)
        
        # for each application check inteview_scheduled total
        for app in all_appl_for_add:
            if app.status == 'interview_scheduled':
                interviews_total += 1
    
    return [total_adds, appl_total, interviews_total]

    