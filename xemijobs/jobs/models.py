from ..extensions import mongo
from bson import ObjectId


class Job:
    def __init__(
        self,
        post_title,
        location,
        salary,
        job_type,
        description,
        ends_on,
        published_on,
        comp_name,
        comp_id,
        _id,
    ):
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
        """
        Returns the unique identifier of the job.

        Parameters:
        None. This method does not take any parameters.

        Returns:
        str: The unique identifier of the job. This identifier is a string representation of the ObjectId.
        """
        return self.id

    #! CRUD-functions

    ## Create
    #! only COMPANIES
    @staticmethod
    def create_new_job(job_data):
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
        mongo.db.jobs.insert_one(job_data)

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
        job_data = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
        if job_data:
            return Job(
                post_title=job_data["post_title"],
                location=job_data["location"],
                salary=job_data["salary"],
                job_type=job_data["job_type"],
                description=job_data["description"],
                ends_on=job_data["ends_on"],
                published_on=job_data["published_on"],
                comp_name=job_data["company_name"],
                comp_id=str(job_data["comp_id"]),
                _id=str(job_data["_id"]),
            )

    @staticmethod
    def get_all_jobs(offset, per_page):
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
        jobs_data = (
            mongo.db.jobs.find().sort("published_on", -1).skip(offset).limit(per_page)
        )

        return [
            Job(
                post_title=job_data["post_title"],
                location=job_data["location"],
                salary=job_data["salary"],
                job_type=job_data["job_type"],
                description=job_data["description"],
                ends_on=str(job_data["ends_on"]),
                published_on=str(job_data["published_on"]),
                comp_name=job_data["company_name"],
                comp_id=str(job_data["comp_id"]),
                _id=str(job_data["_id"]),
            )
            for job_data in jobs_data
        ]

    @staticmethod
    def get_comp_jobs(comp_id):
        """
        Retrieve all job posts associated with a specific company from the database.

        Parameters:
        comp_id (str): The unique identifier of the company whose job posts will be retrieved.

        Returns:
        list: A list of Job objects. Each Job object represents a job post associated with the given company.
              The list is sorted by the 'published_on' field in descending order.

        Note:
        This function does not require a user to be logged in.
        It retrieves all job posts associated with the given company identifier from the 'jobs' collection in the database.
        The results are sorted by the 'published_on' field in descending order.

        Example:
        >>> jobs = Job.get_comp_jobs('5f17c1234567890123456789')
        >>> print(len(jobs))
        10
        >>> print(jobs[0].post_title)
        "Software Developer"
        """
        jobs_data = mongo.db.jobs.find({"comp_id": comp_id}).sort("published_on", -1)
        return [
            Job(
                post_title=job_data["post_title"],
                location=job_data["location"],
                salary=job_data["salary"],
                job_type=job_data["job_type"],
                description=job_data["description"],
                ends_on=job_data["ends_on"],
                published_on=job_data["published_on"],
                comp_name=job_data["company_name"],
                comp_id=str(job_data["comp_id"]),
                _id=str(job_data["_id"]),
            )
            for job_data in jobs_data
        ]


    @staticmethod
    def get_jobs_by_query(q, offset, per_page):
        """
        Retrieve job posts from the database based on a search query.

        This function uses MongoDB's text search feature to find job posts that match the given search query.
        It creates a text index on the specified fields and then performs a search operation using the "$text" operator.
        The results are sorted by the "published_on" field in descending order, and pagination is applied using the "skip" and "limit" methods.

        Parameters:
        q (str): The search query. This parameter is case-insensitive.
        offset (int): The number of job posts to skip before starting to return results.
        per_page (int): The maximum number of job posts to return in a single page.

        Returns:
        list: A list of Job objects. Each Job object represents a job post that matches the search query.

        Note:
        This function does not require a user to be logged in.
        It retrieves job posts from the 'jobs' collection in the database.
        """
        mongo.db.jobs.create_index(
            [
                ("post_title", ("text")),
                ("location", ("text")),
                ("salary", ("text")),
                ("job_type", ("text")),
                ("description", ("text")),
                ("company_name", ("text")),
            ]
        )

        jobs_data = (
            mongo.db.jobs.find({"$text": {"$search": q.lower()}})
            .sort("published_on", -1)
            .skip(offset)
            .limit(per_page)
        )
        return [
            Job(
                post_title=job_data["post_title"],
                location=job_data["location"],
                salary=job_data["salary"],
                job_type=job_data["job_type"],
                description=job_data["description"],
                ends_on=job_data["ends_on"],
                published_on=job_data["published_on"],
                comp_name=job_data["company_name"],
                comp_id=str(job_data["comp_id"]),
                _id=str(job_data["_id"]),
            )
            for job_data in jobs_data
        ]


    @staticmethod
    def number_of_jobs():
        """
        Retrieve the total number of job posts in the database.
        Parameters:
        None. This function does not take any parameters.
        Returns:
        int: The total number of job posts in the database.
        """
        total = mongo.db.jobs.count_documents({})
        print(print("total josbs in MODELS.PY = ", total))
        return total
    

    @staticmethod
    def number_of_jobs():
        """
        Retrieve the total number of job posts in the database.

        Parameters:
        None. This function does not take any parameters.

        Returns:
        int: The total number of job posts in the database.

        Note:
        This function does not require a user to be logged in.
        It retrieves the total count of job posts from the 'jobs' collection in the database.
        The count operation uses the MongoDB count_documents method.

        Example:
        >>> total_jobs = Job.number_of_jobs()
        >>> print(total_jobs)
        100
        """
        total = mongo.db.jobs.count_documents({})
        print(print("total josbs in MODELS.PY = ", total))  # This print statement is redundant and should be removed
        return total


    ## Update
    #! only COMPANIES
    @staticmethod
    def update_job(job_id, job_data):
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
        try:
            mongo.db.jobs.update_one(
                {"_id": ObjectId(job_id)},
                {"$set": job_data}
                )
        except Exception as e:
            raise Exception("Error updating job ", e)

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
        mongo.db.jobs.delete_one(
            {"_id": ObjectId(job_id)}
            )

    #! only COMPANIES
    @staticmethod
    def delete_all_jobs(comp_id):
        """
        Delete all job posts associated with a specific company from the database.

        Parameters:
        comp_id (str): The unique identifier of the company whose job posts will be deleted.

        Returns:
        None

        Raises:
        None

        Note:
        This function should be called by a logged-in company user.
        It deletes all job posts associated with the given company identifier from the 'jobs' collection in the database.
        The deletion operation uses the MongoDB delete_many method.

        Example:
        >>> Job.delete_all_job('5f17c1234567890123456789')
        """
        mongo.db.jobs.delete_many(
            {"comp_id": comp_id}
            )
