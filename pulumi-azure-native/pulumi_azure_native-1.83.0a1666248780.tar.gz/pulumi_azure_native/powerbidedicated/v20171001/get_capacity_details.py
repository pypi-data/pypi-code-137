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
    'GetCapacityDetailsResult',
    'AwaitableGetCapacityDetailsResult',
    'get_capacity_details',
    'get_capacity_details_output',
]

warnings.warn("""Version 2017-10-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetCapacityDetailsResult:
    """
    Represents an instance of a Dedicated Capacity resource.
    """
    def __init__(__self__, administration=None, friendly_name=None, id=None, location=None, mode=None, name=None, provisioning_state=None, sku=None, state=None, tags=None, tenant_id=None, type=None):
        if administration and not isinstance(administration, dict):
            raise TypeError("Expected argument 'administration' to be a dict")
        pulumi.set(__self__, "administration", administration)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def administration(self) -> Optional['outputs.DedicatedCapacityAdministratorsResponse']:
        """
        A collection of Dedicated capacity administrators
        """
        return pulumi.get(self, "administration")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> str:
        """
        Capacity name
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        An identifier that represents the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Location of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def mode(self) -> str:
        """
        The capacity mode.
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment state of PowerBI Dedicated resource. The provisioningState is to indicate states for resource provisioning.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.ResourceSkuResponse':
        """
        The SKU of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of PowerBI Dedicated resource. The state is to indicate more states outside of resource provisioning.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Key-value pairs of additional resource provisioning properties.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        Tenant ID for the capacity. Used for creating Pro Plus capacity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the PowerBI Dedicated resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetCapacityDetailsResult(GetCapacityDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCapacityDetailsResult(
            administration=self.administration,
            friendly_name=self.friendly_name,
            id=self.id,
            location=self.location,
            mode=self.mode,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            state=self.state,
            tags=self.tags,
            tenant_id=self.tenant_id,
            type=self.type)


def get_capacity_details(dedicated_capacity_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCapacityDetailsResult:
    """
    Represents an instance of a Dedicated Capacity resource.


    :param str dedicated_capacity_name: The name of the dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63.
    :param str resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    """
    pulumi.log.warn("""get_capacity_details is deprecated: Version 2017-10-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['dedicatedCapacityName'] = dedicated_capacity_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:powerbidedicated/v20171001:getCapacityDetails', __args__, opts=opts, typ=GetCapacityDetailsResult).value

    return AwaitableGetCapacityDetailsResult(
        administration=__ret__.administration,
        friendly_name=__ret__.friendly_name,
        id=__ret__.id,
        location=__ret__.location,
        mode=__ret__.mode,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        state=__ret__.state,
        tags=__ret__.tags,
        tenant_id=__ret__.tenant_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_capacity_details)
def get_capacity_details_output(dedicated_capacity_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCapacityDetailsResult]:
    """
    Represents an instance of a Dedicated Capacity resource.


    :param str dedicated_capacity_name: The name of the dedicated capacity. It must be a minimum of 3 characters, and a maximum of 63.
    :param str resource_group_name: The name of the Azure Resource group of which a given PowerBIDedicated capacity is part. This name must be at least 1 character in length, and no more than 90.
    """
    pulumi.log.warn("""get_capacity_details is deprecated: Version 2017-10-01 will be removed in v2 of the provider.""")
    ...
