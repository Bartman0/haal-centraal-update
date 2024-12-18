from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.volgindicatie_raadplegen import VolgindicatieRaadplegen
from openapi_server import util

from openapi_server.models.volgindicatie_raadplegen import VolgindicatieRaadplegen  # noqa: E501

class VolgindicatieCollectie(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, volgindicaties=None):  # noqa: E501
        """VolgindicatieCollectie - a model defined in OpenAPI

        :param volgindicaties: The volgindicaties of this VolgindicatieCollectie.  # noqa: E501
        :type volgindicaties: List[VolgindicatieRaadplegen]
        """
        self.openapi_types = {
            'volgindicaties': List[VolgindicatieRaadplegen]
        }

        self.attribute_map = {
            'volgindicaties': 'volgindicaties'
        }

        self._volgindicaties = volgindicaties

    @classmethod
    def from_dict(cls, dikt) -> 'VolgindicatieCollectie':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The VolgindicatieCollectie of this VolgindicatieCollectie.  # noqa: E501
        :rtype: VolgindicatieCollectie
        """
        return util.deserialize_model(dikt, cls)

    @property
    def volgindicaties(self) -> List[VolgindicatieRaadplegen]:
        """Gets the volgindicaties of this VolgindicatieCollectie.


        :return: The volgindicaties of this VolgindicatieCollectie.
        :rtype: List[VolgindicatieRaadplegen]
        """
        return self._volgindicaties

    @volgindicaties.setter
    def volgindicaties(self, volgindicaties: List[VolgindicatieRaadplegen]):
        """Sets the volgindicaties of this VolgindicatieCollectie.


        :param volgindicaties: The volgindicaties of this VolgindicatieCollectie.
        :type volgindicaties: List[VolgindicatieRaadplegen]
        """

        self._volgindicaties = volgindicaties
