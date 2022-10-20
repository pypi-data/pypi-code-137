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

__all__ = ['SqlPoolArgs', 'SqlPool']

@pulumi.input_type
class SqlPoolArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 workspace_name: pulumi.Input[str],
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_size_bytes: Optional[pulumi.Input[float]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['SkuArgs']] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 storage_account_type: Optional[pulumi.Input[Union[str, 'StorageAccountType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a SqlPool resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] workspace_name: The name of the workspace
        :param pulumi.Input[str] collation: Collation mode
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: Specifies the mode of sql pool creation.
               
               Default: regular sql pool creation.
               
               PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified.
               
               Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as the recoverableDatabaseId to restore.
               
               Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified.
        :param pulumi.Input[str] creation_date: Date the SQL pool was created
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[float] max_size_bytes: Maximum size in bytes
        :param pulumi.Input[str] provisioning_state: Resource state
        :param pulumi.Input[str] recoverable_database_id: Backup database to restore from
        :param pulumi.Input[str] restore_point_in_time: Snapshot time to restore
        :param pulumi.Input['SkuArgs'] sku: SQL pool SKU
        :param pulumi.Input[str] source_database_id: Source database to create from
        :param pulumi.Input[str] sql_pool_name: SQL pool name
        :param pulumi.Input[str] status: Resource status
        :param pulumi.Input[Union[str, 'StorageAccountType']] storage_account_type: The storage account type used to store backups for this sql pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "workspace_name", workspace_name)
        if collation is not None:
            pulumi.set(__self__, "collation", collation)
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if creation_date is not None:
            pulumi.set(__self__, "creation_date", creation_date)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if max_size_bytes is not None:
            pulumi.set(__self__, "max_size_bytes", max_size_bytes)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if recoverable_database_id is not None:
            pulumi.set(__self__, "recoverable_database_id", recoverable_database_id)
        if restore_point_in_time is not None:
            pulumi.set(__self__, "restore_point_in_time", restore_point_in_time)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if source_database_id is not None:
            pulumi.set(__self__, "source_database_id", source_database_id)
        if sql_pool_name is not None:
            pulumi.set(__self__, "sql_pool_name", sql_pool_name)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if storage_account_type is not None:
            pulumi.set(__self__, "storage_account_type", storage_account_type)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="workspaceName")
    def workspace_name(self) -> pulumi.Input[str]:
        """
        The name of the workspace
        """
        return pulumi.get(self, "workspace_name")

    @workspace_name.setter
    def workspace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_name", value)

    @property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[str]]:
        """
        Collation mode
        """
        return pulumi.get(self, "collation")

    @collation.setter
    def collation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collation", value)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[str, 'CreateMode']]]:
        """
        Specifies the mode of sql pool creation.

        Default: regular sql pool creation.

        PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified.

        Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as the recoverableDatabaseId to restore.

        Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified.
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[str, 'CreateMode']]]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> Optional[pulumi.Input[str]]:
        """
        Date the SQL pool was created
        """
        return pulumi.get(self, "creation_date")

    @creation_date.setter
    def creation_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_date", value)

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
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> Optional[pulumi.Input[float]]:
        """
        Maximum size in bytes
        """
        return pulumi.get(self, "max_size_bytes")

    @max_size_bytes.setter
    def max_size_bytes(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "max_size_bytes", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Resource state
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="recoverableDatabaseId")
    def recoverable_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        Backup database to restore from
        """
        return pulumi.get(self, "recoverable_database_id")

    @recoverable_database_id.setter
    def recoverable_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recoverable_database_id", value)

    @property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> Optional[pulumi.Input[str]]:
        """
        Snapshot time to restore
        """
        return pulumi.get(self, "restore_point_in_time")

    @restore_point_in_time.setter
    def restore_point_in_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_point_in_time", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['SkuArgs']]:
        """
        SQL pool SKU
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['SkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="sourceDatabaseId")
    def source_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        Source database to create from
        """
        return pulumi.get(self, "source_database_id")

    @source_database_id.setter
    def source_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_database_id", value)

    @property
    @pulumi.getter(name="sqlPoolName")
    def sql_pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        SQL pool name
        """
        return pulumi.get(self, "sql_pool_name")

    @sql_pool_name.setter
    def sql_pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "sql_pool_name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[str]]:
        """
        Resource status
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> Optional[pulumi.Input[Union[str, 'StorageAccountType']]]:
        """
        The storage account type used to store backups for this sql pool.
        """
        return pulumi.get(self, "storage_account_type")

    @storage_account_type.setter
    def storage_account_type(self, value: Optional[pulumi.Input[Union[str, 'StorageAccountType']]]):
        pulumi.set(self, "storage_account_type", value)

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


warnings.warn("""Version 2020-12-01 will be removed in v2 of the provider.""", DeprecationWarning)


