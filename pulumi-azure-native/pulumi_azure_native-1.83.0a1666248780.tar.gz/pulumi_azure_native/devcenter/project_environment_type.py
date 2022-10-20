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

__all__ = ['ProjectEnvironmentTypeArgs', 'ProjectEnvironmentType']

@pulumi.input_type
class ProjectEnvironmentTypeArgs:
    def __init__(__self__, *,
                 project_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 creator_role_assignment: Optional[pulumi.Input['ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs']] = None,
                 deployment_target_id: Optional[pulumi.Input[str]] = None,
                 environment_type_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ManagedServiceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_role_assignments: Optional[pulumi.Input[Mapping[str, pulumi.Input['UserRoleAssignmentArgs']]]] = None):
        """
        The set of arguments for constructing a ProjectEnvironmentType resource.
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the Azure subscription.
        :param pulumi.Input['ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs'] creator_role_assignment: The role definition assigned to the environment creator on backing resources.
        :param pulumi.Input[str] deployment_target_id: Id of a subscription that the environment type will be mapped to. The environment's resources will be deployed into this subscription.
        :param pulumi.Input[str] environment_type_name: The name of the environment type.
        :param pulumi.Input['ManagedServiceIdentityArgs'] identity: Managed identity properties
        :param pulumi.Input[str] location: The geo-location for the environment type
        :param pulumi.Input[Union[str, 'EnableStatus']] status: Defines whether this Environment Type can be used in this Project.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Mapping[str, pulumi.Input['UserRoleAssignmentArgs']]] user_role_assignments: Role Assignments created on environment backing resources. This is a mapping from a user object ID to an object of role definition IDs.
        """
        pulumi.set(__self__, "project_name", project_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if creator_role_assignment is not None:
            pulumi.set(__self__, "creator_role_assignment", creator_role_assignment)
        if deployment_target_id is not None:
            pulumi.set(__self__, "deployment_target_id", deployment_target_id)
        if environment_type_name is not None:
            pulumi.set(__self__, "environment_type_name", environment_type_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if user_role_assignments is not None:
            pulumi.set(__self__, "user_role_assignments", user_role_assignments)

    @property
    @pulumi.getter(name="projectName")
    def project_name(self) -> pulumi.Input[str]:
        """
        The name of the project.
        """
        return pulumi.get(self, "project_name")

    @project_name.setter
    def project_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "project_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="creatorRoleAssignment")
    def creator_role_assignment(self) -> Optional[pulumi.Input['ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs']]:
        """
        The role definition assigned to the environment creator on backing resources.
        """
        return pulumi.get(self, "creator_role_assignment")

    @creator_role_assignment.setter
    def creator_role_assignment(self, value: Optional[pulumi.Input['ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs']]):
        pulumi.set(self, "creator_role_assignment", value)

    @property
    @pulumi.getter(name="deploymentTargetId")
    def deployment_target_id(self) -> Optional[pulumi.Input[str]]:
        """
        Id of a subscription that the environment type will be mapped to. The environment's resources will be deployed into this subscription.
        """
        return pulumi.get(self, "deployment_target_id")

    @deployment_target_id.setter
    def deployment_target_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_target_id", value)

    @property
    @pulumi.getter(name="environmentTypeName")
    def environment_type_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the environment type.
        """
        return pulumi.get(self, "environment_type_name")

    @environment_type_name.setter
    def environment_type_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "environment_type_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ManagedServiceIdentityArgs']]:
        """
        Managed identity properties
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ManagedServiceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location for the environment type
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'EnableStatus']]]:
        """
        Defines whether this Environment Type can be used in this Project.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'EnableStatus']]]):
        pulumi.set(self, "status", value)

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
    @pulumi.getter(name="userRoleAssignments")
    def user_role_assignments(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['UserRoleAssignmentArgs']]]]:
        """
        Role Assignments created on environment backing resources. This is a mapping from a user object ID to an object of role definition IDs.
        """
        return pulumi.get(self, "user_role_assignments")

    @user_role_assignments.setter
    def user_role_assignments(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['UserRoleAssignmentArgs']]]]):
        pulumi.set(self, "user_role_assignments", value)


class ProjectEnvironmentType(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creator_role_assignment: Optional[pulumi.Input[pulumi.InputType['ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs']]] = None,
                 deployment_target_id: Optional[pulumi.Input[str]] = None,
                 environment_type_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_role_assignments: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['UserRoleAssignmentArgs']]]]] = None,
                 __props__=None):
        """
        Represents an environment type.
        API Version: 2022-09-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs']] creator_role_assignment: The role definition assigned to the environment creator on backing resources.
        :param pulumi.Input[str] deployment_target_id: Id of a subscription that the environment type will be mapped to. The environment's resources will be deployed into this subscription.
        :param pulumi.Input[str] environment_type_name: The name of the environment type.
        :param pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']] identity: Managed identity properties
        :param pulumi.Input[str] location: The geo-location for the environment type
        :param pulumi.Input[str] project_name: The name of the project.
        :param pulumi.Input[str] resource_group_name: Name of the resource group within the Azure subscription.
        :param pulumi.Input[Union[str, 'EnableStatus']] status: Defines whether this Environment Type can be used in this Project.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['UserRoleAssignmentArgs']]]] user_role_assignments: Role Assignments created on environment backing resources. This is a mapping from a user object ID to an object of role definition IDs.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ProjectEnvironmentTypeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Represents an environment type.
        API Version: 2022-09-01-preview.

        :param str resource_name: The name of the resource.
        :param ProjectEnvironmentTypeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ProjectEnvironmentTypeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 creator_role_assignment: Optional[pulumi.Input[pulumi.InputType['ProjectEnvironmentTypeUpdatePropertiesCreatorRoleAssignmentArgs']]] = None,
                 deployment_target_id: Optional[pulumi.Input[str]] = None,
                 environment_type_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ManagedServiceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 project_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 user_role_assignments: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['UserRoleAssignmentArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ProjectEnvironmentTypeArgs.__new__(ProjectEnvironmentTypeArgs)

            __props__.__dict__["creator_role_assignment"] = creator_role_assignment
            __props__.__dict__["deployment_target_id"] = deployment_target_id
            __props__.__dict__["environment_type_name"] = environment_type_name
            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            if project_name is None and not opts.urn:
                raise TypeError("Missing required property 'project_name'")
            __props__.__dict__["project_name"] = project_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["user_role_assignments"] = user_role_assignments
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devcenter/v20220801preview:ProjectEnvironmentType"), pulumi.Alias(type_="azure-native:devcenter/v20220901preview:ProjectEnvironmentType"), pulumi.Alias(type_="azure-native:devcenter/v20221012preview:ProjectEnvironmentType")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ProjectEnvironmentType, __self__).__init__(
            'azure-native:devcenter:ProjectEnvironmentType',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ProjectEnvironmentType':
        """
        Get an existing ProjectEnvironmentType resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ProjectEnvironmentTypeArgs.__new__(ProjectEnvironmentTypeArgs)

        __props__.__dict__["creator_role_assignment"] = None
        __props__.__dict__["deployment_target_id"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_role_assignments"] = None
        return ProjectEnvironmentType(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creatorRoleAssignment")
    def creator_role_assignment(self) -> pulumi.Output[Optional['outputs.ProjectEnvironmentTypeUpdatePropertiesResponseCreatorRoleAssignment']]:
        """
        The role definition assigned to the environment creator on backing resources.
        """
        return pulumi.get(self, "creator_role_assignment")

    @property
    @pulumi.getter(name="deploymentTargetId")
    def deployment_target_id(self) -> pulumi.Output[Optional[str]]:
        """
        Id of a subscription that the environment type will be mapped to. The environment's resources will be deployed into this subscription.
        """
        return pulumi.get(self, "deployment_target_id")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ManagedServiceIdentityResponse']]:
        """
        Managed identity properties
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The geo-location for the environment type
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Defines whether this Environment Type can be used in this Project.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userRoleAssignments")
    def user_role_assignments(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.UserRoleAssignmentResponse']]]:
        """
        Role Assignments created on environment backing resources. This is a mapping from a user object ID to an object of role definition IDs.
        """
        return pulumi.get(self, "user_role_assignments")

