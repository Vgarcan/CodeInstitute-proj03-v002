from flask import Blueprint, render_template, flash, redirect, url_for
from ..extensions import mongo
from flask_login import login_required, current_user

from ..users.models import User
from ..users.forms import ProfileForm

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')

@main.route('/')
def index():
    return render_template('main/index.html')

@main.route('/page1')
def app_another():
    return "<h1>this is main's PAGE1</h1>"

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

    flash('Flash INFO', 'info')
    flash('Flash DANGER', 'danger')
    
    form = ProfileForm()

    data = User.get_all_users()
    if data is None:
        flash('No users found!', 'info')
        return redirect(url_for('users.index'))
    
    # # Pagination
    # per_page = 9
    # offset = (page - 1) * per_page
    # data = data[offset:offset + per_page]

    # # Modal Structure
    # modal_data= {
    #     'title': 'this is the title of the modal',
    #     'body': 'this is the body of the modal',
    #     'footer': 'this is the footer of the modal'        
    # }
    modal_data= {
        'title': 'Make Changes?',
        'body': 'this is the body of the modal',
        'footer': 'this is the footer of the modal',
        'btn_text': 'Logout',
        'btn_class': 'btn-danger',
        'btn_link': '{{ url_for(users.logout)}}'        
    }

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
    
    return render_template('main/widgets-collection.html', 
                           rawdata=data, 
                           page=page, 
                           modal_data=modal_data, 
                           carousel=carousel, 
                           form=form,
                           enumerate=enumerate) 
