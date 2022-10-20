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
    'GetManagedInstancePrivateEndpointConnectionResult',
    'AwaitableGetManagedInstancePrivateEndpointConnectionResult',
    'get_managed_instance_private_endpoint_connection',
    'get_managed_instance_private_endpoint_connection_output',
]

@pulumi.output_type
class GetManagedInstancePrivateEndpointConnectionResult:
    """
    A private endpoint connection
    """
    def __init__(__self__, id=None, name=None, private_endpoint=None, private_link_service_connection_state=None, provisioning_state=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint and not isinstance(private_endpoint, dict):
            raise TypeError("Expected argument 'private_endpoint' to be a dict")
        pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state and not isinstance(private_link_service_connection_state, dict):
            raise TypeError("Expected argument 'private_link_service_connection_state' to be a dict")
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.ManagedInstancePrivateEndpointPropertyResponse']:
        """
        Private endpoint which the connection belongs to.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional['outputs.ManagedInstancePrivateLinkServiceConnectionStatePropertyResponse']:
        """
        Connection State of the Private Endpoint Connection.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the Private Endpoint Connection.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedInstancePrivateEndpointConnectionResult(GetManagedInstancePrivateEndpointConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstancePrivateEndpointConnectionResult(
            id=self.id,
            name=self.name,
            private_endpoint=self.private_endpoint,
            private_link_service_connection_state=self.private_link_service_connection_state,
            provisioning_state=self.provisioning_state,
            type=self.type)


def get_managed_instance_private_endpoint_connection(managed_instance_name: Optional[str] = None,
                                                     private_endpoint_connection_name: Optional[str] = None,
                                                     resource_group_name: Optional[str] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstancePrivateEndpointConnectionResult:
    """
    A private endpoint connection


    :param str managed_instance_name: The name of the managed instance.
    :param str private_endpoint_connection_name: The name of the private endpoint connection.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['managedInstanceName'] = managed_instance_name
    __args__['privateEndpointConnectionName'] = private_endpoint_connection_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20200801preview:getManagedInstancePrivateEndpointConnection', __args__, opts=opts, typ=GetManagedInstancePrivateEndpointConnectionResult).value

    return AwaitableGetManagedInstancePrivateEndpointConnectionResult(
        id=__ret__.id,
        name=__ret__.name,
        private_endpoint=__ret__.private_endpoint,
        private_link_service_connection_state=__ret__.private_link_service_connection_state,
        provisioning_state=__ret__.provisioning_state,
        type=__ret__.type)


@_utilities.lift_output_func(get_managed_instance_private_endpoint_connection)
def get_managed_instance_private_endpoint_connection_output(managed_instance_name: Optional[pulumi.Input[str]] = None,
                                                            private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstancePrivateEndpointConnectionResult]:
    """
    A private endpoint connection


    :param str managed_instance_name: The name of the managed instance.
    :param str private_endpoint_connection_name: The name of the private endpoint connection.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
