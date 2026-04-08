from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import config  # assuming you have a config.py with DevelopmentConfig

db = SQLAlchemy()

def create_app(config_class=config.DevelopmentConfig):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize extensions
    db.init_app(app)

    # Register blueprints or other app components here
    # from app.routes import main
    # app.register_blueprint(main)

    return app