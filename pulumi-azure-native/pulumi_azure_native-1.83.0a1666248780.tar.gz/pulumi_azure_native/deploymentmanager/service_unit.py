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
from ._enums import *
from ._inputs import *

__all__ = ['ServiceUnitArgs', 'ServiceUnit']

@pulumi.input_type
class ServiceUnitArgs:
    def __init__(__self__, *,
                 deployment_mode: pulumi.Input['DeploymentMode'],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 service_topology_name: pulumi.Input[str],
                 target_resource_group: pulumi.Input[str],
                 artifacts: Optional[pulumi.Input['ServiceUnitArtifactsArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 service_unit_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ServiceUnit resource.
        :param pulumi.Input['DeploymentMode'] deployment_mode: Describes the type of ARM deployment to be performed on the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the service resource.
        :param pulumi.Input[str] service_topology_name: The name of the service topology .
        :param pulumi.Input[str] target_resource_group: The Azure Resource Group to which the resources in the service unit belong to or should be deployed to.
        :param pulumi.Input['ServiceUnitArtifactsArgs'] artifacts: The artifacts for the service unit.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] service_unit_name: The name of the service unit resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "deployment_mode", deployment_mode)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "service_topology_name", service_topology_name)
        pulumi.set(__self__, "target_resource_group", target_resource_group)
        if artifacts is not None:
            pulumi.set(__self__, "artifacts", artifacts)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if service_unit_name is not None:
            pulumi.set(__self__, "service_unit_name", service_unit_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Input['DeploymentMode']:
        """
        Describes the type of ARM deployment to be performed on the resource.
        """
        return pulumi.get(self, "deployment_mode")

    @deployment_mode.setter
    def deployment_mode(self, value: pulumi.Input['DeploymentMode']):
        pulumi.set(self, "deployment_mode", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the service resource.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="serviceTopologyName")
    def service_topology_name(self) -> pulumi.Input[str]:
        """
        The name of the service topology .
        """
        return pulumi.get(self, "service_topology_name")

    @service_topology_name.setter
    def service_topology_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_topology_name", value)

    @property
    @pulumi.getter(name="targetResourceGroup")
    def target_resource_group(self) -> pulumi.Input[str]:
        """
        The Azure Resource Group to which the resources in the service unit belong to or should be deployed to.
        """
        return pulumi.get(self, "target_resource_group")

    @target_resource_group.setter
    def target_resource_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_resource_group", value)

    @property
    @pulumi.getter
    def artifacts(self) -> Optional[pulumi.Input['ServiceUnitArtifactsArgs']]:
        """
        The artifacts for the service unit.
        """
        return pulumi.get(self, "artifacts")

    @artifacts.setter
    def artifacts(self, value: Optional[pulumi.Input['ServiceUnitArtifactsArgs']]):
        pulumi.set(self, "artifacts", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="serviceUnitName")
    def service_unit_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the service unit resource.
        """
        return pulumi.get(self, "service_unit_name")

    @service_unit_name.setter
    def service_unit_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "service_unit_name", value)

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


class ServiceUnit(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifacts: Optional[pulumi.Input[pulumi.InputType['ServiceUnitArtifactsArgs']]] = None,
                 deployment_mode: Optional[pulumi.Input['DeploymentMode']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_topology_name: Optional[pulumi.Input[str]] = None,
                 service_unit_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_group: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents the response of a service unit resource.
        API Version: 2019-11-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ServiceUnitArtifactsArgs']] artifacts: The artifacts for the service unit.
        :param pulumi.Input['DeploymentMode'] deployment_mode: Describes the type of ARM deployment to be performed on the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] service_name: The name of the service resource.
        :param pulumi.Input[str] service_topology_name: The name of the service topology .
        :param pulumi.Input[str] service_unit_name: The name of the service unit resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] target_resource_group: The Azure Resource Group to which the resources in the service unit belong to or should be deployed to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServiceUnitArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents the response of a service unit resource.
        API Version: 2019-11-01-preview.

        :param str resource_name: The name of the resource.
        :param ServiceUnitArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServiceUnitArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 artifacts: Optional[pulumi.Input[pulumi.InputType['ServiceUnitArtifactsArgs']]] = None,
                 deployment_mode: Optional[pulumi.Input['DeploymentMode']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 service_topology_name: Optional[pulumi.Input[str]] = None,
                 service_unit_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_group: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServiceUnitArgs.__new__(ServiceUnitArgs)

            __props__.__dict__["artifacts"] = artifacts
            if deployment_mode is None and not opts.urn:
                raise TypeError("Missing required property 'deployment_mode'")
            __props__.__dict__["deployment_mode"] = deployment_mode
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            if service_topology_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_topology_name'")
            __props__.__dict__["service_topology_name"] = service_topology_name
            __props__.__dict__["service_unit_name"] = service_unit_name
            __props__.__dict__["tags"] = tags
            if target_resource_group is None and not opts.urn:
                raise TypeError("Missing required property 'target_resource_group'")
            __props__.__dict__["target_resource_group"] = target_resource_group
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:deploymentmanager/v20180901preview:ServiceUnit"), pulumi.Alias(type_="azure-native:deploymentmanager/v20191101preview:ServiceUnit")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServiceUnit, __self__).__init__(
            'azure-native:deploymentmanager:ServiceUnit',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServiceUnit':
        """
        Get an existing ServiceUnit resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServiceUnitArgs.__new__(ServiceUnitArgs)

        __props__.__dict__["artifacts"] = None
        __props__.__dict__["deployment_mode"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_resource_group"] = None
        __props__.__dict__["type"] = None
        return ServiceUnit(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def artifacts(self) -> pulumi.Output[Optional['outputs.ServiceUnitArtifactsResponse']]:
        """
        The artifacts for the service unit.
        """
        return pulumi.get(self, "artifacts")

    @property
    @pulumi.getter(name="deploymentMode")
    def deployment_mode(self) -> pulumi.Output[str]:
        """
        Describes the type of ARM deployment to be performed on the resource.
        """
        return pulumi.get(self, "deployment_mode")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetResourceGroup")
    def target_resource_group(self) -> pulumi.Output[str]:
        """
        The Azure Resource Group to which the resources in the service unit belong to or should be deployed to.
        """
        return pulumi.get(self, "target_resource_group")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

