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
    'ListPartnerNamespaceSharedAccessKeysResult',
    'AwaitableListPartnerNamespaceSharedAccessKeysResult',
    'list_partner_namespace_shared_access_keys',
    'list_partner_namespace_shared_access_keys_output',
]

@pulumi.output_type
class ListPartnerNamespaceSharedAccessKeysResult:
    """
    Shared access keys of the partner namespace.
    """
    def __init__(__self__, key1=None, key2=None):
        if key1 and not isinstance(key1, str):
            raise TypeError("Expected argument 'key1' to be a str")
        pulumi.set(__self__, "key1", key1)
        if key2 and not isinstance(key2, str):
            raise TypeError("Expected argument 'key2' to be a str")
        pulumi.set(__self__, "key2", key2)

    @property
    @pulumi.getter
    def key1(self) -> Optional[str]:
        """
        Shared access key1 for the partner namespace.
        """
        return pulumi.get(self, "key1")

    @property
    @pulumi.getter
    def key2(self) -> Optional[str]:
        """
        Shared access key2 for the partner namespace.
        """
        return pulumi.get(self, "key2")


class AwaitableListPartnerNamespaceSharedAccessKeysResult(ListPartnerNamespaceSharedAccessKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListPartnerNamespaceSharedAccessKeysResult(
            key1=self.key1,
            key2=self.key2)


def list_partner_namespace_shared_access_keys(partner_namespace_name: Optional[str] = None,
                                              resource_group_name: Optional[str] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListPartnerNamespaceSharedAccessKeysResult:
    """
    Shared access keys of the partner namespace.


    :param str partner_namespace_name: Name of the partner namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    __args__ = dict()
    __args__['partnerNamespaceName'] = partner_namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventgrid/v20201015preview:listPartnerNamespaceSharedAccessKeys', __args__, opts=opts, typ=ListPartnerNamespaceSharedAccessKeysResult).value

    return AwaitableListPartnerNamespaceSharedAccessKeysResult(
        key1=__ret__.key1,
        key2=__ret__.key2)


@_utilities.lift_output_func(list_partner_namespace_shared_access_keys)
def list_partner_namespace_shared_access_keys_output(partner_namespace_name: Optional[pulumi.Input[str]] = None,
                                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListPartnerNamespaceSharedAccessKeysResult]:
    """
    Shared access keys of the partner namespace.


    :param str partner_namespace_name: Name of the partner namespace.
    :param str resource_group_name: The name of the resource group within the user's subscription.
    """
    ...
