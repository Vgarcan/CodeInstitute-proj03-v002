from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_required, current_user
from .forms import JobForm
from .models import Job
from ..extensions import mongo
from ..decoratros import role_checker

from datetime import datetime, date, time

jobs = Blueprint("jobs", __name__, template_folder="templates", static_folder="static")


@jobs.route("/job-list/<int:page>")
def job_list(page):
    """
    This function handles the job list page, displaying a paginated list of job advertisements.

    Parameters:
    page (int): The current page number for pagination.

    Returns:
    render_template: A rendered HTML template displaying the job list page.
    """
    # PAGINATION = 9
    per_page = 9 + 1  # add ONE to check if pagination forward is needed
    offset = (page - 1) * (per_page - 1)
    # data = rawdata[offset:offset + per_page]

    listed_jobs = Job.get_all_jobs(offset, per_page)
    print(" offset value = ", offset)
    print(" per_page value = ", per_page)
    for j in listed_jobs:
        print(j.id)
    return render_template(
        "jobs/jobs-list.html", data=listed_jobs, page=page, d_type="jobs"
    )


@jobs.route("/search")
def search(page=1):
    """
    This function handles the search functionality for job advertisements. It retrieves a paginated list of job advertisements
    based on the search query provided in the request parameters.

    Parameters:
    page (int): The current page number for pagination. Default value is 1.

    Returns:
    render_template: A rendered HTML template displaying the search results page. The template is located in the 'jobs' folder
    and is named 'jobs-list.html'. The function passes the search results, current page number, and a string 'jobs' to the template.
    """
    # PAGINATION = 9
    per_page = 9 + 1  # add ONE to check if pagination forward is needed
    offset = (page - 1) * (per_page - 1)
    # data = rawdata[offset:offset + per_page]

    query = request.args.get("q")
    print(query)
    results = []
    if query:
        results = Job.get_jobs_by_query(query, offset=offset, per_page=per_page)

    for j in results:
        print(j.id)
    return render_template("jobs/jobs-list.html", data=results, page=page)


@jobs.route("/job-detail/<adv_id>")
def job_detail(adv_id):
    """
    This function retrieves and displays the details of a specific job advertisement based on the provided advertisement ID.

    Parameters:
    adv_id (str): The unique identifier of the job advertisement. This is obtained from the URL parameter 'adv_id'.

    Returns:
    render_template: A rendered HTML template displaying the job details page. The template is located in the 'jobs' folder
    and is named 'view-job.html'. The function passes the job details to the template.
    """
    job_details = Job.get_by_id(adv_id)
    return render_template("jobs/view-job.html", data=job_details)


@jobs.route("/create-job", methods=["GET", "POST"])
@login_required
@role_checker("company")
def create_job():
    """
    This function handles the creation of a new job advertisement. It validates the form data, creates a new job object,
    and saves it to the database.

    Parameters:
    None

    Returns:
    render_template: If the form is not submitted or validation fails, it renders the 'create-job.html' template with the form.
    redirect: If the form is submitted successfully, it redirects to the company dashboard with a success flash message.
    """
    form = JobForm()

    if form.validate_on_submit():

        job_data = {
            "post_title": form.post_title.data,
            "location": form.location.data,
            "salary": form.salary.data,
            "job_type": form.job_type.data,
            "description": form.description.data,
            "published_on": datetime.now(),
            "ends_on": datetime.strptime(str(form.ends_on.data), "%Y-%m-%d").replace(
                hour=0, minute=00, second=00, microsecond=000000
            ),
            "company_name": current_user.username,
            "comp_id": current_user.id,
        }

        # print (datetime.now())
        # print (form.ends_on.data)

        try:
            Job.create_new_job(job_data=job_data)
            flash("Job created successfully", "success")
            return redirect(url_for("companies.dashboard"))
        except Exception as e:
            print("There was an error creating ======> " + str(e))
            flash("Job was not Created: " + str(e), "error")

    return render_template("jobs/create-job.html", form=form)


@jobs.route("/edit-job/<adv_id>", methods=["GET", "POST"])
@login_required
@role_checker("company")
def edit_job(adv_id):
    """
    This function handles the editing of a job advertisement. It retrieves the job details based on the provided advertisement ID,
    validates the form data, updates the job object, and saves it to the database.

    Parameters:
    adv_id (str): The unique identifier of the job advertisement. This is obtained from the URL parameter 'adv_id'.

    Returns:
    render_template: If the form is not submitted or validation fails, it renders the 'create-job.html' template with the form and the existing job details.
    redirect: If the form is submitted successfully, it redirects to the company dashboard with a success flash message.
    """

    job_details = Job.get_by_id(adv_id)

    form = JobForm()

    if form.validate_on_submit():
        details = {
            "post_title": form.post_title.data,
            "location": form.location.data,
            "salary": form.salary.data,
            "job_type": form.job_type.data,
            "description": form.description.data,
            # 'published_on': datetime.now(),
            "ends_on": datetime.strptime(str(form.ends_on.data), "%Y-%m-%d").replace(
                hour=0, minute=00, second=00, microsecond=000000
            ),
            "company_name": current_user.username,
            "comp_id": current_user.id,
        }

        try:
            Job.update_job(adv_id, job_data=details)
            flash("Job updated successfully", "info")
            return redirect(url_for("companies.dashboard"))
        except Exception as e:
            print("There was an error creating ======> " + str(e))
            flash("Job was not updated: " + str(e), "error")
            return redirect(url_for("jobs.edit_job", adv_id=adv_id))

    return render_template("jobs/create-job.html", form=form, passed_info=job_details)


@jobs.route("/delete-advert/<adv_id>", methods=["GET", "POST"])
@login_required
@role_checker("company")
def delete_comp_adv(adv_id):
    """
    Deletes a specific job advertisement from the database based on the provided advertisement ID.

    Parameters:
    adv_id (str): The unique identifier of the job advertisement. This is obtained from the URL parameter 'adv_id'.

    Returns:
    redirect: Redirects to the company dashboard after successfully deleting the job advertisement.
    flash: Displays a success message if the job advertisement is deleted successfully.
    flash: Displays an error message if there is an exception while deleting the job advertisement.
    """
    try:
        Job.delete_job(adv_id)
        flash("Advert successfully deleted!!")
    except Exception as e:
        flash("There was an error deleting the job: " + str(e))

    return redirect(url_for("companies.dashboard"))


# delete all JOBS form COMPANY
@jobs.route("/delete-all-adverts", methods=["POST"])
@login_required
@role_checker("company")
def delete_all_adv():
    """
    Deletes all job advertisements associated with the currently logged-in company from the database.

    This function is intended to be called when a company wants to delete all of their job advertisements at once.
    It uses the `delete_all_jobs` method from the `Job` model to perform the deletion. The function also handles
    any exceptions that may occur during the deletion process and displays appropriate flash messages to the user.

    Parameters:
    None

    Returns:
    redirect: Redirects the user to the company dashboard after successfully deleting all job advertisements.
    flash: Displays a success message if all job advertisements are deleted successfully.
    flash: Displays an error message if there is an exception while deleting the job advertisements.
    """
    try:
        Job.delete_all_jobs(current_user.id, current_user.role)
        flash("All adverts successfully deleted!!")
    except Exception as e:
        flash("There was an error deleting the adverts: " + str(e))

    return redirect(url_for("companies.dashboard"))
