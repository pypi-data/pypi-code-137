# coding: utf-8

"""
    Merlin

    API Guide for accessing Merlin's model management, deployment, and serving functionalities  # noqa: E501

    OpenAPI spec version: 0.14.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class Model(object):
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
        'id': 'int',
        'project_id': 'int',
        'mlflow_experiment_id': 'int',
        'name': 'str',
        'type': 'str',
        'mlflow_url': 'str',
        'endpoints': 'list[ModelEndpoint]',
        'created_at': 'datetime',
        'updated_at': 'datetime'
    }

    attribute_map = {
        'id': 'id',
        'project_id': 'project_id',
        'mlflow_experiment_id': 'mlflow_experiment_id',
        'name': 'name',
        'type': 'type',
        'mlflow_url': 'mlflow_url',
        'endpoints': 'endpoints',
        'created_at': 'created_at',
        'updated_at': 'updated_at'
    }

    def __init__(self, id=None, project_id=None, mlflow_experiment_id=None, name=None, type=None, mlflow_url=None, endpoints=None, created_at=None, updated_at=None):  # noqa: E501
        """Model - a model defined in Swagger"""  # noqa: E501
        self._id = None
        self._project_id = None
        self._mlflow_experiment_id = None
        self._name = None
        self._type = None
        self._mlflow_url = None
        self._endpoints = None
        self._created_at = None
        self._updated_at = None
        self.discriminator = None
        if id is not None:
            self.id = id
        if project_id is not None:
            self.project_id = project_id
        if mlflow_experiment_id is not None:
            self.mlflow_experiment_id = mlflow_experiment_id
        if name is not None:
            self.name = name
        if type is not None:
            self.type = type
        if mlflow_url is not None:
            self.mlflow_url = mlflow_url
        if endpoints is not None:
            self.endpoints = endpoints
        if created_at is not None:
            self.created_at = created_at
        if updated_at is not None:
            self.updated_at = updated_at

    @property
    def id(self):
        """Gets the id of this Model.  # noqa: E501


        :return: The id of this Model.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Model.


        :param id: The id of this Model.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def project_id(self):
        """Gets the project_id of this Model.  # noqa: E501


        :return: The project_id of this Model.  # noqa: E501
        :rtype: int
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this Model.


        :param project_id: The project_id of this Model.  # noqa: E501
        :type: int
        """

        self._project_id = project_id

    @property
    def mlflow_experiment_id(self):
        """Gets the mlflow_experiment_id of this Model.  # noqa: E501


        :return: The mlflow_experiment_id of this Model.  # noqa: E501
        :rtype: int
        """
        return self._mlflow_experiment_id

    @mlflow_experiment_id.setter
    def mlflow_experiment_id(self, mlflow_experiment_id):
        """Sets the mlflow_experiment_id of this Model.


        :param mlflow_experiment_id: The mlflow_experiment_id of this Model.  # noqa: E501
        :type: int
        """

        self._mlflow_experiment_id = mlflow_experiment_id

    @property
    def name(self):
        """Gets the name of this Model.  # noqa: E501


        :return: The name of this Model.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Model.


        :param name: The name of this Model.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def type(self):
        """Gets the type of this Model.  # noqa: E501

        Model type  # noqa: E501

        :return: The type of this Model.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Model.

        Model type  # noqa: E501

        :param type: The type of this Model.  # noqa: E501
        :type: str
        """
        allowed_values = ["xgboost", "tensorflow", "sklearn", "pytorch", "pyfunc", "pyfunc_v2", "custom"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

    @property
    def mlflow_url(self):
        """Gets the mlflow_url of this Model.  # noqa: E501


        :return: The mlflow_url of this Model.  # noqa: E501
        :rtype: str
        """
        return self._mlflow_url

    @mlflow_url.setter
    def mlflow_url(self, mlflow_url):
        """Sets the mlflow_url of this Model.


        :param mlflow_url: The mlflow_url of this Model.  # noqa: E501
        :type: str
        """

        self._mlflow_url = mlflow_url

    @property
    def endpoints(self):
        """Gets the endpoints of this Model.  # noqa: E501


        :return: The endpoints of this Model.  # noqa: E501
        :rtype: list[ModelEndpoint]
        """
        return self._endpoints

    @endpoints.setter
    def endpoints(self, endpoints):
        """Sets the endpoints of this Model.


        :param endpoints: The endpoints of this Model.  # noqa: E501
        :type: list[ModelEndpoint]
        """

        self._endpoints = endpoints

    @property
    def created_at(self):
        """Gets the created_at of this Model.  # noqa: E501


        :return: The created_at of this Model.  # noqa: E501
        :rtype: datetime
        """
        return self._created_at

    @created_at.setter
    def created_at(self, created_at):
        """Sets the created_at of this Model.


        :param created_at: The created_at of this Model.  # noqa: E501
        :type: datetime
        """

        self._created_at = created_at

    @property
    def updated_at(self):
        """Gets the updated_at of this Model.  # noqa: E501


        :return: The updated_at of this Model.  # noqa: E501
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this Model.


        :param updated_at: The updated_at of this Model.  # noqa: E501
        :type: datetime
        """

        self._updated_at = updated_at

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
        if issubclass(Model, dict):
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
        if not isinstance(other, Model):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
