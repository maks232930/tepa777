from flask import Flask

from .extensions import db, migrate
from .config import DevelopmentConfig, ProductionConfig
from builder.routers.main import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    db.init_app(app)
    migrate.init_app(app, db)

    app.register_blueprint(main)

    return app
