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

__all__ = ['AttachedDatabaseConfigurationArgs', 'AttachedDatabaseConfiguration']

@pulumi.input_type
class AttachedDatabaseConfigurationArgs:
    def __init__(__self__, *,
                 cluster_name: pulumi.Input[str],
                 cluster_resource_id: pulumi.Input[str],
                 database_name: pulumi.Input[str],
                 default_principals_modification_kind: pulumi.Input[Union[str, 'DefaultPrincipalsModificationKind']],
                 resource_group_name: pulumi.Input[str],
                 attached_database_configuration_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a AttachedDatabaseConfiguration resource.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] cluster_resource_id: The resource id of the cluster where the databases you would like to attach reside.
        :param pulumi.Input[str] database_name: The name of the database which you would like to attach, use * if you want to follow all current and future databases.
        :param pulumi.Input[Union[str, 'DefaultPrincipalsModificationKind']] default_principals_modification_kind: The default principals modification kind
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        :param pulumi.Input[str] attached_database_configuration_name: The name of the attached database configuration.
        :param pulumi.Input[str] location: Resource location.
        """
        pulumi.set(__self__, "cluster_name", cluster_name)
        pulumi.set(__self__, "cluster_resource_id", cluster_resource_id)
        pulumi.set(__self__, "database_name", database_name)
        pulumi.set(__self__, "default_principals_modification_kind", default_principals_modification_kind)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if attached_database_configuration_name is not None:
            pulumi.set(__self__, "attached_database_configuration_name", attached_database_configuration_name)
        if location is not None:
            pulumi.set(__self__, "location", location)

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
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> pulumi.Input[str]:
        """
        The resource id of the cluster where the databases you would like to attach reside.
        """
        return pulumi.get(self, "cluster_resource_id")

    @cluster_resource_id.setter
    def cluster_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_resource_id", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Input[str]:
        """
        The name of the database which you would like to attach, use * if you want to follow all current and future databases.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="defaultPrincipalsModificationKind")
    def default_principals_modification_kind(self) -> pulumi.Input[Union[str, 'DefaultPrincipalsModificationKind']]:
        """
        The default principals modification kind
        """
        return pulumi.get(self, "default_principals_modification_kind")

    @default_principals_modification_kind.setter
    def default_principals_modification_kind(self, value: pulumi.Input[Union[str, 'DefaultPrincipalsModificationKind']]):
        pulumi.set(self, "default_principals_modification_kind", value)

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
    @pulumi.getter(name="attachedDatabaseConfigurationName")
    def attached_database_configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the attached database configuration.
        """
        return pulumi.get(self, "attached_database_configuration_name")

    @attached_database_configuration_name.setter
    def attached_database_configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "attached_database_configuration_name", value)

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


class AttachedDatabaseConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_database_configuration_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_resource_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 default_principals_modification_kind: Optional[pulumi.Input[Union[str, 'DefaultPrincipalsModificationKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Class representing an attached database configuration.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] attached_database_configuration_name: The name of the attached database configuration.
        :param pulumi.Input[str] cluster_name: The name of the Kusto cluster.
        :param pulumi.Input[str] cluster_resource_id: The resource id of the cluster where the databases you would like to attach reside.
        :param pulumi.Input[str] database_name: The name of the database which you would like to attach, use * if you want to follow all current and future databases.
        :param pulumi.Input[Union[str, 'DefaultPrincipalsModificationKind']] default_principals_modification_kind: The default principals modification kind
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] resource_group_name: The name of the resource group containing the Kusto cluster.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AttachedDatabaseConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Class representing an attached database configuration.

        :param str resource_name: The name of the resource.
        :param AttachedDatabaseConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AttachedDatabaseConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 attached_database_configuration_name: Optional[pulumi.Input[str]] = None,
                 cluster_name: Optional[pulumi.Input[str]] = None,
                 cluster_resource_id: Optional[pulumi.Input[str]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 default_principals_modification_kind: Optional[pulumi.Input[Union[str, 'DefaultPrincipalsModificationKind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AttachedDatabaseConfigurationArgs.__new__(AttachedDatabaseConfigurationArgs)

            __props__.__dict__["attached_database_configuration_name"] = attached_database_configuration_name
            if cluster_name is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_name'")
            __props__.__dict__["cluster_name"] = cluster_name
            if cluster_resource_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_resource_id'")
            __props__.__dict__["cluster_resource_id"] = cluster_resource_id
            if database_name is None and not opts.urn:
                raise TypeError("Missing required property 'database_name'")
            __props__.__dict__["database_name"] = database_name
            if default_principals_modification_kind is None and not opts.urn:
                raise TypeError("Missing required property 'default_principals_modification_kind'")
            __props__.__dict__["default_principals_modification_kind"] = default_principals_modification_kind
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["attached_database_names"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:kusto:AttachedDatabaseConfiguration"), pulumi.Alias(type_="azure-native:kusto/v20190907:AttachedDatabaseConfiguration"), pulumi.Alias(type_="azure-native:kusto/v20191109:AttachedDatabaseConfiguration"), pulumi.Alias(type_="azure-native:kusto/v20200215:AttachedDatabaseConfiguration"), pulumi.Alias(type_="azure-native:kusto/v20200918:AttachedDatabaseConfiguration"), pulumi.Alias(type_="azure-native:kusto/v20210101:AttachedDatabaseConfiguration"), pulumi.Alias(type_="azure-native:kusto/v20210827:AttachedDatabaseConfiguration"), pulumi.Alias(type_="azure-native:kusto/v20220201:AttachedDatabaseConfiguration"), pulumi.Alias(type_="azure-native:kusto/v20220707:AttachedDatabaseConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AttachedDatabaseConfiguration, __self__).__init__(
            'azure-native:kusto/v20200614:AttachedDatabaseConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AttachedDatabaseConfiguration':
        """
        Get an existing AttachedDatabaseConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AttachedDatabaseConfigurationArgs.__new__(AttachedDatabaseConfigurationArgs)

        __props__.__dict__["attached_database_names"] = None
        __props__.__dict__["cluster_resource_id"] = None
        __props__.__dict__["database_name"] = None
        __props__.__dict__["default_principals_modification_kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return AttachedDatabaseConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="attachedDatabaseNames")
    def attached_database_names(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of databases from the clusterResourceId which are currently attached to the cluster.
        """
        return pulumi.get(self, "attached_database_names")

    @property
    @pulumi.getter(name="clusterResourceId")
    def cluster_resource_id(self) -> pulumi.Output[str]:
        """
        The resource id of the cluster where the databases you would like to attach reside.
        """
        return pulumi.get(self, "cluster_resource_id")

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> pulumi.Output[str]:
        """
        The name of the database which you would like to attach, use * if you want to follow all current and future databases.
        """
        return pulumi.get(self, "database_name")

    @property
    @pulumi.getter(name="defaultPrincipalsModificationKind")
    def default_principals_modification_kind(self) -> pulumi.Output[str]:
        """
        The default principals modification kind
        """
        return pulumi.get(self, "default_principals_modification_kind")

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
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

