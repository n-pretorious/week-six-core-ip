from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config_options


bootstrap = Bootstrap()
db = SQLAlchemy()
mail=Mail()


def create_app(config_name):
    app = Flask(__name__)

    # Initializing flask extensions
    app.config.from_object(config_options[config_name])
    bootstrap.init_app(app)
    db.init_app(app)
    mail.init_app(app)


    from .main import main as main_blueprint
    from .auth import auth as auth_blueprint
    
    # Registering blueprint
    app.register_blueprint(main_blueprint)
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app