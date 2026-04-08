from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import config

db = SQLAlchemy()

def create_app(config_class=config['development']):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Initialize SQLAlchemy
    db.init_app(app)

    # Register blueprints here if needed
    # from app.routes import main
    # app.register_blueprint(main)

    return app
