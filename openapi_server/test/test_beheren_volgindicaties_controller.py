import unittest

from flask import json

from openapi_server.models.bad_request_foutbericht import BadRequestFoutbericht  # noqa: E501
from openapi_server.models.foutbericht import Foutbericht  # noqa: E501
from openapi_server.models.volgindicatie import Volgindicatie  # noqa: E501
from openapi_server.models.volgindicatie_collectie import VolgindicatieCollectie  # noqa: E501
from openapi_server.models.volgindicatie_raadplegen import VolgindicatieRaadplegen  # noqa: E501
from openapi_server.test import BaseTestCase


class TestBeherenVolgindicatiesController(BaseTestCase):
    """BeherenVolgindicatiesController integration test stubs"""

    def test_get_volgindicatie(self):
        """Test case for get_volgindicatie

        Raadpleeg een volgindicatie op een persoon
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/haalcentraal/api/brpupdate/volgindicaties/{burgerservicenummer}'.format(burgerservicenummer=555555021),
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_get_volgindicaties(self):
        """Test case for get_volgindicaties

        Raadpleeg actieve volgindicaties
        """
        headers = { 
            'Accept': 'application/json',
        }
        response = self.client.open(
            '/haalcentraal/api/brpupdate/volgindicaties',
            method='GET',
            headers=headers)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))

    def test_upsert_volgindicatie(self):
        """Test case for upsert_volgindicatie

        Plaats, wijzig of beëindig een volgindicatie
        """
        volgindicatie = {"einddatum":"2000-01-23"}
        headers = { 
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = self.client.open(
            '/haalcentraal/api/brpupdate/volgindicaties/{burgerservicenummer}'.format(burgerservicenummer=555555021),
            method='PUT',
            headers=headers,
            data=json.dumps(volgindicatie),
            content_type='application/json')
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
