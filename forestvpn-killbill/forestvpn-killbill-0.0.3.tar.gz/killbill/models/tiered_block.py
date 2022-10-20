# coding: utf-8

"""
    Kill Bill

    Kill Bill is an open-source billing and payments platform  # noqa: E501

    OpenAPI spec version: 0.22.30
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class TieredBlock(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'unit': 'str',
        'size': 'str',
        'max': 'str',
        'prices': 'list[Price]'
    }

    attribute_map = {
        'unit': 'unit',
        'size': 'size',
        'max': 'max',
        'prices': 'prices'
    }

    def __init__(self, unit=None, size=None, max=None, prices=None):  # noqa: E501
        """TieredBlock - a model defined in Swagger"""  # noqa: E501
        self._unit = None
        self._size = None
        self._max = None
        self._prices = None
        self.discriminator = None
        if unit is not None:
            self.unit = unit
        if size is not None:
            self.size = size
        if max is not None:
            self.max = max
        if prices is not None:
            self.prices = prices

    @property
    def unit(self):
        """Gets the unit of this TieredBlock.  # noqa: E501


        :return: The unit of this TieredBlock.  # noqa: E501
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """Sets the unit of this TieredBlock.


        :param unit: The unit of this TieredBlock.  # noqa: E501
        :type: str
        """

        self._unit = unit

    @property
    def size(self):
        """Gets the size of this TieredBlock.  # noqa: E501


        :return: The size of this TieredBlock.  # noqa: E501
        :rtype: str
        """
        return self._size

    @size.setter
    def size(self, size):
        """Sets the size of this TieredBlock.


        :param size: The size of this TieredBlock.  # noqa: E501
        :type: str
        """

        self._size = size

    @property
    def max(self):
        """Gets the max of this TieredBlock.  # noqa: E501


        :return: The max of this TieredBlock.  # noqa: E501
        :rtype: str
        """
        return self._max

    @max.setter
    def max(self, max):
        """Sets the max of this TieredBlock.


        :param max: The max of this TieredBlock.  # noqa: E501
        :type: str
        """

        self._max = max

    @property
    def prices(self):
        """Gets the prices of this TieredBlock.  # noqa: E501


        :return: The prices of this TieredBlock.  # noqa: E501
        :rtype: list[Price]
        """
        return self._prices

    @prices.setter
    def prices(self, prices):
        """Sets the prices of this TieredBlock.


        :param prices: The prices of this TieredBlock.  # noqa: E501
        :type: list[Price]
        """

        self._prices = prices

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(TieredBlock, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, TieredBlock):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
