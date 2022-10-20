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

class BundleTimeline(object):
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
        'account_id': 'str',
        'bundle_id': 'str',
        'external_key': 'str',
        'events': 'list[EventSubscription]',
        'audit_logs': 'list[AuditLog]'
    }

    attribute_map = {
        'account_id': 'accountId',
        'bundle_id': 'bundleId',
        'external_key': 'externalKey',
        'events': 'events',
        'audit_logs': 'auditLogs'
    }

    def __init__(self, account_id=None, bundle_id=None, external_key=None, events=None, audit_logs=None):  # noqa: E501
        """BundleTimeline - a model defined in Swagger"""  # noqa: E501
        self._account_id = None
        self._bundle_id = None
        self._external_key = None
        self._events = None
        self._audit_logs = None
        self.discriminator = None
        if account_id is not None:
            self.account_id = account_id
        if bundle_id is not None:
            self.bundle_id = bundle_id
        if external_key is not None:
            self.external_key = external_key
        if events is not None:
            self.events = events
        if audit_logs is not None:
            self.audit_logs = audit_logs

    @property
    def account_id(self):
        """Gets the account_id of this BundleTimeline.  # noqa: E501


        :return: The account_id of this BundleTimeline.  # noqa: E501
        :rtype: str
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this BundleTimeline.


        :param account_id: The account_id of this BundleTimeline.  # noqa: E501
        :type: str
        """

        self._account_id = account_id

    @property
    def bundle_id(self):
        """Gets the bundle_id of this BundleTimeline.  # noqa: E501


        :return: The bundle_id of this BundleTimeline.  # noqa: E501
        :rtype: str
        """
        return self._bundle_id

    @bundle_id.setter
    def bundle_id(self, bundle_id):
        """Sets the bundle_id of this BundleTimeline.


        :param bundle_id: The bundle_id of this BundleTimeline.  # noqa: E501
        :type: str
        """

        self._bundle_id = bundle_id

    @property
    def external_key(self):
        """Gets the external_key of this BundleTimeline.  # noqa: E501


        :return: The external_key of this BundleTimeline.  # noqa: E501
        :rtype: str
        """
        return self._external_key

    @external_key.setter
    def external_key(self, external_key):
        """Sets the external_key of this BundleTimeline.


        :param external_key: The external_key of this BundleTimeline.  # noqa: E501
        :type: str
        """

        self._external_key = external_key

    @property
    def events(self):
        """Gets the events of this BundleTimeline.  # noqa: E501


        :return: The events of this BundleTimeline.  # noqa: E501
        :rtype: list[EventSubscription]
        """
        return self._events

    @events.setter
    def events(self, events):
        """Sets the events of this BundleTimeline.


        :param events: The events of this BundleTimeline.  # noqa: E501
        :type: list[EventSubscription]
        """

        self._events = events

    @property
    def audit_logs(self):
        """Gets the audit_logs of this BundleTimeline.  # noqa: E501


        :return: The audit_logs of this BundleTimeline.  # noqa: E501
        :rtype: list[AuditLog]
        """
        return self._audit_logs

    @audit_logs.setter
    def audit_logs(self, audit_logs):
        """Sets the audit_logs of this BundleTimeline.


        :param audit_logs: The audit_logs of this BundleTimeline.  # noqa: E501
        :type: list[AuditLog]
        """

        self._audit_logs = audit_logs

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
        if issubclass(BundleTimeline, dict):
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
        if not isinstance(other, BundleTimeline):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
