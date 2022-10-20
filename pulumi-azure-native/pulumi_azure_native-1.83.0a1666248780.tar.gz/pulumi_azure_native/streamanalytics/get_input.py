# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetInputResult',
    'AwaitableGetInputResult',
    'get_input',
    'get_input_output',
]

@pulumi.output_type
class GetInputResult:
    """
    An input object, containing all information associated with the named input. All inputs are contained under a streaming job.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> Any:
        """
        The properties that are associated with an input. Required on PUT (CreateOrReplace) requests.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetInputResult(GetInputResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetInputResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_input(input_name: Optional[str] = None,
              job_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetInputResult:
    """
    An input object, containing all information associated with the named input. All inputs are contained under a streaming job.
    API Version: 2016-03-01.


    :param str input_name: The name of the input.
    :param str job_name: The name of the streaming job.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['inputName'] = input_name
    __args__['jobName'] = job_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:streamanalytics:getInput', __args__, opts=opts, typ=GetInputResult).value

    return AwaitableGetInputResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)


@_utilities.lift_output_func(get_input)
def get_input_output(input_name: Optional[pulumi.Input[str]] = None,
                     job_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetInputResult]:
    """
    An input object, containing all information associated with the named input. All inputs are contained under a streaming job.
    API Version: 2016-03-01.


    :param str input_name: The name of the input.
    :param str job_name: The name of the streaming job.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
