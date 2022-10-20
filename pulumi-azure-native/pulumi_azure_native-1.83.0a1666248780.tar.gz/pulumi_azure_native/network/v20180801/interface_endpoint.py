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

__all__ = ['InterfaceEndpointArgs', 'InterfaceEndpoint']

@pulumi.input_type
class InterfaceEndpointArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 endpoint_service: Optional[pulumi.Input['EndpointServiceArgs']] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 interface_endpoint_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input['SubnetArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a InterfaceEndpoint resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['EndpointServiceArgs'] endpoint_service: A reference to the service being brought into the virtual network.
        :param pulumi.Input[str] fqdn: A first-party service's FQDN that is mapped to the private IP allocated via this interface endpoint.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] interface_endpoint_name: The name of the interface endpoint.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input['SubnetArgs'] subnet: The ID of the subnet from which the private IP will be allocated.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if endpoint_service is not None:
            pulumi.set(__self__, "endpoint_service", endpoint_service)
        if fqdn is not None:
            pulumi.set(__self__, "fqdn", fqdn)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if interface_endpoint_name is not None:
            pulumi.set(__self__, "interface_endpoint_name", interface_endpoint_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)
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
    @pulumi.getter(name="endpointService")
    def endpoint_service(self) -> Optional[pulumi.Input['EndpointServiceArgs']]:
        """
        A reference to the service being brought into the virtual network.
        """
        return pulumi.get(self, "endpoint_service")

    @endpoint_service.setter
    def endpoint_service(self, value: Optional[pulumi.Input['EndpointServiceArgs']]):
        pulumi.set(self, "endpoint_service", value)

    @property
    @pulumi.getter
    def fqdn(self) -> Optional[pulumi.Input[str]]:
        """
        A first-party service's FQDN that is mapped to the private IP allocated via this interface endpoint.
        """
        return pulumi.get(self, "fqdn")

    @fqdn.setter
    def fqdn(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "fqdn", value)

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
    @pulumi.getter(name="interfaceEndpointName")
    def interface_endpoint_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the interface endpoint.
        """
        return pulumi.get(self, "interface_endpoint_name")

    @interface_endpoint_name.setter
    def interface_endpoint_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "interface_endpoint_name", value)

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
    def subnet(self) -> Optional[pulumi.Input['SubnetArgs']]:
        """
        The ID of the subnet from which the private IP will be allocated.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input['SubnetArgs']]):
        pulumi.set(self, "subnet", value)

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


class InterfaceEndpoint(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_service: Optional[pulumi.Input[pulumi.InputType['EndpointServiceArgs']]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 interface_endpoint_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['SubnetArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Interface endpoint resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['EndpointServiceArgs']] endpoint_service: A reference to the service being brought into the virtual network.
        :param pulumi.Input[str] fqdn: A first-party service's FQDN that is mapped to the private IP allocated via this interface endpoint.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] interface_endpoint_name: The name of the interface endpoint.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[pulumi.InputType['SubnetArgs']] subnet: The ID of the subnet from which the private IP will be allocated.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: InterfaceEndpointArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Interface endpoint resource.

        :param str resource_name: The name of the resource.
        :param InterfaceEndpointArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(InterfaceEndpointArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 endpoint_service: Optional[pulumi.Input[pulumi.InputType['EndpointServiceArgs']]] = None,
                 fqdn: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 interface_endpoint_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subnet: Optional[pulumi.Input[pulumi.InputType['SubnetArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = InterfaceEndpointArgs.__new__(InterfaceEndpointArgs)

            __props__.__dict__["endpoint_service"] = endpoint_service
            __props__.__dict__["fqdn"] = fqdn
            __props__.__dict__["id"] = id
            __props__.__dict__["interface_endpoint_name"] = interface_endpoint_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subnet"] = subnet
            __props__.__dict__["tags"] = tags
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["network_interfaces"] = None
            __props__.__dict__["owner"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20181001:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20181101:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20181201:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20190201:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20190401:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20190601:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20190701:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20190801:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20190901:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20191101:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20191201:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20200301:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20200401:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20200501:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20200601:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20200701:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20200801:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20201101:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20210201:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20210301:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20210501:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20210801:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20220101:InterfaceEndpoint"), pulumi.Alias(type_="azure-native:network/v20220501:InterfaceEndpoint")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(InterfaceEndpoint, __self__).__init__(
            'azure-native:network/v20180801:InterfaceEndpoint',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'InterfaceEndpoint':
        """
        Get an existing InterfaceEndpoint resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = InterfaceEndpointArgs.__new__(InterfaceEndpointArgs)

        __props__.__dict__["endpoint_service"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["fqdn"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_interfaces"] = None
        __props__.__dict__["owner"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["subnet"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return InterfaceEndpoint(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endpointService")
    def endpoint_service(self) -> pulumi.Output[Optional['outputs.EndpointServiceResponse']]:
        """
        A reference to the service being brought into the virtual network.
        """
        return pulumi.get(self, "endpoint_service")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets a unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def fqdn(self) -> pulumi.Output[Optional[str]]:
        """
        A first-party service's FQDN that is mapped to the private IP allocated via this interface endpoint.
        """
        return pulumi.get(self, "fqdn")

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
    @pulumi.getter(name="networkInterfaces")
    def network_interfaces(self) -> pulumi.Output[Sequence['outputs.NetworkInterfaceResponse']]:
        """
        Gets an array of references to the network interfaces created for this interface endpoint.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter
    def owner(self) -> pulumi.Output[str]:
        """
        A read-only property that identifies who created this interface endpoint.
        """
        return pulumi.get(self, "owner")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the interface endpoint. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def subnet(self) -> pulumi.Output[Optional['outputs.SubnetResponse']]:
        """
        The ID of the subnet from which the private IP will be allocated.
        """
        return pulumi.get(self, "subnet")

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

