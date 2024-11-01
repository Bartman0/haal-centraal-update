#!/usr/bin/env python3

import logging
from connexion import FlaskApp
from flask import Flask

from openapi_server import auth
from openapi_server.database.setup import init_database

# from openapi_server import encoder

database = None


def init_app():
    options = {"swagger_ui": True}
    app: FlaskApp = FlaskApp(__name__, specification_dir="./openapi/", options=options)
    # app.app.json_encoder = encoder.JSONEncoder
    app.add_api(
        "openapi.yaml", arguments={"title": "BRP Update API"}, pythonic_params=True
    )
    return app


def init_flask(app: FlaskApp, level=logging.INFO):
    flask_app: Flask = app.app
    flask_app.logger.setLevel(level)
    return flask_app


if __name__ == "__main__":
    token = auth.encode_token("afnemer_test", ["benk-brp-volgindicaties"])
    print(token)
    app = init_app()
    flask_app = init_flask(app, logging.DEBUG)
    database = init_database(flask_app)
    app.run(port=8083)
