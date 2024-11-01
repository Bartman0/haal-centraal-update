import logging

from connexion import FlaskApp
from flask_testing import TestCase

# from openapi_server.encoder import JSONEncoder


class BaseTestCase(TestCase):

    def create_app(self):
        logging.getLogger('connexion.operation').setLevel('ERROR')
        app = FlaskApp(__name__, specification_dir='../openapi/')
        # app.app.json_encoder = JSONEncoder
        app.add_api('openapi.yaml', pythonic_params=True)
        return app.app
