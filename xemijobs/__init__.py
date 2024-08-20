from flask import Flask, render_template, redirect, url_for
from .extensions import mongo, login_manager, get_info_for



def create_app():
    app = Flask(__name__)
    # LOAD <Config.class> from <config.py> into app
    app.config.from_object('config.Config')
    
    # Initialize the EXTENSIONS
    # mongo.init_app(app, uri= str(os.getenv('MONGO_URI')))
    mongo.init_app(app)
    login_manager.init_app(app)

    # Add custom functions to Jinja2
    app.jinja_env.globals.update(get_info_for=get_info_for)
    
    # BLUEPRINTS
    from .main.views import main as main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    from .users.views import users as user_bp
    app.register_blueprint(user_bp, url_prefix='/user')

    from .companies.views import companies as company_bp
    app.register_blueprint(company_bp, url_prefix='/company')
    
    from .jobs.views import jobs as job_bp
    app.register_blueprint(job_bp, url_prefix='/job')
    
    from .applications.views import applications as appl_bp
    app.register_blueprint(appl_bp, url_prefix='/apply')

    @app.errorhandler(404)
    def e404(e):
        return redirect(url_for('main.error404'))
    
    @app.errorhandler(403)
    def e403(e):
        return redirect(url_for('main.error403'))

    
    return app
