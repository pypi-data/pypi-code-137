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
    'GetAvailabilitySetResult',
    'AwaitableGetAvailabilitySetResult',
    'get_availability_set',
    'get_availability_set_output',
]

@pulumi.output_type
class GetAvailabilitySetResult:
    """
    The AvailabilitySets resource definition.
    """
    def __init__(__self__, availability_set_name=None, extended_location=None, id=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None, vmm_server_id=None):
        if availability_set_name and not isinstance(availability_set_name, str):
            raise TypeError("Expected argument 'availability_set_name' to be a str")
        pulumi.set(__self__, "availability_set_name", availability_set_name)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vmm_server_id and not isinstance(vmm_server_id, str):
            raise TypeError("Expected argument 'vmm_server_id' to be a str")
        pulumi.set(__self__, "vmm_server_id", vmm_server_id)

    @property
    @pulumi.getter(name="availabilitySetName")
    def availability_set_name(self) -> Optional[str]:
        """
        Name of the availability set.
        """
        return pulumi.get(self, "availability_set_name")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extended location.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Gets or sets the location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets or sets the provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmmServerId")
    def vmm_server_id(self) -> Optional[str]:
        """
        ARM Id of the vmmServer resource in which this resource resides.
        """
        return pulumi.get(self, "vmm_server_id")


class AwaitableGetAvailabilitySetResult(GetAvailabilitySetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAvailabilitySetResult(
            availability_set_name=self.availability_set_name,
            extended_location=self.extended_location,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            vmm_server_id=self.vmm_server_id)


def get_availability_set(availability_set_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAvailabilitySetResult:
    """
    The AvailabilitySets resource definition.
    API Version: 2020-06-05-preview.


    :param str availability_set_name: Name of the AvailabilitySet.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['availabilitySetName'] = availability_set_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:scvmm:getAvailabilitySet', __args__, opts=opts, typ=GetAvailabilitySetResult).value

    return AwaitableGetAvailabilitySetResult(
        availability_set_name=__ret__.availability_set_name,
        extended_location=__ret__.extended_location,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        vmm_server_id=__ret__.vmm_server_id)


@_utilities.lift_output_func(get_availability_set)
def get_availability_set_output(availability_set_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAvailabilitySetResult]:
    """
    The AvailabilitySets resource definition.
    API Version: 2020-06-05-preview.


    :param str availability_set_name: Name of the AvailabilitySet.
    :param str resource_group_name: The name of the resource group.
    """
    ...
