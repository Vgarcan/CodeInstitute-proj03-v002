from flask import Flask, redirect, url_for
from .extensions import mongo, login_manager, get_info_for


def create_app():
    """
    This function creates and configures a Flask application instance.

    Parameters:
    None

    Returns:
    app (Flask): A configured Flask application instance.
    """
    app = Flask(__name__)
    # LOAD <Config.class> from <config.py> into app
    app.config.from_object("config.Config")

    # Initialize the EXTENSIONS
    mongo.init_app(app)
    login_manager.init_app(app)

    # Add custom functions to Jinja2
    app.jinja_env.globals.update(get_info_for=get_info_for)

    # BLUEPRINTS
    from .main.views import main as main_bp

    app.register_blueprint(main_bp, url_prefix="/")

    from .users.views import users as user_bp

    app.register_blueprint(user_bp, url_prefix="/user")

    from .companies.views import companies as company_bp

    app.register_blueprint(company_bp, url_prefix="/company")

    from .jobs.views import jobs as job_bp

    app.register_blueprint(job_bp, url_prefix="/job")

    from .applications.views import applications as appl_bp

    app.register_blueprint(appl_bp, url_prefix="/apply")

    @app.errorhandler(404)
    def e404(e):
        """
        Handles the 404 error by redirecting the user to the 'error404' function within the 'main' blueprint.

        Parameters:
        e (Exception): The exception object associated with the 404 error.

        Returns:
        redirect: A redirect response to the 'error404' function within the 'main' blueprint.
        """
        return redirect(url_for("main.error404"))

    @app.errorhandler(403)
    def e401(e):
        """
        Handles the 403 error by redirecting the user to the 'error403' function within the 'main' blueprint.

        Parameters:
        e (Exception): The exception object associated with the 403 error.

        Returns:
        redirect: A redirect response to the 'error403' function within the 'main' blueprint.
        """
        return redirect(url_for("main.error403"))

    @app.errorhandler(401)
    def e401(e):
        """
        Handles the 401 error by redirecting the user to the 'error401' function within the 'main' blueprint.

        Parameters:
        e (Exception): The exception object associated with the 401 error.

        Returns:
        redirect: A redirect response to the 'error401' function within the 'main' blueprint.
        """
        return redirect(url_for("main.error401"))

    return app
