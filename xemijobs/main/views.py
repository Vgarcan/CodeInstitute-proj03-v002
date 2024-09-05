from flask import Blueprint, render_template, flash
from ..extensions import mongo, get_total_jobs
from flask_login import login_required, current_user

from ..users.models import User
from ..users.forms import ProfileForm

main = Blueprint("main", __name__, template_folder="templates", static_folder="static")


@main.route("/")
def index():
    """
    This function renders the home page of the application. It displays a carousel with various job-related images,
    and fetches the total number of job listings from the database.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template 'main/index.html' with the following parameters:
        carousel: A list of dictionaries, each containing image source, alt text, header, and text for the carousel.
        enumerate: A built-in Python function used for iterating over a sequence and returning a tuple containing a count and the value.
        total_jobs: The total number of job listings fetched from the database.
    """

    carousel = [
        {
            "img_src": "imgs/banner.webp",
            "img_alt": "Banner #1",
            "header": "Join XemiJobs",
            "text": "Find the perfect job for you",
        },
        {
            "img_src": "imgs/banner2.webp",
            "img_alt": "Banner #2",
            "header": "Always looking for professionals",
        },
        {
            "img_src": "imgs/banner3.webp",
            "img_alt": "Banner #3",
            "text": "The best companies are looking for talented people",
        },
        {
            "img_src": "imgs/banner2.webp",
            "img_alt": "Banner #4",
        },
    ]
    total_jobs = get_total_jobs()
    print("total josbs in MAIN>VIEWS.PY = ", total_jobs)
    return render_template(
        "main/index.html", carousel=carousel, enumerate=enumerate, total_jobs=total_jobs
    )


@main.route("/404")
def error404():
    """
    This function renders a custom 404 error page.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template 'main/404.html' to display the custom 404 error page.
    """
    return render_template("main/404.html")


@main.route("/403")
def error403():
    """
    This function renders a custom 403 error page.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template 'main/403.html' to display the custom 403 error page.
    """
    return render_template("main/403.html")


@main.route("/401")
def error401():
    """
    This function renders a custom 401 error page.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template 'main/401.html' to display the custom 401 error page.
    """
    return render_template("main/401.html")


@main.route("/terms-and-conditions")
def tnc():
    """
    This function renders a Terms and Conditions page.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template 'main/tnc.html' to display the Terms and Conditions page.
    """
    return render_template("main/tnc.html")


@main.route("/about-us")
def about_us():
    """
    This function renders the 'about-us.html' template.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template 'main/about-us.html' to display the About Us page.
    """
    return render_template("main/about-us.html")


@main.route("/test_mongo")
def test_mongo():
    try:
        from flask import jsonify

        collections = mongo.db.list_collection_names()
        return jsonify(collections)
    except Exception as e:
        return str(e), 500


@main.route("/profile")
@login_required
def profile():
    """
    This function renders the user's profile page. It is accessible only to authenticated users.

    Parameters:
    None

    Returns:
    render_template: A rendered HTML template 'profile.html' with the following parameters:
        user: The current logged-in user's data. This data is used to populate the user's profile page.

    Decorators:
    @login_required: This decorator ensures that only authenticated users can access this route.
    """
    return render_template(
        "profile.html",
        user=current_user
    )


@main.route("/widgets/<int:page>")
def widget_showcase(page=1):
    """
    This function displays all widgets in the site.

    Parameters:
    page (int): The page number for pagination. Default value is 1.

    Returns:
    render_template: If users are found, render the 'users-list.html' template with the user data, page number,
                     enumerate function, and profile form.
    redirect: If no users are found, display an info flash message and redirect to the index page.
    """

    flash("Flash SUCCESS", "success")
    flash("Flash INFO", "info")
    flash("Flash WARNING", "warning")
    flash("Flash ERROR", "error")
    flash("Flash DANGER", "danger")

    form = ProfileForm()

    # PAGINATION = 9
    per_page = 9 + 1  # add ONE to check if pagination forward is needed
    offset = (page - 1) * (per_page - 1)
    # data = rawdata[offset:offset + per_page]

    data = User.get_all_users(offset, per_page)
    if data == None:
        flash("No users found!", "info")

    return render_template(
        "main/widgets-collection.html",
        data=data,
        page=page,
        enumerate=enumerate,
        form=form,
        d_type="users",
    )
