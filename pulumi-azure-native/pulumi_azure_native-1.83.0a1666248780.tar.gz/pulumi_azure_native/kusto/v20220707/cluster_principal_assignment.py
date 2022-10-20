# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = ['ClusterPrincipalAssignmentArgs', 'ClusterPrincipalAssignment']

@pulumi.input_type
class ClusterPrincipalAssignmentArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 principal_id: pulumi.Input[str],
                 principal_type: pulumi.Input[Union[str, 'PrincipalType']],
                 resource_group_name: pulumi.Input[str],
                 role: pulumi.Input[Union[str, 'ClusterPrincipalRole']],
                 principal_assignment_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ClusterPrincipalAssignment resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] principal_id: The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name.
        :param pulumi.Input[Union[str, 'PrincipalType']] principal_type: Principal type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[Union[str, 'ClusterPrincipalRole']] role: Cluster principal role.
        :param pulumi.Input[str] principal_assignment_name: The name of the Kusto principalAssignment.
        :param pulumi.Input[str] tenant_id: The tenant id of the principal
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "principal_type", principal_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "role", role)
        if principal_assignment_name is not None:
            pulumi.set(__self__, "principal_assignment_name", principal_assignment_name)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="clusterName")
    def cluster_name(self) -> pulumi.Input[str]:
        """
        The name of the Kusto cluster.
        """
        return pulumi.get(self, "cluster_name")

    @cluster_name.setter
    def cluster_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_name", value)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Input[str]:
        """
        The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name.
        """
        return pulumi.get(self, "principal_id")

    @principal_id.setter
    def principal_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "principal_id", value)

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Input[Union[str, 'PrincipalType']]:
        """
        Principal type.
        """
        return pulumi.get(self, "principal_type")

    @principal_type.setter
    def principal_type(self, value: pulumi.Input[Union[str, 'PrincipalType']]):
        pulumi.set(self, "principal_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group containing the Kusto cluster.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def role(self) -> pulumi.Input[Union[str, 'ClusterPrincipalRole']]:
        """
        Cluster principal role.
        """
        return pulumi.get(self, "role")

    @role.setter
    def role(self, value: pulumi.Input[Union[str, 'ClusterPrincipalRole']]):
        pulumi.set(self, "role", value)

    @property
    @pulumi.getter(name="principalAssignmentName")
    def principal_assignment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Kusto principalAssignment.
        """
        return pulumi.get(self, "principal_assignment_name")

    @principal_assignment_name.setter
    def principal_assignment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "principal_assignment_name", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The tenant id of the principal
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class ClusterPrincipalAssignment(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 principal_assignment_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_type: Optional[pulumi.Input[Union[str, 'PrincipalType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[Union[str, 'ClusterPrincipalRole']]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing a cluster principal assignment.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] principal_assignment_name: The name of the Kusto principalAssignment.
        :param pulumi.Input[str] principal_id: The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name.
        :param pulumi.Input[Union[str, 'PrincipalType']] principal_type: Principal type.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[Union[str, 'ClusterPrincipalRole']] role: Cluster principal role.
        :param pulumi.Input[str] tenant_id: The tenant id of the principal
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ClusterPrincipalAssignmentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing a cluster principal assignment.

        :param str resource_name: The name of the resource.
        :param ClusterPrincipalAssignmentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ClusterPrincipalAssignmentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 principal_assignment_name: Optional[pulumi.Input[str]] = None,
                 principal_id: Optional[pulumi.Input[str]] = None,
                 principal_type: Optional[pulumi.Input[Union[str, 'PrincipalType']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role: Optional[pulumi.Input[Union[str, 'ClusterPrincipalRole']]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ClusterPrincipalAssignmentArgs.__new__(ClusterPrincipalAssignmentArgs)

            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            __props__.__dict__["principal_assignment_name"] = principal_assignment_name
            if principal_id is None and not opts.urn:
                raise TypeError("Missing required property 'principal_id'")
            __props__.__dict__["principal_id"] = principal_id
            if principal_type is None and not opts.urn:
                raise TypeError("Missing required property 'principal_type'")
            __props__.__dict__["principal_type"] = principal_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if role is None and not opts.urn:
                raise TypeError("Missing required property 'role'")
            __props__.__dict__["role"] = role
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["aad_object_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["principal_name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["tenant_name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:kusto:ClusterPrincipalAssignment"), pulumi.Alias(type_="azure-native:kusto/v20191109:ClusterPrincipalAssignment"), pulumi.Alias(type_="azure-native:kusto/v20200215:ClusterPrincipalAssignment"), pulumi.Alias(type_="azure-native:kusto/v20200614:ClusterPrincipalAssignment"), pulumi.Alias(type_="azure-native:kusto/v20200918:ClusterPrincipalAssignment"), pulumi.Alias(type_="azure-native:kusto/v20210101:ClusterPrincipalAssignment"), pulumi.Alias(type_="azure-native:kusto/v20210827:ClusterPrincipalAssignment"), pulumi.Alias(type_="azure-native:kusto/v20220201:ClusterPrincipalAssignment")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ClusterPrincipalAssignment, __self__).__init__(
            'azure-native:kusto/v20220707:ClusterPrincipalAssignment',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ClusterPrincipalAssignment':
        """
        Get an existing ClusterPrincipalAssignment resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ClusterPrincipalAssignmentArgs.__new__(ClusterPrincipalAssignmentArgs)

        __props__.__dict__["aad_object_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["principal_id"] = None
        __props__.__dict__["principal_name"] = None
        __props__.__dict__["principal_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["role"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["tenant_name"] = None
        __props__.__dict__["type"] = None
        return ClusterPrincipalAssignment(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="aadObjectId")
    def aad_object_id(self) -> pulumi.Output[str]:
        """
        The service principal object id in AAD (Azure active directory)
        """
        return pulumi.get(self, "aad_object_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> pulumi.Output[str]:
        """
        The principal ID assigned to the cluster principal. It can be a user email, application ID, or security group name.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="principalName")
    def principal_name(self) -> pulumi.Output[str]:
        """
        The principal name
        """
        return pulumi.get(self, "principal_name")

    @property
    @pulumi.getter(name="principalType")
    def principal_type(self) -> pulumi.Output[str]:
        """
        Principal type.
        """
        return pulumi.get(self, "principal_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def role(self) -> pulumi.Output[str]:
        """
        Cluster principal role.
        """
        return pulumi.get(self, "role")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        The tenant id of the principal
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="tenantName")
    def tenant_name(self) -> pulumi.Output[str]:
        """
        The tenant name of the principal
        """
        return pulumi.get(self, "tenant_name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

