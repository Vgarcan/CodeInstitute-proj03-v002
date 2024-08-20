from flask import Blueprint, render_template, flash, redirect, url_for
from ..extensions import mongo, get_total_jobs
from flask_login import login_required, current_user

from ..users.models import User
from ..users.forms import ProfileForm

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
def index():

    carousel = [
        {
            'img_src': "imgs/banner.jpg",
            'img_alt': '',
            'header': 'Display the TITLE',
            'text': 'And display a CAPTATION too.'
        },
        {
            'img_src': "imgs/banner2.jpg",
            'img_alt': '',
            'header': ' You can only show the TITLE',

        },
        {
            'img_src': "imgs/banner3.jpg",
            'img_alt': '',
            'text': ' Or just show the CAPTATION in this section.\nYou can display nothing, like the next'
        },
        {
            'img_src': "imgs/banner2.jpg",
            'img_alt': '',
        },
    ]
    total_jobs = get_total_jobs()
    print("total josbs in MAIN>VIEWS.PY = ",total_jobs)
    return render_template('main/index.html', carousel=carousel, enumerate=enumerate, total_jobs= total_jobs )

@main.route('/404')
def error404():
    return render_template('main/404.html')

@main.route('/403')
def error403():
    return render_template('main/403.html')

@main.route('/401')
def error401():
    return render_template('main/401.html')


@main.route('/test_mongo')
def test_mongo():
    try:
        from flask import jsonify
        collections = mongo.db.list_collection_names()
        return jsonify(collections)
    except Exception as e:
        return str(e), 500
    
@main.route('/profile')
# @login_required
def profile():
    return render_template('profile.html', user=current_user)


@main.route('/widgets/<int:page>')
def widget_showcase(page=1):
    """
    This function retrieves a list of all users from the database and renders a template with the user data.

    Parameters:
    None

    Returns:
    render_template: If users are found, render the 'users-list.html' template with the user data.
    redirect: If no users are found, display an info flash message and redirect to the index page.
    """

    flash('Flash SUCCESS', 'success')
    flash('Flash INFO', 'info')
    flash('Flash WARNING', 'warning')
    flash('Flash ERROR', 'error')
    flash('Flash DANGER', 'danger')
    
    form = ProfileForm()

    # PAGINATION = 9
    per_page = 9
    offset = (page - 1) * per_page

    data = User.get_all_users(offset, per_page)
    if data is None:
        flash('No users found!', 'info')
    
    return render_template('main/widgets-collection.html', 
                           data=data, 
                           page=page,
                           enumerate=enumerate, 
                           form=form)

