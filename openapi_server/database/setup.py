import os
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import URL
from sqlalchemy.orm import DeclarativeBase

from openapi_server.config import CONFIG
from openapi_server.database import models


def init_database(flask_app):
    uri = CONFIG.SQLALCHEMY_DATABASE_URI
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = uri
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    database = SQLAlchemy(flask_app)
    with flask_app.app_context():
        database.reflect()
    models.setup(database)
    return database
