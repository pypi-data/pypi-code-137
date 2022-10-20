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
from ._inputs import *

__all__ = ['LocalNetworkGatewayInitArgs', 'LocalNetworkGateway']

@pulumi.input_type
class LocalNetworkGatewayInitArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 bgp_settings: Optional[pulumi.Input['BgpSettingsArgs']] = None,
                 gateway_ip_address: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 local_network_address_space: Optional[pulumi.Input['AddressSpaceArgs']] = None,
                 local_network_gateway_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a LocalNetworkGateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['BgpSettingsArgs'] bgp_settings: Local network gateway's BGP speaker settings.
        :param pulumi.Input[str] gateway_ip_address: IP address of local network gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input['AddressSpaceArgs'] local_network_address_space: Local network site address space.
        :param pulumi.Input[str] local_network_gateway_name: The name of the local network gateway.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if bgp_settings is not None:
            pulumi.set(__self__, "bgp_settings", bgp_settings)
        if gateway_ip_address is not None:
            pulumi.set(__self__, "gateway_ip_address", gateway_ip_address)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if local_network_address_space is not None:
            pulumi.set(__self__, "local_network_address_space", local_network_address_space)
        if local_network_gateway_name is not None:
            pulumi.set(__self__, "local_network_gateway_name", local_network_gateway_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
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
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> Optional[pulumi.Input['BgpSettingsArgs']]:
        """
        Local network gateway's BGP speaker settings.
        """
        return pulumi.get(self, "bgp_settings")

    @bgp_settings.setter
    def bgp_settings(self, value: Optional[pulumi.Input['BgpSettingsArgs']]):
        pulumi.set(self, "bgp_settings", value)

    @property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        IP address of local network gateway.
        """
        return pulumi.get(self, "gateway_ip_address")

    @gateway_ip_address.setter
    def gateway_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "gateway_ip_address", value)

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
    @pulumi.getter(name="localNetworkAddressSpace")
    def local_network_address_space(self) -> Optional[pulumi.Input['AddressSpaceArgs']]:
        """
        Local network site address space.
        """
        return pulumi.get(self, "local_network_address_space")

    @local_network_address_space.setter
    def local_network_address_space(self, value: Optional[pulumi.Input['AddressSpaceArgs']]):
        pulumi.set(self, "local_network_address_space", value)

    @property
    @pulumi.getter(name="localNetworkGatewayName")
    def local_network_gateway_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the local network gateway.
        """
        return pulumi.get(self, "local_network_gateway_name")

    @local_network_gateway_name.setter
    def local_network_gateway_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "local_network_gateway_name", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class LocalNetworkGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_settings: Optional[pulumi.Input[pulumi.InputType['BgpSettingsArgs']]] = None,
                 gateway_ip_address: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 local_network_address_space: Optional[pulumi.Input[pulumi.InputType['AddressSpaceArgs']]] = None,
                 local_network_gateway_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A common class for general resource information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['BgpSettingsArgs']] bgp_settings: Local network gateway's BGP speaker settings.
        :param pulumi.Input[str] gateway_ip_address: IP address of local network gateway.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[pulumi.InputType['AddressSpaceArgs']] local_network_address_space: Local network site address space.
        :param pulumi.Input[str] local_network_gateway_name: The name of the local network gateway.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LocalNetworkGatewayInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A common class for general resource information.

        :param str resource_name: The name of the resource.
        :param LocalNetworkGatewayInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LocalNetworkGatewayInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 bgp_settings: Optional[pulumi.Input[pulumi.InputType['BgpSettingsArgs']]] = None,
                 gateway_ip_address: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 local_network_address_space: Optional[pulumi.Input[pulumi.InputType['AddressSpaceArgs']]] = None,
                 local_network_gateway_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LocalNetworkGatewayInitArgs.__new__(LocalNetworkGatewayInitArgs)

            __props__.__dict__["bgp_settings"] = bgp_settings
            __props__.__dict__["gateway_ip_address"] = gateway_ip_address
            __props__.__dict__["id"] = id
            __props__.__dict__["local_network_address_space"] = local_network_address_space
            __props__.__dict__["local_network_gateway_name"] = local_network_gateway_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20150615:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20160330:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20160601:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20160901:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20161201:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20170301:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20170601:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20170801:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20170901:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20171001:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20171101:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20180101:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20180201:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20180401:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20180601:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20180701:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20180801:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20181001:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20181101:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20181201:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20190201:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20190401:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20190601:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20190701:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20190801:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20191101:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20191201:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20200301:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20200401:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20200501:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20200601:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20200701:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20200801:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20201101:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20210201:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20210301:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20210501:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20210801:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20220101:LocalNetworkGateway"), pulumi.Alias(type_="azure-native:network/v20220501:LocalNetworkGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LocalNetworkGateway, __self__).__init__(
            'azure-native:network/v20190901:LocalNetworkGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LocalNetworkGateway':
        """
        Get an existing LocalNetworkGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LocalNetworkGatewayInitArgs.__new__(LocalNetworkGatewayInitArgs)

        __props__.__dict__["bgp_settings"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["gateway_ip_address"] = None
        __props__.__dict__["local_network_address_space"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return LocalNetworkGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="bgpSettings")
    def bgp_settings(self) -> pulumi.Output[Optional['outputs.BgpSettingsResponse']]:
        """
        Local network gateway's BGP speaker settings.
        """
        return pulumi.get(self, "bgp_settings")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="gatewayIpAddress")
    def gateway_ip_address(self) -> pulumi.Output[Optional[str]]:
        """
        IP address of local network gateway.
        """
        return pulumi.get(self, "gateway_ip_address")

    @property
    @pulumi.getter(name="localNetworkAddressSpace")
    def local_network_address_space(self) -> pulumi.Output[Optional['outputs.AddressSpaceResponse']]:
        """
        Local network site address space.
        """
        return pulumi.get(self, "local_network_address_space")

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
        The provisioning state of the local network gateway resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        The resource GUID property of the local network gateway resource.
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

