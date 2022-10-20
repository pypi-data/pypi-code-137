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

class Overdue(object):
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
        'initial_reevaluation_interval': 'int',
        'overdue_states': 'list[OverdueStateConfig]'
    }

    attribute_map = {
        'initial_reevaluation_interval': 'initialReevaluationInterval',
        'overdue_states': 'overdueStates'
    }

    def __init__(self, initial_reevaluation_interval=None, overdue_states=None):  # noqa: E501
        """Overdue - a model defined in Swagger"""  # noqa: E501
        self._initial_reevaluation_interval = None
        self._overdue_states = None
        self.discriminator = None
        if initial_reevaluation_interval is not None:
            self.initial_reevaluation_interval = initial_reevaluation_interval
        if overdue_states is not None:
            self.overdue_states = overdue_states

    @property
    def initial_reevaluation_interval(self):
        """Gets the initial_reevaluation_interval of this Overdue.  # noqa: E501


        :return: The initial_reevaluation_interval of this Overdue.  # noqa: E501
        :rtype: int
        """
        return self._initial_reevaluation_interval

    @initial_reevaluation_interval.setter
    def initial_reevaluation_interval(self, initial_reevaluation_interval):
        """Sets the initial_reevaluation_interval of this Overdue.


        :param initial_reevaluation_interval: The initial_reevaluation_interval of this Overdue.  # noqa: E501
        :type: int
        """

        self._initial_reevaluation_interval = initial_reevaluation_interval

    @property
    def overdue_states(self):
        """Gets the overdue_states of this Overdue.  # noqa: E501


        :return: The overdue_states of this Overdue.  # noqa: E501
        :rtype: list[OverdueStateConfig]
        """
        return self._overdue_states

    @overdue_states.setter
    def overdue_states(self, overdue_states):
        """Sets the overdue_states of this Overdue.


        :param overdue_states: The overdue_states of this Overdue.  # noqa: E501
        :type: list[OverdueStateConfig]
        """

        self._overdue_states = overdue_states

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
        if issubclass(Overdue, dict):
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
        if not isinstance(other, Overdue):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
