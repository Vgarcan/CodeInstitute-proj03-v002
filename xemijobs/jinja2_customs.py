
from .jobs.models import Job
from .users.models import User
from .companies.models import Company

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
    if collection == 'users':
        return User.get_by_id(id).username
    elif collection == 'companies':
        return Company.get_by_id(id).username
    elif collection == 'jobs':
        return Job.get_by_id(id).post_title
