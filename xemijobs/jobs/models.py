from flask_login import UserMixin, current_user
from ..extensions import mongo
from bson import ObjectId, BSON


class Job:
    def __init__(self, post_title, location, salary, job_type, description, ends_on, published_on, comp_name, comp_id, _id):
        self.post_title = post_title
        self.location = location
        self.salary = salary
        self.job_type = job_type
        self.description = description
        self.ends_on = ends_on
        self.published_on = published_on
        self.comp_name = comp_name
        self.comp_id = comp_id
        self.id = str(_id)

    def get_id(self):
        return self.id

    #! CRUD-functions

    ## Create
    #! only COMPANIES
    @staticmethod
    def create_new_job(**job_data):
        """
        Create a new job post in the database.

        Parameters:
        job_data (dict): A dictionary containing the details of the new job post.
            The keys of the dictionary should match the fields in the database collection.

        Returns:
        None

        Raises:
        None

        Note:
        This function should be called by a logged-in company user.
        It inserts a new job post into the 'jobs' collection in the database.

        Example:
        >>> job_data = {
            'post_title': 'Software Developer',
            'location': 'New York',
            'salary': 80000,
            'job_type': 'Full-time',
            'description': 'Develop software applications...',
            'ends_on': datetime.datetime(2022, 12, 31),
            'published_on': datetime.datetime.now(),
            'comp_name': 'XYZ Corp.',
            'comp_id': '12345'
        }
        >>> Job.create_new_job(**job_data)
        """
        mongo.db.jobs.insert_one(**job_data)


    ## Read
    #! no Login needed
    @staticmethod
    def get_by_id(job_id):
        """
        Retrieve a Job object by its unique identifier.

        Parameters:
        job_id (str): The unique identifier of the job post.

        Returns:
        Job: A Job object representing the job post with the given identifier.
            If no job post is found with the given identifier, return None.

        Raises:
        None

        Note:
        This function does not require a user to be logged in.
        It retrieves a single job post from the database based on its unique identifier.

        Example:
        >>> job = Job.get_by_id('5f17c1234567890123456789')
        >>> print(job.post_title)
        "Software Developer"
        """
        job_data = mongo.db.jobs.find_one({'_id': ObjectId(job_id)})
        if job_data:
            return Job(
                post_title=job_data['post_title'],
                location=job_data['location'],
                salary=job_data['salary'],
                job_type=job_data['job_type'],
                description=job_data['description'],
                ends_on=job_data['ends_on'],
                published_on=job_data['published_on'],
                comp_name=job_data['comp_name'],
                comp_id=str(job_data['comp_id']),
                _id=str(job_data['_id'])
            )
    

    @staticmethod
    def get_all_jobs():
        """
        Retrieve all Job objects from the database.

        Returns:
            list: A list of Job objects. Each Job object represents a job post in the database.

        Raises:
            None

        Note:
            This function does not require a user to be logged in. It retrieves all job posts from the database.

        Example:
            >>> jobs = Job.get_all_jobs()
            >>> print(len(jobs))
            10
            >>> print(jobs[0].post_title)
            "Software Developer"
        """
        jobs_data = mongo.db.jobs.find()
        return [Job(
            post_title=job_data['post_title'],
            location=job_data['location'],
            salary=job_data['salary'],
            job_type=job_data['job_type'],
            description=job_data['description'],
            ends_on=job_data['ends_on'],
            published_on=job_data['published_on'],
            comp_name=job_data['comp_name'],
            comp_id=str(job_data['comp_id']),
            _id=str(job_data['_id'])
        ) for job_data in jobs_data]
    
    
    ## Update
    #! only COMPANIES
    @staticmethod
    def update_job(job_id, **job_data):
        """
        Update a job post in the database.

        Parameters:
        job_id (str): The unique identifier of the job post to be updated.
        job_data (dict): A dictionary containing the updated details of the job post.
            The keys of the dictionary should match the fields in the database collection.

        Returns:
        None

        Raises:
        None

        Note:
        This function should be called by a logged-in company user.
        It updates the job post with the given identifier in the 'jobs' collection in the database.
        The update operation uses the MongoDB update_one method with the "$set" operator to update the specified fields.

        Example:
        >>> job_data = {
            'post_title': 'Senior Software Developer',
            'location': 'San Francisco',
            'salary': 90000
        }
        >>> Job.update_job('5f17c1234567890123456789', **job_data)
        """
        mongo.db.jobs.update_one(
            {'_id': ObjectId(job_id)},
            {"$set": job_data}
        )


    ## Delete
    #! only COMPANIES
    @staticmethod
    def delete_job(job_id):
        """
        Delete a job post from the database.

        Parameters:
        job_id (str): The unique identifier of the job post to be deleted.

        Returns:
        None

        Raises:
        None

        Note:
        This function should be called by a logged-in company user.
        It deletes the job post with the given identifier from the 'jobs' collection in the database.
        The deletion operation uses the MongoDB delete_one method.

        Example:
        >>> Job.delete_job('5f17c1234567890123456789')
        """
        mongo.db.jobs.delete_one({'_id': ObjectId(job_id)})


    