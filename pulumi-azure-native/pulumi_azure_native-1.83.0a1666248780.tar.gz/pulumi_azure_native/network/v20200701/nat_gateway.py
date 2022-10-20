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

__all__ = ['NatGatewayInitArgs', 'NatGateway']

@pulumi.input_type
class NatGatewayInitArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 nat_gateway_name: Optional[pulumi.Input[str]] = None,
                 public_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]] = None,
                 public_ip_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]] = None,
                 sku: Optional[pulumi.Input['NatGatewaySkuArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NatGateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[int] idle_timeout_in_minutes: The idle timeout of the nat gateway.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] nat_gateway_name: The name of the nat gateway.
        :param pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]] public_ip_addresses: An array of public ip addresses associated with the nat gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]] public_ip_prefixes: An array of public ip prefixes associated with the nat gateway resource.
        :param pulumi.Input['NatGatewaySkuArgs'] sku: The nat gateway SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting the zone in which Nat Gateway should be deployed.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if idle_timeout_in_minutes is not None:
            pulumi.set(__self__, "idle_timeout_in_minutes", idle_timeout_in_minutes)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if nat_gateway_name is not None:
            pulumi.set(__self__, "nat_gateway_name", nat_gateway_name)
        if public_ip_addresses is not None:
            pulumi.set(__self__, "public_ip_addresses", public_ip_addresses)
        if public_ip_prefixes is not None:
            pulumi.set(__self__, "public_ip_prefixes", public_ip_prefixes)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if zones is not None:
            pulumi.set(__self__, "zones", zones)

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
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        The idle timeout of the nat gateway.
        """
        return pulumi.get(self, "idle_timeout_in_minutes")

    @idle_timeout_in_minutes.setter
    def idle_timeout_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "idle_timeout_in_minutes", value)

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
    @pulumi.getter(name="natGatewayName")
    def nat_gateway_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the nat gateway.
        """
        return pulumi.get(self, "nat_gateway_name")

    @nat_gateway_name.setter
    def nat_gateway_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "nat_gateway_name", value)

    @property
    @pulumi.getter(name="publicIpAddresses")
    def public_ip_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]:
        """
        An array of public ip addresses associated with the nat gateway resource.
        """
        return pulumi.get(self, "public_ip_addresses")

    @public_ip_addresses.setter
    def public_ip_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]):
        pulumi.set(self, "public_ip_addresses", value)

    @property
    @pulumi.getter(name="publicIpPrefixes")
    def public_ip_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]:
        """
        An array of public ip prefixes associated with the nat gateway resource.
        """
        return pulumi.get(self, "public_ip_prefixes")

    @public_ip_prefixes.setter
    def public_ip_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SubResourceArgs']]]]):
        pulumi.set(self, "public_ip_prefixes", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['NatGatewaySkuArgs']]:
        """
        The nat gateway SKU.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['NatGatewaySkuArgs']]):
        pulumi.set(self, "sku", value)

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

    @property
    @pulumi.getter
    def zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        A list of availability zones denoting the zone in which Nat Gateway should be deployed.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "zones", value)


class NatGateway(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 nat_gateway_name: Optional[pulumi.Input[str]] = None,
                 public_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 public_ip_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['NatGatewaySkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Nat Gateway resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[int] idle_timeout_in_minutes: The idle timeout of the nat gateway.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] nat_gateway_name: The name of the nat gateway.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]] public_ip_addresses: An array of public ip addresses associated with the nat gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]] public_ip_prefixes: An array of public ip prefixes associated with the nat gateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['NatGatewaySkuArgs']] sku: The nat gateway SKU.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: A list of availability zones denoting the zone in which Nat Gateway should be deployed.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NatGatewayInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Nat Gateway resource.

        :param str resource_name: The name of the resource.
        :param NatGatewayInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NatGatewayInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 idle_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 nat_gateway_name: Optional[pulumi.Input[str]] = None,
                 public_ip_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 public_ip_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SubResourceArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['NatGatewaySkuArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NatGatewayInitArgs.__new__(NatGatewayInitArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["idle_timeout_in_minutes"] = idle_timeout_in_minutes
            __props__.__dict__["location"] = location
            __props__.__dict__["nat_gateway_name"] = nat_gateway_name
            __props__.__dict__["public_ip_addresses"] = public_ip_addresses
            __props__.__dict__["public_ip_prefixes"] = public_ip_prefixes
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["sku"] = sku
            __props__.__dict__["tags"] = tags
            __props__.__dict__["zones"] = zones
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["subnets"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:NatGateway"), pulumi.Alias(type_="azure-native:network/v20190201:NatGateway"), pulumi.Alias(type_="azure-native:network/v20190401:NatGateway"), pulumi.Alias(type_="azure-native:network/v20190601:NatGateway"), pulumi.Alias(type_="azure-native:network/v20190701:NatGateway"), pulumi.Alias(type_="azure-native:network/v20190801:NatGateway"), pulumi.Alias(type_="azure-native:network/v20190901:NatGateway"), pulumi.Alias(type_="azure-native:network/v20191101:NatGateway"), pulumi.Alias(type_="azure-native:network/v20191201:NatGateway"), pulumi.Alias(type_="azure-native:network/v20200301:NatGateway"), pulumi.Alias(type_="azure-native:network/v20200401:NatGateway"), pulumi.Alias(type_="azure-native:network/v20200501:NatGateway"), pulumi.Alias(type_="azure-native:network/v20200601:NatGateway"), pulumi.Alias(type_="azure-native:network/v20200801:NatGateway"), pulumi.Alias(type_="azure-native:network/v20201101:NatGateway"), pulumi.Alias(type_="azure-native:network/v20210201:NatGateway"), pulumi.Alias(type_="azure-native:network/v20210301:NatGateway"), pulumi.Alias(type_="azure-native:network/v20210501:NatGateway"), pulumi.Alias(type_="azure-native:network/v20210801:NatGateway"), pulumi.Alias(type_="azure-native:network/v20220101:NatGateway"), pulumi.Alias(type_="azure-native:network/v20220501:NatGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NatGateway, __self__).__init__(
            'azure-native:network/v20200701:NatGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NatGateway':
        """
        Get an existing NatGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NatGatewayInitArgs.__new__(NatGatewayInitArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["idle_timeout_in_minutes"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_ip_addresses"] = None
        __props__.__dict__["public_ip_prefixes"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zones"] = None
        return NatGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="idleTimeoutInMinutes")
    def idle_timeout_in_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        The idle timeout of the nat gateway.
        """
        return pulumi.get(self, "idle_timeout_in_minutes")

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
        The provisioning state of the NAT gateway resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIpAddresses")
    def public_ip_addresses(self) -> pulumi.Output[Optional[Sequence['outputs.SubResourceResponse']]]:
        """
        An array of public ip addresses associated with the nat gateway resource.
        """
        return pulumi.get(self, "public_ip_addresses")

    @property
    @pulumi.getter(name="publicIpPrefixes")
    def public_ip_prefixes(self) -> pulumi.Output[Optional[Sequence['outputs.SubResourceResponse']]]:
        """
        An array of public ip prefixes associated with the nat gateway resource.
        """
        return pulumi.get(self, "public_ip_prefixes")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        The resource GUID property of the NAT gateway resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.NatGatewaySkuResponse']]:
        """
        The nat gateway SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        An array of references to the subnets using this nat gateway resource.
        """
        return pulumi.get(self, "subnets")

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

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        A list of availability zones denoting the zone in which Nat Gateway should be deployed.
        """
        return pulumi.get(self, "zones")

