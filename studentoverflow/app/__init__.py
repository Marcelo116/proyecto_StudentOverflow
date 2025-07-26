from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os


db = SQLAlchemy()
migrate = Migrate()

def create_app():
    load_dotenv()
    app = Flask(__name__)
    app.config.from_object("config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from . import models
    from . import routes
    from . import auth
    app.register_blueprint(routes.bp)
    app.register_blueprint(auth.auth)

    return app