class SqlPool(pulumi.CustomResource):
    warnings.warn("""Version 2020-12-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_size_bytes: Optional[pulumi.Input[float]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 storage_account_type: Optional[pulumi.Input[Union[str, 'StorageAccountType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A SQL Analytics pool

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] collation: Collation mode
        :param pulumi.Input[Union[str, 'CreateMode']] create_mode: Specifies the mode of sql pool creation.
               
               Default: regular sql pool creation.
               
               PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified.
               
               Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as the recoverableDatabaseId to restore.
               
               Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified.
        :param pulumi.Input[str] creation_date: Date the SQL pool was created
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[float] max_size_bytes: Maximum size in bytes
        :param pulumi.Input[str] provisioning_state: Resource state
        :param pulumi.Input[str] recoverable_database_id: Backup database to restore from
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] restore_point_in_time: Snapshot time to restore
        :param pulumi.Input[pulumi.InputType['SkuArgs']] sku: SQL pool SKU
        :param pulumi.Input[str] source_database_id: Source database to create from
        :param pulumi.Input[str] sql_pool_name: SQL pool name
        :param pulumi.Input[str] status: Resource status
        :param pulumi.Input[Union[str, 'StorageAccountType']] storage_account_type: The storage account type used to store backups for this sql pool.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] workspace_name: The name of the workspace
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SqlPoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A SQL Analytics pool

        :param str resource_name: The name of the resource.
        :param SqlPoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SqlPoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'CreateMode']]] = None,
                 creation_date: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 max_size_bytes: Optional[pulumi.Input[float]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['SkuArgs']]] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 sql_pool_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[str]] = None,
                 storage_account_type: Optional[pulumi.Input[Union[str, 'StorageAccountType']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 workspace_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""SqlPool is deprecated: Version 2020-12-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SqlPoolArgs.__new__(SqlPoolArgs)

            __props__.__dict__["collation"] = collation
            __props__.__dict__["create_mode"] = create_mode
            __props__.__dict__["creation_date"] = creation_date
            __props__.__dict__["location"] = location
            __props__.__dict__["max_size_bytes"] = max_size_bytes
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["recoverable_database_id"] = recoverable_database_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["restore_point_in_time"] = restore_point_in_time
            __props__.__dict__["sku"] = sku
            __props__.__dict__["source_database_id"] = source_database_id
            __props__.__dict__["sql_pool_name"] = sql_pool_name
            __props__.__dict__["status"] = status
            __props__.__dict__["storage_account_type"] = storage_account_type
            __props__.__dict__["tags"] = tags
            if workspace_name is None and not opts.urn:
                raise TypeError("Missing required property 'workspace_name'")
            __props__.__dict__["workspace_name"] = workspace_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:synapse:SqlPool"), pulumi.Alias(type_="azure-native:synapse/v20190601preview:SqlPool"), pulumi.Alias(type_="azure-native:synapse/v20200401preview:SqlPool"), pulumi.Alias(type_="azure-native:synapse/v20210301:SqlPool"), pulumi.Alias(type_="azure-native:synapse/v20210401preview:SqlPool"), pulumi.Alias(type_="azure-native:synapse/v20210501:SqlPool"), pulumi.Alias(type_="azure-native:synapse/v20210601:SqlPool"), pulumi.Alias(type_="azure-native:synapse/v20210601preview:SqlPool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(SqlPool, __self__).__init__(
            'azure-native:synapse/v20201201:SqlPool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'SqlPool':
        """
        Get an existing SqlPool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SqlPoolArgs.__new__(SqlPoolArgs)

        __props__.__dict__["collation"] = None
        __props__.__dict__["create_mode"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["max_size_bytes"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["recoverable_database_id"] = None
        __props__.__dict__["restore_point_in_time"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["source_database_id"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["storage_account_type"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return SqlPool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def collation(self) -> pulumi.Output[Optional[str]]:
        """
        Collation mode
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> pulumi.Output[Optional[str]]:
        """
        Specifies the mode of sql pool creation.

        Default: regular sql pool creation.

        PointInTimeRestore: Creates a sql pool by restoring a point in time backup of an existing sql pool. sourceDatabaseId must be specified as the resource ID of the existing sql pool, and restorePointInTime must be specified.

        Recovery: Creates a sql pool by a geo-replicated backup. sourceDatabaseId  must be specified as the recoverableDatabaseId to restore.

        Restore: Creates a sql pool by restoring a backup of a deleted sql  pool. SourceDatabaseId should be the sql pool's original resource ID. SourceDatabaseId and sourceDatabaseDeletionDate must be specified.
        """
        return pulumi.get(self, "create_mode")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[Optional[str]]:
        """
        Date the SQL pool was created
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maxSizeBytes")
    def max_size_bytes(self) -> pulumi.Output[Optional[float]]:
        """
        Maximum size in bytes
        """
        return pulumi.get(self, "max_size_bytes")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Resource state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="recoverableDatabaseId")
    def recoverable_database_id(self) -> pulumi.Output[Optional[str]]:
        """
        Backup database to restore from
        """
        return pulumi.get(self, "recoverable_database_id")

    @property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> pulumi.Output[Optional[str]]:
        """
        Snapshot time to restore
        """
        return pulumi.get(self, "restore_point_in_time")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.SkuResponse']]:
        """
        SQL pool SKU
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sourceDatabaseId")
    def source_database_id(self) -> pulumi.Output[Optional[str]]:
        """
        Source database to create from
        """
        return pulumi.get(self, "source_database_id")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        Resource status
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageAccountType")
    def storage_account_type(self) -> pulumi.Output[Optional[str]]:
        """
        The storage account type used to store backups for this sql pool.
        """
        return pulumi.get(self, "storage_account_type")

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

