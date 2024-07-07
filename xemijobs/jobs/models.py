
# from form data:
    # post_title
    # location
    # salary
    # job_type
    # description
    # ends_on
# from views 
    # published_on
    # comp_name
    # comp_id
# from model
    # job_id

# TODO:
# Import Section
from flask_login import UserMixin, current_user
from ..extensions import mongo
from bson import ObjectId, BSON
# class JOB
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

    #! create the {CRUD-functions}

    ## Create
    #! only COMPANIES
    ##? create_new_job function
    @staticmethod
    def create_new_job(**job_data):
        mongo.db.jobs.insert_one(**job_data)

    ## Read
    #! no Login needed
    ##? get_by_id function - ftech one job
    @staticmethod
    def get_by_id(job_id):
        """
        Retrieve a Job object by its unique identifier.
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
    ##? get_all_jobs function - ftech all jobs
    @staticmethod
    def get_all_jobs():
        """
        Retrieve all Job objects.
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
    ##? update_job function
    @staticmethod
    def update_job(job_id, **job_data):
        mongo.db.jobs.update_one(
            {'_id': ObjectId(job_id)},
            {"$set": job_data}
        )
    ## Delete
    #! only COMPANIES
    ##? delete_job function
    @staticmethod
    def delete_job(job_id):
        mongo.db.jobs.delete_one({'_id': ObjectId(job_id)})


    