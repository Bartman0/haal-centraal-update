from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server.models.hal_link import HalLink
from openapi_server import util

from openapi_server.models.hal_link import HalLink  # noqa: E501

class GewijzigdePersonenHalCollectionLinks(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, _self=None, ingeschreven_persoon=None):  # noqa: E501
        """GewijzigdePersonenHalCollectionLinks - a model defined in OpenAPI

        :param _self: The _self of this GewijzigdePersonenHalCollectionLinks.  # noqa: E501
        :type _self: HalLink
        :param ingeschreven_persoon: The ingeschreven_persoon of this GewijzigdePersonenHalCollectionLinks.  # noqa: E501
        :type ingeschreven_persoon: HalLink
        """
        self.openapi_types = {
            '_self': HalLink,
            'ingeschreven_persoon': HalLink
        }

        self.attribute_map = {
            '_self': 'self',
            'ingeschreven_persoon': 'ingeschrevenPersoon'
        }

        self.__self = _self
        self._ingeschreven_persoon = ingeschreven_persoon

    @classmethod
    def from_dict(cls, dikt) -> 'GewijzigdePersonenHalCollectionLinks':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The GewijzigdePersonenHalCollectionLinks of this GewijzigdePersonenHalCollectionLinks.  # noqa: E501
        :rtype: GewijzigdePersonenHalCollectionLinks
        """
        return util.deserialize_model(dikt, cls)

    @property
    def _self(self) -> HalLink:
        """Gets the _self of this GewijzigdePersonenHalCollectionLinks.


        :return: The _self of this GewijzigdePersonenHalCollectionLinks.
        :rtype: HalLink
        """
        return self.__self

    @_self.setter
    def _self(self, _self: HalLink):
        """Sets the _self of this GewijzigdePersonenHalCollectionLinks.


        :param _self: The _self of this GewijzigdePersonenHalCollectionLinks.
        :type _self: HalLink
        """

        self.__self = _self

    @property
    def ingeschreven_persoon(self) -> HalLink:
        """Gets the ingeschreven_persoon of this GewijzigdePersonenHalCollectionLinks.


        :return: The ingeschreven_persoon of this GewijzigdePersonenHalCollectionLinks.
        :rtype: HalLink
        """
        return self._ingeschreven_persoon

    @ingeschreven_persoon.setter
    def ingeschreven_persoon(self, ingeschreven_persoon: HalLink):
        """Sets the ingeschreven_persoon of this GewijzigdePersonenHalCollectionLinks.


        :param ingeschreven_persoon: The ingeschreven_persoon of this GewijzigdePersonenHalCollectionLinks.
        :type ingeschreven_persoon: HalLink
        """

        self._ingeschreven_persoon = ingeschreven_persoon