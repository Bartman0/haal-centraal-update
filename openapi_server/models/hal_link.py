from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from openapi_server.models.base_model import Model
from openapi_server import util


class HalLink(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, href=None, templated=None, title=None):  # noqa: E501
        """HalLink - a model defined in OpenAPI

        :param href: The href of this HalLink.  # noqa: E501
        :type href: str
        :param templated: The templated of this HalLink.  # noqa: E501
        :type templated: bool
        :param title: The title of this HalLink.  # noqa: E501
        :type title: str
        """
        self.openapi_types = {
            'href': str,
            'templated': bool,
            'title': str
        }

        self.attribute_map = {
            'href': 'href',
            'templated': 'templated',
            'title': 'title'
        }

        self._href = href
        self._templated = templated
        self._title = title

    @classmethod
    def from_dict(cls, dikt) -> 'HalLink':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The HalLink of this HalLink.  # noqa: E501
        :rtype: HalLink
        """
        return util.deserialize_model(dikt, cls)

    @property
    def href(self) -> str:
        """Gets the href of this HalLink.


        :return: The href of this HalLink.
        :rtype: str
        """
        return self._href

    @href.setter
    def href(self, href: str):
        """Sets the href of this HalLink.


        :param href: The href of this HalLink.
        :type href: str
        """
        if href is None:
            raise ValueError("Invalid value for `href`, must not be `None`")  # noqa: E501

        self._href = href

    @property
    def templated(self) -> bool:
        """Gets the templated of this HalLink.


        :return: The templated of this HalLink.
        :rtype: bool
        """
        return self._templated

    @templated.setter
    def templated(self, templated: bool):
        """Sets the templated of this HalLink.


        :param templated: The templated of this HalLink.
        :type templated: bool
        """

        self._templated = templated

    @property
    def title(self) -> str:
        """Gets the title of this HalLink.

        Voor mens leesbaar label bij de link  # noqa: E501

        :return: The title of this HalLink.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title: str):
        """Sets the title of this HalLink.

        Voor mens leesbaar label bij de link  # noqa: E501

        :param title: The title of this HalLink.
        :type title: str
        """

        self._title = title