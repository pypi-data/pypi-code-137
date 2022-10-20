# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetServiceTaskResult',
    'AwaitableGetServiceTaskResult',
    'get_service_task',
    'get_service_task_output',
]

@pulumi.output_type
class GetServiceTaskResult:
    """
    A task resource
    """
    def __init__(__self__, etag=None, id=None, name=None, properties=None, system_data=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        HTTP strong entity tag value. This is ignored if submitted.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Any:
        """
        Custom task properties
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetServiceTaskResult(GetServiceTaskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetServiceTaskResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_service_task(expand: Optional[str] = None,
                     group_name: Optional[str] = None,
                     service_name: Optional[str] = None,
                     task_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetServiceTaskResult:
    """
    A task resource


    :param str expand: Expand the response
    :param str group_name: Name of the resource group
    :param str service_name: Name of the service
    :param str task_name: Name of the Task
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['groupName'] = group_name
    __args__['serviceName'] = service_name
    __args__['taskName'] = task_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datamigration/v20220330preview:getServiceTask', __args__, opts=opts, typ=GetServiceTaskResult).value

    return AwaitableGetServiceTaskResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_service_task)
def get_service_task_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                            group_name: Optional[pulumi.Input[str]] = None,
                            service_name: Optional[pulumi.Input[str]] = None,
                            task_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetServiceTaskResult]:
    """
    A task resource


    :param str expand: Expand the response
    :param str group_name: Name of the resource group
    :param str service_name: Name of the service
    :param str task_name: Name of the Task
    """
    ...
