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

__all__ = ['AssignmentArgs', 'Assignment']

@pulumi.input_type
class AssignmentArgs:
    def __init__(__self__, *,
                 identity: pulumi.Input['ManagedServiceIdentityArgs'],
                 parameters: pulumi.Input[Mapping[str, pulumi.Input['ParameterValueBaseArgs']]],
                 resource_groups: pulumi.Input[Mapping[str, pulumi.Input['ResourceGroupValueArgs']]],
                 assignment_name: Optional[pulumi.Input[str]] = None,
                 blueprint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 locks: Optional[pulumi.Input['AssignmentLockSettingsArgs']] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Assignment resource.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: Managed Service Identity for this Blueprint assignment
        :param pulumi.Input[Mapping[str, pulumi.Input['ParameterValueBaseArgs']]] parameters: Blueprint parameter values.
        :param pulumi.Input[Mapping[str, pulumi.Input['ResourceGroupValueArgs']]] resource_groups: Names and locations of resource group placeholders.
        :param pulumi.Input[str] assignment_name: name of the assignment.
        :param pulumi.Input[str] blueprint_id: ID of the Blueprint definition resource.
        :param pulumi.Input[str] description: Multi-line explain this resource.
        :param pulumi.Input[str] display_name: One-liner string explain this resource.
        :param pulumi.Input[str] location: The location of this Blueprint assignment.
        :param pulumi.Input['AssignmentLockSettingsArgs'] locks: Defines how Blueprint-managed resources will be locked.
        :param pulumi.Input[str] subscription_id: azure subscriptionId, which we assign the blueprint to.
        """
        pulumi.set(__self__, "identity", identity)
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "resource_groups", resource_groups)
        if assignment_name is not None:
            pulumi.set(__self__, "assignment_name", assignment_name)
        if blueprint_id is not None:
            pulumi.set(__self__, "blueprint_id", blueprint_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if locks is not None:
            pulumi.set(__self__, "locks", locks)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Input['ManagedServiceIdentityArgs']:
        """
        Managed Service Identity for this Blueprint assignment
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: pulumi.Input['ManagedServiceIdentityArgs']):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Mapping[str, pulumi.Input['ParameterValueBaseArgs']]]:
        """
        Blueprint parameter values.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: pulumi.Input[Mapping[str, pulumi.Input['ParameterValueBaseArgs']]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> pulumi.Input[Mapping[str, pulumi.Input['ResourceGroupValueArgs']]]:
        """
        Names and locations of resource group placeholders.
        """
        return pulumi.get(self, "resource_groups")

    @resource_groups.setter
    def resource_groups(self, value: pulumi.Input[Mapping[str, pulumi.Input['ResourceGroupValueArgs']]]):
        pulumi.set(self, "resource_groups", value)

    @property
    @pulumi.getter(name="assignmentName")
    def assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the assignment.
        """
        return pulumi.get(self, "assignment_name")

    @assignment_name.setter
    def assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assignment_name", value)

    @property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the Blueprint definition resource.
        """
        return pulumi.get(self, "blueprint_id")

    @blueprint_id.setter
    def blueprint_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "blueprint_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Multi-line explain this resource.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        One-liner string explain this resource.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of this Blueprint assignment.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def locks(self) -> Optional[pulumi.Input['AssignmentLockSettingsArgs']]:
        """
        Defines how Blueprint-managed resources will be locked.
        """
        return pulumi.get(self, "locks")

    @locks.setter
    def locks(self, value: Optional[pulumi.Input['AssignmentLockSettingsArgs']]):
        pulumi.set(self, "locks", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        azure subscriptionId, which we assign the blueprint to.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)


warnings.warn("""Version 2017-11-11-preview will be removed in v2 of the provider.""", DeprecationWarning)


class Assignment(pulumi.CustomResource):
    warnings.warn("""Version 2017-11-11-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignment_name: Optional[pulumi.Input[str]] = None,
                 blueprint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 locks: Optional[pulumi.Input[pulumi.InputType['AssignmentLockSettingsArgs']]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterValueBaseArgs']]]]] = None,
                 resource_groups: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ResourceGroupValueArgs']]]]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Represents a Blueprint assignment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] assignment_name: name of the assignment.
        :param pulumi.Input[str] blueprint_id: ID of the Blueprint definition resource.
        :param pulumi.Input[str] description: Multi-line explain this resource.
        :param pulumi.Input[str] display_name: One-liner string explain this resource.
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: Managed Service Identity for this Blueprint assignment
        :param pulumi.Input[str] location: The location of this Blueprint assignment.
        :param pulumi.Input[pulumi.InputType['AssignmentLockSettingsArgs']] locks: Defines how Blueprint-managed resources will be locked.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterValueBaseArgs']]]] parameters: Blueprint parameter values.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ResourceGroupValueArgs']]]] resource_groups: Names and locations of resource group placeholders.
        :param pulumi.Input[str] subscription_id: azure subscriptionId, which we assign the blueprint to.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents a Blueprint assignment.

        :param str resource_name: The name of the resource.
        :param AssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignment_name: Optional[pulumi.Input[str]] = None,
                 blueprint_id: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 locks: Optional[pulumi.Input[pulumi.InputType['AssignmentLockSettingsArgs']]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ParameterValueBaseArgs']]]]] = None,
                 resource_groups: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['ResourceGroupValueArgs']]]]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""Assignment is deprecated: Version 2017-11-11-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssignmentArgs.__new__(AssignmentArgs)

            __props__.__dict__["assignment_name"] = assignment_name
            __props__.__dict__["blueprint_id"] = blueprint_id
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if identity is None and not opts.urn:
                raise TypeError("Missing required property 'identity'")
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["locks"] = locks
            if parameters is None and not opts.urn:
                raise TypeError("Missing required property 'parameters'")
            __props__.__dict__["parameters"] = parameters
            if resource_groups is None and not opts.urn:
                raise TypeError("Missing required property 'resource_groups'")
            __props__.__dict__["resource_groups"] = resource_groups
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        super(Assignment, __self__).__init__(
            'azure-native:blueprint/v20171111preview:Assignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Assignment':
        """
        Get an existing Assignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssignmentArgs.__new__(AssignmentArgs)

        __props__.__dict__["blueprint_id"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["locks"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_groups"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return Assignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="blueprintId")
    def blueprint_id(self) -> pulumi.Output[Optional[str]]:
        """
        ID of the Blueprint definition resource.
        """
        return pulumi.get(self, "blueprint_id")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Multi-line explain this resource.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        One-liner string explain this resource.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output['outputs.ManagedServiceIdentityResponse']:
        """
        Managed Service Identity for this Blueprint assignment
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The location of this Blueprint assignment.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def locks(self) -> pulumi.Output[Optional['outputs.AssignmentLockSettingsResponse']]:
        """
        Defines how Blueprint-managed resources will be locked.
        """
        return pulumi.get(self, "locks")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Mapping[str, 'outputs.ParameterValueBaseResponse']]:
        """
        Blueprint parameter values.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        State of the assignment.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceGroups")
    def resource_groups(self) -> pulumi.Output[Mapping[str, 'outputs.ResourceGroupValueResponse']]:
        """
        Names and locations of resource group placeholders.
        """
        return pulumi.get(self, "resource_groups")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output['outputs.AssignmentStatusResponse']:
        """
        Status of Blueprint assignment. This field is readonly.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")

