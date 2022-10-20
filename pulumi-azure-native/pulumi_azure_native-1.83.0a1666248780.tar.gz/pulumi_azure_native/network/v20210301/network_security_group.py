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

__all__ = ['NetworkSecurityGroupInitArgs', 'NetworkSecurityGroup']

@pulumi.input_type
class NetworkSecurityGroupInitArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_security_group_name: Optional[pulumi.Input[str]] = None,
                 security_rules: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a NetworkSecurityGroup resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] network_security_group_name: The name of the network security group.
        :param pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]] security_rules: A collection of security rules of the network security group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if network_security_group_name is not None:
            pulumi.set(__self__, "network_security_group_name", network_security_group_name)
        if security_rules is not None:
            pulumi.set(__self__, "security_rules", security_rules)
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
    @pulumi.getter(name="networkSecurityGroupName")
    def network_security_group_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the network security group.
        """
        return pulumi.get(self, "network_security_group_name")

    @network_security_group_name.setter
    def network_security_group_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_security_group_name", value)

    @property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]]:
        """
        A collection of security rules of the network security group.
        """
        return pulumi.get(self, "security_rules")

    @security_rules.setter
    def security_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SecurityRuleArgs']]]]):
        pulumi.set(self, "security_rules", value)

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


class NetworkSecurityGroup(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_security_group_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        NetworkSecurityGroup resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] network_security_group_name: The name of the network security group.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]] security_rules: A collection of security rules of the network security group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NetworkSecurityGroupInitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NetworkSecurityGroup resource.

        :param str resource_name: The name of the resource.
        :param NetworkSecurityGroupInitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NetworkSecurityGroupInitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 network_security_group_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 security_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['SecurityRuleArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NetworkSecurityGroupInitArgs.__new__(NetworkSecurityGroupInitArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["network_security_group_name"] = network_security_group_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["security_rules"] = security_rules
            __props__.__dict__["tags"] = tags
            __props__.__dict__["default_security_rules"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["flow_logs"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["network_interfaces"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_guid"] = None
            __props__.__dict__["subnets"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20150501preview:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20150615:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20160330:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20160601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20160901:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20161201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20170301:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20170601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20170801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20170901:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20171001:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20171101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180401:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180701:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20180801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20181001:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20181101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20181201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190401:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190701:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20190901:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20191101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20191201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200301:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200401:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200501:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200601:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200701:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20200801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20201101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20210201:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20210501:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20210801:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20220101:NetworkSecurityGroup"), pulumi.Alias(type_="azure-native:network/v20220501:NetworkSecurityGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NetworkSecurityGroup, __self__).__init__(
            'azure-native:network/v20210301:NetworkSecurityGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NetworkSecurityGroup':
        """
        Get an existing NetworkSecurityGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NetworkSecurityGroupInitArgs.__new__(NetworkSecurityGroupInitArgs)

        __props__.__dict__["default_security_rules"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["flow_logs"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["network_interfaces"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["security_rules"] = None
        __props__.__dict__["subnets"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return NetworkSecurityGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultSecurityRules")
    def default_security_rules(self) -> pulumi.Output[Sequence['outputs.SecurityRuleResponse']]:
        """
        The default security rules of network security group.
        """
        return pulumi.get(self, "default_security_rules")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="flowLogs")
    def flow_logs(self) -> pulumi.Output[Sequence['outputs.FlowLogResponse']]:
        """
        A collection of references to flow log resources.
        """
        return pulumi.get(self, "flow_logs")

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
        A collection of references to network interfaces.
        """
        return pulumi.get(self, "network_interfaces")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the network security group resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[str]:
        """
        The resource GUID property of the network security group resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter(name="securityRules")
    def security_rules(self) -> pulumi.Output[Optional[Sequence['outputs.SecurityRuleResponse']]]:
        """
        A collection of security rules of the network security group.
        """
        return pulumi.get(self, "security_rules")

    @property
    @pulumi.getter
    def subnets(self) -> pulumi.Output[Sequence['outputs.SubnetResponse']]:
        """
        A collection of references to subnets.
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

