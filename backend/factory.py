from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from spectree import SpecTree


db = SQLAlchemy()
migrate = Migrate()
api = SpecTree("flask", title="Mini Course API", version="v.1.0", path="docs")


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    db.init_app(app)

    from models import User

    migrate.init_app(app, db)

    from controllers.user_controller import user_controller

    app.register_blueprint(user_controller)

    api.register(app)

    @app.route("/")
    def hello_world():
        return "<h1>Hello, World!</h1>"

    return app
