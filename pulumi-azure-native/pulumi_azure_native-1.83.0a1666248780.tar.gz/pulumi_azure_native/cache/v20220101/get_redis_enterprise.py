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
    'GetRedisEnterpriseResult',
    'AwaitableGetRedisEnterpriseResult',
    'get_redis_enterprise',
    'get_redis_enterprise_output',
]

@pulumi.output_type
class GetRedisEnterpriseResult:
    """
    Describes the RedisEnterprise cluster
    """
    def __init__(__self__, host_name=None, id=None, location=None, minimum_tls_version=None, name=None, private_endpoint_connections=None, provisioning_state=None, redis_version=None, resource_state=None, sku=None, tags=None, type=None, zones=None):
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if minimum_tls_version and not isinstance(minimum_tls_version, str):
            raise TypeError("Expected argument 'minimum_tls_version' to be a str")
        pulumi.set(__self__, "minimum_tls_version", minimum_tls_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_endpoint_connections and not isinstance(private_endpoint_connections, list):
            raise TypeError("Expected argument 'private_endpoint_connections' to be a list")
        pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if redis_version and not isinstance(redis_version, str):
            raise TypeError("Expected argument 'redis_version' to be a str")
        pulumi.set(__self__, "redis_version", redis_version)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        DNS name of the cluster endpoint
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="minimumTlsVersion")
    def minimum_tls_version(self) -> Optional[str]:
        """
        The minimum TLS version for the cluster to support, e.g. '1.2'
        """
        return pulumi.get(self, "minimum_tls_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Sequence['outputs.PrivateEndpointConnectionResponse']:
        """
        List of private endpoint connections associated with the specified RedisEnterprise cluster
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Current provisioning status of the cluster
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="redisVersion")
    def redis_version(self) -> str:
        """
        Version of redis the cluster supports, e.g. '6'
        """
        return pulumi.get(self, "redis_version")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        Current resource status of the cluster
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.EnterpriseSkuResponse':
        """
        The SKU to create, which affects price, performance, and features.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        The Availability Zones where this cluster will be deployed.
        """
        return pulumi.get(self, "zones")


class AwaitableGetRedisEnterpriseResult(GetRedisEnterpriseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRedisEnterpriseResult(
            host_name=self.host_name,
            id=self.id,
            location=self.location,
            minimum_tls_version=self.minimum_tls_version,
            name=self.name,
            private_endpoint_connections=self.private_endpoint_connections,
            provisioning_state=self.provisioning_state,
            redis_version=self.redis_version,
            resource_state=self.resource_state,
            sku=self.sku,
            tags=self.tags,
            type=self.type,
            zones=self.zones)


def get_redis_enterprise(cluster_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRedisEnterpriseResult:
    """
    Describes the RedisEnterprise cluster


    :param str cluster_name: The name of the RedisEnterprise cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cache/v20220101:getRedisEnterprise', __args__, opts=opts, typ=GetRedisEnterpriseResult).value

    return AwaitableGetRedisEnterpriseResult(
        host_name=__ret__.host_name,
        id=__ret__.id,
        location=__ret__.location,
        minimum_tls_version=__ret__.minimum_tls_version,
        name=__ret__.name,
        private_endpoint_connections=__ret__.private_endpoint_connections,
        provisioning_state=__ret__.provisioning_state,
        redis_version=__ret__.redis_version,
        resource_state=__ret__.resource_state,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type,
        zones=__ret__.zones)


@_utilities.lift_output_func(get_redis_enterprise)
def get_redis_enterprise_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRedisEnterpriseResult]:
    """
    Describes the RedisEnterprise cluster


    :param str cluster_name: The name of the RedisEnterprise cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
