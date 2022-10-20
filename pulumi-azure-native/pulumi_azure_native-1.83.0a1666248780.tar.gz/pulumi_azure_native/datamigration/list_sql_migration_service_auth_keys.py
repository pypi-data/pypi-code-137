# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ListSqlMigrationServiceAuthKeysResult',
    'AwaitableListSqlMigrationServiceAuthKeysResult',
    'list_sql_migration_service_auth_keys',
    'list_sql_migration_service_auth_keys_output',
]

@pulumi.output_type
class ListSqlMigrationServiceAuthKeysResult:
    """
    An authentication key.
    """
    def __init__(__self__, auth_key1=None, auth_key2=None):
        if auth_key1 and not isinstance(auth_key1, str):
            raise TypeError("Expected argument 'auth_key1' to be a str")
        pulumi.set(__self__, "auth_key1", auth_key1)
        if auth_key2 and not isinstance(auth_key2, str):
            raise TypeError("Expected argument 'auth_key2' to be a str")
        pulumi.set(__self__, "auth_key2", auth_key2)

    @property
    @pulumi.getter(name="authKey1")
    def auth_key1(self) -> Optional[str]:
        """
        The first authentication key.
        """
        return pulumi.get(self, "auth_key1")

    @property
    @pulumi.getter(name="authKey2")
    def auth_key2(self) -> Optional[str]:
        """
        The second authentication key.
        """
        return pulumi.get(self, "auth_key2")


class AwaitableListSqlMigrationServiceAuthKeysResult(ListSqlMigrationServiceAuthKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSqlMigrationServiceAuthKeysResult(
            auth_key1=self.auth_key1,
            auth_key2=self.auth_key2)


def list_sql_migration_service_auth_keys(resource_group_name: Optional[str] = None,
                                         sql_migration_service_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSqlMigrationServiceAuthKeysResult:
    """
    An authentication key.
    API Version: 2021-10-30-preview.


    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_migration_service_name: Name of the SQL Migration Service.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sqlMigrationServiceName'] = sql_migration_service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datamigration:listSqlMigrationServiceAuthKeys', __args__, opts=opts, typ=ListSqlMigrationServiceAuthKeysResult).value

    return AwaitableListSqlMigrationServiceAuthKeysResult(
        auth_key1=__ret__.auth_key1,
        auth_key2=__ret__.auth_key2)


@_utilities.lift_output_func(list_sql_migration_service_auth_keys)
def list_sql_migration_service_auth_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                sql_migration_service_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListSqlMigrationServiceAuthKeysResult]:
    """
    An authentication key.
    API Version: 2021-10-30-preview.


    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_migration_service_name: Name of the SQL Migration Service.
    """
    ...
