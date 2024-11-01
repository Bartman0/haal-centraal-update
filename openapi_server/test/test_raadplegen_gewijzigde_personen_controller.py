import unittest

from flask import json

from openapi_server.models.bad_request_foutbericht import BadRequestFoutbericht  # noqa: E501
from openapi_server.models.foutbericht import Foutbericht  # noqa: E501
from openapi_server.models.gewijzigde_personen_hal_collectie import GewijzigdePersonenHalCollectie  # noqa: E501
from openapi_server.test import BaseTestCase


class TestRaadplegenGewijzigdePersonenController(BaseTestCase):
    """RaadplegenGewijzigdePersonenController integration test stubs"""

    def test_get_gewijzigde_personen(self):
        """Test case for get_gewijzigde_personen

        Raadpleeg personen met gewijzigde gegevens
        """
        query_string = [('vanaf', '2013-10-20')]
        headers = { 
            'Accept': 'application/problem+json',
        }
        response = self.client.open(
            '/haalcentraal/api/brpupdate/wijzigingen',
            method='GET',
            headers=headers,
            query_string=query_string)
        self.assert200(response,
                       'Response body is : ' + response.data.decode('utf-8'))


if __name__ == '__main__':
    unittest.main()
