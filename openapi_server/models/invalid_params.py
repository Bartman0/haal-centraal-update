from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class InvalidParams(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, type=None, name=None, code=None, reason=None):  # noqa: E501
        """InvalidParams - a model defined in OpenAPI

        :param type: The type of this InvalidParams.  # noqa: E501
        :type type: str
        :param name: The name of this InvalidParams.  # noqa: E501
        :type name: str
        :param code: The code of this InvalidParams.  # noqa: E501
        :type code: str
        :param reason: The reason of this InvalidParams.  # noqa: E501
        :type reason: str
        """
        self.openapi_types = {
            'type': str,
            'name': str,
            'code': str,
            'reason': str
        }

        self.attribute_map = {
            'type': 'type',
            'name': 'name',
            'code': 'code',
            'reason': 'reason'
        }

        self._type = type
        self._name = name
        self._code = code
        self._reason = reason

    @classmethod
    def from_dict(cls, dikt) -> 'InvalidParams':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The InvalidParams of this InvalidParams.  # noqa: E501
        :rtype: InvalidParams
        """
        return util.deserialize_model(dikt, cls)

    @property
    def type(self) -> str:
        """Gets the type of this InvalidParams.


        :return: The type of this InvalidParams.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type: str):
        """Sets the type of this InvalidParams.


        :param type: The type of this InvalidParams.
        :type type: str
        """

        self._type = type

    @property
    def name(self) -> str:
        """Gets the name of this InvalidParams.

        Naam van de parameter  # noqa: E501

        :return: The name of this InvalidParams.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name: str):
        """Sets the name of this InvalidParams.

        Naam van de parameter  # noqa: E501

        :param name: The name of this InvalidParams.
        :type name: str
        """

        self._name = name

    @property
    def code(self) -> str:
        """Gets the code of this InvalidParams.

        Systeemcode die het type fout aangeeft  # noqa: E501

        :return: The code of this InvalidParams.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code: str):
        """Sets the code of this InvalidParams.

        Systeemcode die het type fout aangeeft  # noqa: E501

        :param code: The code of this InvalidParams.
        :type code: str
        """
        if code is not None and len(code) < 1:
            raise ValueError("Invalid value for `code`, length must be greater than or equal to `1`")  # noqa: E501

        self._code = code

    @property
    def reason(self) -> str:
        """Gets the reason of this InvalidParams.

        Beschrijving van de fout op de parameterwaarde  # noqa: E501

        :return: The reason of this InvalidParams.
        :rtype: str
        """
        return self._reason

    @reason.setter
    def reason(self, reason: str):
        """Sets the reason of this InvalidParams.

        Beschrijving van de fout op de parameterwaarde  # noqa: E501

        :param reason: The reason of this InvalidParams.
        :type reason: str
        """

        self._reason = reason