from flask import Flask

from builder.api.main import MainApi
from builder.extensions import db, migrate, ma, api
from builder.config import DevelopmentConfig, ProductionConfig
from builder.routers.main import main


def create_app():
    app = Flask(__name__)
    app.config.from_object(ProductionConfig)

    register_extensions(app)

    return app


def register_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)

    initialize_blueprints(app)
    initialize_routes(api)

    api.init_app(app)
    return None


def initialize_routes(api):
    api.add_resource(MainApi, '/api/v1.0/builder/')
    return None


def initialize_blueprints(app):
    app.register_blueprint(main)


app = create_app()
