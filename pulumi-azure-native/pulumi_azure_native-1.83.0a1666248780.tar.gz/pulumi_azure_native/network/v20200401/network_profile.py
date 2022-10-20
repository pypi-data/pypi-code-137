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
from ._enums import *
from ._inputs import *

__all__ = ['NetworkProfileArgs', 'NetworkProfile']

@pulumi.input_type
class NetworkProfileArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 container_network_interface_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceConfigurationArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkProfile resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceConfigurationArgs']]] container_network_interface_configurations: List of chid container network interface configurations.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] network_profile_name: The name of the network profile.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if container_network_interface_configurations is not None:
            pulumi.set(__self__, "container_network_interface_configurations", container_network_interface_configurations)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_profile_name is not None:
            pulumi.set(__self__, "network_profile_name", network_profile_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="containerNetworkInterfaceConfigurations")
    def container_network_interface_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceConfigurationArgs']]]]:
        """
        List of chid container network interface configurations.
        """
        return pulumi.get(self, "container_network_interface_configurations")

    @container_network_interface_configurations.setter
    def container_network_interface_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ContainerNetworkInterfaceConfigurationArgs']]]]):
        pulumi.set(self, "container_network_interface_configurations", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="networkProfileName")
    def network_profile_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network profile.
        """
        return pulumi.get(self, "network_profile_name")

    @network_profile_name.setter
    def network_profile_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_profile_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class NetworkProfile(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_network_interface_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerNetworkInterfaceConfigurationArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Network profile resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerNetworkInterfaceConfigurationArgs']]]] container_network_interface_configurations: List of chid container network interface configurations.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] network_profile_name: The name of the network profile.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkProfileArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Network profile resource.

        :param str resource_name: The name of the resource.
        :param NetworkProfileArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkProfileArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 container_network_interface_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ContainerNetworkInterfaceConfigurationArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkProfileArgs.__new__(NetworkProfileArgs)

            __props__.__dict__["container_network_interface_configurations"] = container_network_interface_configurations
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["network_profile_name"] = network_profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["container_network_interfaces"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20180801:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20181001:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20181101:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20181201:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20190201:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20190401:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20190601:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20190701:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20190801:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20190901:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20191101:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20191201:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20200301:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20200501:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20200601:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20200701:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20200801:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20201101:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20210201:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20210301:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20210501:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20210801:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20220101:NetworkProfile"), pulumi.Alias(type_="azure-native:network/v20220501:NetworkProfile")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkProfile, __self__).__init__(
            'azure-native:network/v20200401:NetworkProfile',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkProfile':
        """
        Get an existing NetworkProfile resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkProfileArgs.__new__(NetworkProfileArgs)

        __props__.__dict__["container_network_interface_configurations"] = None
        __props__.__dict__["container_network_interfaces"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return NetworkProfile(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="containerNetworkInterfaceConfigurations")
    def container_network_interface_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ContainerNetworkInterfaceConfigurationResponse']]]:
        """
        List of chid container network interface configurations.
        """
        return pulumi.get(self, "container_network_interface_configurations")

    @property
    @pulumi.getter(name="containerNetworkInterfaces")
    def container_network_interfaces(self) -> pulumi.Output[Sequence['outputs.ContainerNetworkInterfaceResponse']]:
        """
        List of child container network interfaces.
        """
        return pulumi.get(self, "container_network_interfaces")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the network profile resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        The resource GUID property of the network profile resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

