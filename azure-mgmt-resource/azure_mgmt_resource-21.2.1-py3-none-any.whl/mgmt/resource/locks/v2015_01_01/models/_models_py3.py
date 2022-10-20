# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import List, Optional, TYPE_CHECKING, Union

from ... import _serialization

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models


class ManagementLockListResult(_serialization.Model):
    """List of management locks.

    :ivar value: The list of locks.
    :vartype value: list[~azure.mgmt.resource.locks.v2015_01_01.models.ManagementLockObject]
    :ivar next_link: The URL to get the next set of results.
    :vartype next_link: str
    """

    _attribute_map = {
        "value": {"key": "value", "type": "[ManagementLockObject]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: Optional[List["_models.ManagementLockObject"]] = None, next_link: Optional[str] = None, **kwargs
    ):
        """
        :keyword value: The list of locks.
        :paramtype value: list[~azure.mgmt.resource.locks.v2015_01_01.models.ManagementLockObject]
        :keyword next_link: The URL to get the next set of results.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class ManagementLockObject(_serialization.Model):
    """Management lock information.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: The Id of the lock.
    :vartype id: str
    :ivar type: The type of the lock.
    :vartype type: str
    :ivar name: The name of the lock.
    :vartype name: str
    :ivar level: The lock level of the management lock. Known values are: "NotSpecified",
     "CanNotDelete", and "ReadOnly".
    :vartype level: str or ~azure.mgmt.resource.locks.v2015_01_01.models.LockLevel
    :ivar notes: The notes of the management lock.
    :vartype notes: str
    """

    _validation = {
        "id": {"readonly": True},
        "type": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "level": {"key": "properties.level", "type": "str"},
        "notes": {"key": "properties.notes", "type": "str"},
    }

    def __init__(
        self,
        *,
        name: Optional[str] = None,
        level: Optional[Union[str, "_models.LockLevel"]] = None,
        notes: Optional[str] = None,
        **kwargs
    ):
        """
        :keyword name: The name of the lock.
        :paramtype name: str
        :keyword level: The lock level of the management lock. Known values are: "NotSpecified",
         "CanNotDelete", and "ReadOnly".
        :paramtype level: str or ~azure.mgmt.resource.locks.v2015_01_01.models.LockLevel
        :keyword notes: The notes of the management lock.
        :paramtype notes: str
        """
        super().__init__(**kwargs)
        self.id = None
        self.type = None
        self.name = name
        self.level = level
        self.notes = notes
