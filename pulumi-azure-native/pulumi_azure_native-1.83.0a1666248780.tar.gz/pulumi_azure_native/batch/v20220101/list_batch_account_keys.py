# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'ListBatchAccountKeysResult',
    'AwaitableListBatchAccountKeysResult',
    'list_batch_account_keys',
    'list_batch_account_keys_output',
]

@pulumi.output_type
class ListBatchAccountKeysResult:
    """
    A set of Azure Batch account keys.
    """
    def __init__(__self__, account_name=None, primary=None, secondary=None):
        if account_name and not isinstance(account_name, str):
            raise TypeError("Expected argument 'account_name' to be a str")
        pulumi.set(__self__, "account_name", account_name)
        if primary and not isinstance(primary, str):
            raise TypeError("Expected argument 'primary' to be a str")
        pulumi.set(__self__, "primary", primary)
        if secondary and not isinstance(secondary, str):
            raise TypeError("Expected argument 'secondary' to be a str")
        pulumi.set(__self__, "secondary", secondary)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> str:
        """
        The Batch account name.
        """
        return pulumi.get(self, "account_name")

    @property
    @pulumi.getter
    def primary(self) -> str:
        """
        The primary key associated with the account.
        """
        return pulumi.get(self, "primary")

    @property
    @pulumi.getter
    def secondary(self) -> str:
        """
        The secondary key associated with the account.
        """
        return pulumi.get(self, "secondary")


class AwaitableListBatchAccountKeysResult(ListBatchAccountKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListBatchAccountKeysResult(
            account_name=self.account_name,
            primary=self.primary,
            secondary=self.secondary)


def list_batch_account_keys(account_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListBatchAccountKeysResult:
    """
    A set of Azure Batch account keys.


    :param str account_name: The name of the Batch account.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:batch/v20220101:listBatchAccountKeys', __args__, opts=opts, typ=ListBatchAccountKeysResult).value

    return AwaitableListBatchAccountKeysResult(
        account_name=__ret__.account_name,
        primary=__ret__.primary,
        secondary=__ret__.secondary)


@_utilities.lift_output_func(list_batch_account_keys)
def list_batch_account_keys_output(account_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListBatchAccountKeysResult]:
    """
    A set of Azure Batch account keys.


    :param str account_name: The name of the Batch account.
    :param str resource_group_name: The name of the resource group that contains the Batch account.
    """
    ...
